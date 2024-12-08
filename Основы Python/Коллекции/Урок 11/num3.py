def is_palindrome(s : str):
    final_str = ''.join(s.split()).lower()
    reversed_str = final_str[::-1]
    return final_str == reversed_str



# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))