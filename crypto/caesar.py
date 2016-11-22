__author__ = 'ruiqin'

cipher = raw_input('please input the cipher: ')

for i in range(1,26):
    result = ''
    for c in cipher:
        if ord(c) in range(97, 123):
            d = ord(c) + i
            if d > 122:
                d -= 26
            result += chr(d)
        elif ord(c) in range(65, 91):
            d = ord(c) + i
            if d > 90:
                d -= 26
            result += chr(d)
        else:
            result += c
    print result
