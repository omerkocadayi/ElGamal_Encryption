# ElGamal_Encryption
ElGamal Key Generation, Encryption, Decryption

ElGamal Signature, Encryption, Decryption

B kişisi; p,d,e1,e2 değerlerini oluşturup açık anahtarları a kişisine iletir.

- rastgele p asal sayısı, açık anahtar
- rastgele d gizli anahtarı
- rastgele e1 açık anahtarı
- e2 = (e1^d) % p , açık anahtar


A kişisi; m=metin, r,c1,c2 değerlerini oluşturup c1 ve c2'yi b kişisine iletir.

- rastgele r gizli anahtarı
- c1 = (e1^r) % p , açık anahtar
- c2 = ((e2^r) * m) %p -> şifreli metin


B kişisi;

- (c2 * [((c1 ^ d) % p)^-1 %p]) %p -> işlemi ile şifreli metni çözer.
