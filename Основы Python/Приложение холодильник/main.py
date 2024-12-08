import datetime
from datetime import datetime as dt, timedelta
from decimal import Decimal
from typing import Union
from typing import TypedDict

DATE_FORMAT : str = '%Y-%m-%d'
Product = TypedDict('Product', 
        {'amount' : Decimal, 'expiration_date' : datetime.date | None})

def add(items, title : str, amount : Decimal, expiration_date=None):
    datee = None
    try:
        datee = dt.strptime(expiration_date, DATE_FORMAT).date()
    except TypeError:
        datee = None

    product_info = Product(amount=amount, expiration_date=datee)

    if (title in items):
        items[title].append(product_info)
    else:
        items[title] = [product_info]

def extract_date_or_none(date : str):
    try:
        date_in_dt = dt.strptime(date, DATE_FORMAT)
        return date_in_dt.date()
    except ValueError:
        return None

def format_product_info(product_info : list[str]):
    title = ''
    amount = Decimal('0')
    expiration_date = None
    title_found = False
    for i in product_info:
        c = i[0]
        if c.isdigit() and (not title_found):
            title_found = True
            amount = Decimal(i)
        elif title_found:
            #expiration_date = extract_date_or_none(i)
            expiration_date = i
        else:
            title += i + ' '
    l = len(title)
    title = title[:l - 1]

    return (title, amount, expiration_date)


def add_by_note(items, note : str):
    note_items = note.split()
    title, amount, exp_date = format_product_info(note_items)
    add(items, title, amount, exp_date)


def find(items, needle : str):
    ks = items.keys()
    result = list()
    fin = needle.lower()
    for key in ks:
        if (fin in key.lower()):
            result.append(key)
    return result


def amount(items, needle) -> Decimal:
    total_amount = Decimal('0')
    prods = find(items, needle)
    for p in prods:
        prod_info = items[p]
        for one_prod_info in prod_info:
            total_amount += one_prod_info['amount'] 
    return total_amount


def expire(items, in_advance_days=0):
    result = list()
    now = dt.today()
    date_in_adv = now + timedelta(days=in_advance_days)
    date_in_adv = date_in_adv.date()
    expired = dict()
    for product, product_info in items.items():
        for one_prod_info in product_info:
            date_to = one_prod_info['expiration_date']
            if (date_to is None):
                continue
            if date_to > date_in_adv:
                continue
            if product in expired:
                expired[product] += one_prod_info['amount']
            else:
                expired[product] = one_prod_info['amount']
    for key, value in expired.items():
        result.append(tuple([key, value]))
    return result