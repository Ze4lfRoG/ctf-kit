'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator
import binascii

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        #print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    #test_hack_RSA()
    #e = 65537
    n = '03:67:19:8d:6b:56:14:e9:58:13:ad:d8:f2:2a:47:17:bc:72:be:1e:ab:d9:33:d1:b8:69:44:fd:b7:5b:8e:d2:30:be:62:d7:d1:b6:9d:22:20:95:c1:28:c8:6f:82:01:2e:cb:11:61:91:fd:9d:01:8a:6d:02:f8:4d:b2:7b:c5:1a:21:30:7d:c8:6f:4b:f7:71:c6:91:c1:43:e5:ab:e5:49:b5:bd:2d:6e:b1:a2:1f:d6:27:0e:7e:1b:48:fe:06:11:fb:b2:e1:b0:b3:52:4e:6f:4d:e8:b4:e4:a3:45:da:44:a1:3d:e8:25:b7:26:08:db:6c:7c:4a:40:b7:82:66:e6:c8:7b:bf:de:f6:b4:83:81:d4:9c:45:07:a5:8b:cd:47:b7:6d:64:b4:59:08:b1:58:bd:7e:bc:4d:ac:b0:b1:cf:d6:c2:c1:95:74:f4:0e:b2:ef:d0:e9:e1:0d:c7:00:5c:ad:39:bc:af:52:b9:ea:c3:87:33:68:d6:90:31:c5:e7:24:68:4a:44:f0:68:ef:d1:d3:dc:09:6d:9b:5d:64:11:e5:8b:de:e4:3e:46:b9:9a:0d:04:94:b9:db:28:19:5a:f9:01:af:f1:30:d4:a6:e2:03:da:d0:8d:a5:7f:a7:e4:02:62:a5:ba:db:2a:32:3e:da:28:b4:46:96:ab:30:5d'
    n = n.replace(':','')
    e = '00:f3:95:9d:97:8e:02:eb:9f:06:de:f3:f3:35:d8:f8:af:d7:60:99:51:dd:ac:60:b7:14:b6:c2:2a:f0:fa:91:2f:21:0b:34:20:6b:d2:4a:96:01:c7:8d:f4:a0:27:5f:10:7f:d3:ab:55:2d:95:05:7e:b9:34:e7:1b:dd:cd:70:45:c2:4b:18:58:7b:8c:8f:cf:5a:dd:4c:5d:83:f0:c7:7c:94:dc:9c:50:cb:e4:38:e2:b6:7b:af:d3:16:33:b6:aa:f1:78:1d:90:c3:ad:6f:03:d0:37:b3:32:18:01:b2:35:46:d4:83:e6:7e:26:06:7f:7b:22:34:7d:db:c0:c2:d5:92:ce:81:4c:bf:5d:fc:cc:14:14:37:f1:4e:0b:39:90:f8:80:61:e5:f0:ba:e5:f0:1e:3f:a7:0d:b0:e9:60:5e:7c:fd:57:5e:9c:81:ef:ee:c5:29:c3:3f:d9:03:7a:20:fd:8a:cd:51:3a:c9:63:77:68:31:3e:63:f9:83:8a:e3:51:1c:dd:0a:9a:2b:51:6f:21:48:c8:d4:75:a3:60:a0:63:59:44:97:39:ee:cd:25:1a:bb:42:b0:14:57:3e:43:9f:2f:a4:57:35:57:b2:56:99:ff:c1:1e:63:1c:e8:ee:97:5a:86:e7:e2:72:bc:f5:f7:6a:93:45:03:48:fe:3f'
    e = e.replace(':','')
    #m = '00b62dce9f2581635723db6b188f12f0469cbee0cbc5dacb36c36e0c96b6ea7bfc'
    #n = int(m, 16)
    n = int(n, 16)
    e = int(e, 16)
    d = hack_RSA(e, n)
    print d
    c = '1e04304936215de8e21965cfca9c245b1a8f38339875d36779c0f123c475bc24d5eef50e7d9ff5830e80c62e8083ec55f27456c80b0ab26546b9aeb8af30e82b650690a2ed7ea407dcd094ab9c9d3d25a93b2140dcebae1814610302896e67f3ae37d108cd029fae6362ea7ac1168974c1a747ec9173799e1107e7a56d783660418ebdf6898d7037cea25867093216c2c702ef3eef71f694a6063f5f0f1179c8a2afe9898ae8dec5bb393cdffa3a52a297cd96d1ea602309ecf47cd009829b44ed3100cf6194510c53c25ca7435f60ce5f4f614cdd2c63756093b848a70aade002d6bc8f316c9e5503f32d39a56193d1d92b697b48f5aa43417631846824b5e86'
    c = int(c, 16)
    result = hex(pow(c, d, n))
    result = result[2:][:-1]
    result = binascii.a2b_hex(result)
    print result