__author__ = 'ruiqin'

from numpy import *

Dic = {chr(i+97):i for i in range(26)}
def decode(pwd, org):
    temp = []
    result = ''
    while True:
        if len(pwd) % 3 != 0:
            pwd.append(pwd[-1])
        else:
            break
    for i in pwd:
        temp.append(Dic.get(i))
    temp = array(temp)
    temp = temp.reshape(len(pwd)/3, 3)
    #print temp
    #print org
    xx = matrix(temp)*org
    for j in range(len(pwd)/3):
        for i in range(3):
            if (int(xx[j, i]) >= 26):
                #result.append(chr(xx[j, i] % 26 + 97))
                result += chr(xx[j, i] % 26 + 97)
                #print xx[j, i] % 26
            else:
                #print xx[j, i]
                #result.append(chr(xx[j, i] + 97))
                result += chr(xx[j, i] + 97)
    return result

def get_vmatrix(org):
    org_adjoin = org.I*linalg.det(org)
    #print org_adjoin
    org_det = int(str(abs(linalg.det(org))).split('.')[0])
    #print org_det
    for i in range(1, 26):
        if i * org_det % 26 == 1:
            break
    org_mod = -org_adjoin * i % 26
    org_mod = matrix(org_mod)
    temp = []
    for i in range(org_mod.shape[0]):
        for j in range(org_mod.shape[1]):
            temp.append(int(str(org_mod[i, j]).split('.')[0]))
    org_final = matrix(temp).reshape(org_mod.shape[0], org_mod.shape[1])
    return org_final

if __name__ == '__main__':
    cipher_num = raw_input('Input the cipher(use "," to seperate): ').split(',')
    cipher = ''
    for num in cipher_num:
        cipher += chr(int(num) + 97)
    cipher = list(cipher)
    key = raw_input('Input the key(example:[[1,2,3],[4,5,6],[7,8,10]]): ')
    org = matrix(array(key))
    org_vm = get_vmatrix(org)
    print 'The plaintext: ' + decode(cipher, org_vm)