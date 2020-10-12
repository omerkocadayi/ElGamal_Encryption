""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """
    
import random  
import libnum

def Get_Public_Key():
    
    f = open("primes.txt")
    primes = f.readlines()
    index = random.randint(0,len(primes))   
    
    p = int(primes[index])       #Prime number between 1k and 100k
    d = random.randint(1, p-1)   #Private Key
    e1 = random.randint(1, p-1)  #Public Key
    e2 = pow(e1,d,p)
    
    return p, d, e1, e2


def Encrypt(msg, p, e1, e2): 
  
    en_msg = [] 
    r = random.randint(1,p-1) 
    c1 = pow(e1,r,p)
    
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
        
    for i in range(0, len(en_msg)): 
        en_msg[i] = (pow(e2,r) * ord(en_msg[i])) % p
  
    print("A Public Key -> (c1):",c1,"\nA Private Key-> (r)\t:",r)
    print("\nTotal Character : ",len(en_msg),"\n\nEncrypted Message :", en_msg);
    return en_msg, c1


def Decrypt(en_msg, p, d, e1, c1): 
  
    de_msg = [] 
    for i in range(0, len(en_msg)):         
        de_msg.append(chr((int(en_msg[i]) * libnum.invmod(pow(c1,d,p),p)) % p))
        
    return de_msg 
  

def main(): 
    
    p, d, e1, e2 = Get_Public_Key()
    print("B Public Key -> (p)\t:",p,", (e1):",e1,", (e2):",e2,"\nB Private Key-> (d)\t:",d)
    
    msg = "Omer_Faruk_Kocadayi"    
    en_msg, c1 = Encrypt(msg, p, e1, e2)
    de_msg = Decrypt(en_msg, p, d, e1, c1)
     
    dmsg = ''.join(de_msg) 
    print("\nDecrypted Message :", dmsg);
    
if __name__ == '__main__': 
    main() 

"""
B kişisi; p,d,e1,e2 değerlerin, oluşturup açık anahtarları a kişisine iletir.
.rastgele p asal sayısı, açık anahtar
.rastgele d gizli anahtarı
.rastgele e1 açık anahtarı
. e2 = (e1^d) % p , açık anahtar

A kişisi; m=metin, r,c1,c2 değerlerini oluşturup c1 ve c2'yi b kişisine iletir.
.rastgele r gizli anahtarı
.c1 = (e1^r) % p , açık anahtar
.c2 = ((e2^r) * m) %p   -> şifreli metin

B kişisi;
.(c2 * [((c1 ^ d) % p)^-1 %p]) %p  -> işlemi ile şifreli metni çözer.
"""