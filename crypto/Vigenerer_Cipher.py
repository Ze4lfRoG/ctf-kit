__author__ = 'ruiqin'

def encrypt():
	text = raw_input('Please input plaintext: ').lower()
	key =raw_input('Please input key: ').lower()
	length_text = len(text)
	length_key = len(key)
	cipher_result = ''
	special_count = 0
	for n in range(length_text):
		if ord(text[n]) >= 97 and ord(text[n]) <= 122:
			cipher_ascii = ord(text[n]) + (ord(key[(n - special_count) % length_key]) - 97)
			if cipher_ascii > 122:
				cipher_ascii = cipher_ascii - 26
			cipher = chr(cipher_ascii)
			cipher_result = cipher_result + cipher
		else:
			cipher_result = cipher_result + text[n]
			special_count = special_count + 1
		
	print cipher_result

def decrypt():
	cipher = raw_input('Please input ciphertext: ').lower()
	key = raw_input('Please input key: ').lower()
	length_cipher = len(cipher)
	length_key = len(key)
	text_result = ''
	special_count = 0
	for n in range(length_cipher):
		if ord(cipher[n]) >= 97 and ord(cipher[n]) <= 122:
			text_ascii = ord(cipher[n]) - (ord(key[(n - special_count) % length_key]) - 97)
			if text_ascii < 97:
				text_ascii = text_ascii + 26
			text = chr(text_ascii)
			text_result = text_result + text
		else:
			text_result = text_result + cipher[n]
			special_count = special_count + 1
		
	print text_result

if __name__ == '__main__':
	choice = raw_input('Do you want to use encryption or decryption? (e/d)')
	if choice == 'e':
		encrypt()
	elif choice == 'd':
		decrypt()
	else:
		pass