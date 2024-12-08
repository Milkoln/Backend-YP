class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def process_text(self, text, shift, is_encrypt):
        if not is_encrypt:
            shift = - shift
        result = ''
        alph_cap = len(self.alphabet)
        for char in text:
            c = char.lower()
            if (c not in self.alphabet):
                result += c
                continue
            i = self.alphabet.index(c)
            result += self.alphabet[(i + shift) % alph_cap]
        return result


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 