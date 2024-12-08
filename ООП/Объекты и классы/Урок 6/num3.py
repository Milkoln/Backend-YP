class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def cipher(self, original_text, shift) -> str:
        # Метод должен возвращать зашифрованный текст 
        # с учетом переданного смещения shift.
        result = ''
        alph_cap = len(self.alphabet)
        for char in original_text:
            c = char.lower()
            if (c not in self.alphabet):
                result += c
                continue
            i = self.alphabet.index(c)
            result += self.alphabet[(i + shift) % alph_cap]
        return result
    
    
    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        return self.cipher(cipher_text, - shift)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))