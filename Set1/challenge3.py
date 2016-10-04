encrypted_message = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def decryptor(message, key):
	decrypted_message = []
	for letter in message.decode('hex'):
		decrypted_message.append(chr(ord(letter)^key))
	return ''.join(decrypted_message)

for i in range(128): # every character in the ascii range
	print "Key: %s\t Decrypted Message: %s" % (chr(i), decryptor(encrypted_message, i))
