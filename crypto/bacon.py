__author__ = 'ruiqin'

cipher = raw_input('Input the cipher: ')
result = ''
l = len(cipher)/5
for i in range(l):
    c = cipher[i*5:(i+1)*5]
    c = c.replace('a', '0').replace('b', '1')
    result += chr(int(c, 2) + ord('a'))
print 'The plaintext: ' + result