from pwn import xor

data = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
#part_key = xor(data, 'crypto{}'.encode())
#print(part_key)
flag = xor(data, 'myXORkey'.encode())
print(flag.decode())