p=int(input("Enter Large Prime Number: "))
d=int(input("Enter Private Key: "))
e1=int(input("Enter Encryption Key (E1): "))
e2=(e1**d)%p
print("Public Key is",(e1,e2,p))
ch=input("Enter 'E':Encryption 'D':Decryption ").upper()
if ch=='E':
    r=int(input("Enter Random Integer: "))
    pt = int(input("Enter Plain Text: "))
    ct1=(e1**r)%p
    ct2=(pt*(e2**r))%p
    print("Cipher Text is", (ct1, ct2))
elif ch=='D':
    ct1 = int(input("Enter Cipher Text 1: "))
    ct2 = int(input("Enter Cipher Text 2: "))
    pt=(ct2*(ct1**((p-1)-d)))%p
    print("Plain Text is",pt)
else:
    print("Invalid Option")