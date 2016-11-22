__author__ = 'ruiqin'

cipher = raw_input('Input the cipher: ')
length = len(cipher)
factor_arr = []
for a in range(2, length):
    if length % a == 0:
        factor_arr.append([a, length / a])
for factor in factor_arr:
    plain = ''
    a = factor[0]
    b = factor[1]
    for i in range(a):
        for j in range(b):
            plain += cipher[j * a + i]
    print plain
