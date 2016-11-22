__author__ = 'ruiqin'

def affine(a, b):
    pwd_dic = {}
    for i in range(26):
        pwd_dic[chr(((a*i+b)%26)+97)] = chr(i+97)
    return pwd_dic

if __name__ == '__main__':
    cipher_dic = {}
    cipher = raw_input('Input the cipher: ')
    func = raw_input('Input the function: ').replace(' ', '')
    plain = ""
    func = func.split('=')[1]
    a = int(func.split('x+')[0])
    b = int(func.split('x+')[1])
    cipher_dic = affine(a, b)
    for i in cipher:
        plain += cipher_dic[i]
    print 'The plaintext: ' + plain
