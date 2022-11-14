from pwn import xor

key = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
KEY = bytes.fromhex(key)

for i in range(256):
    flag = (xor(KEY, i)).decode()
    if flag[:7] == 'crypto{':
        print(flag)