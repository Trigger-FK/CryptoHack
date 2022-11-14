from pwn import xor

key1 = 'label'
key2 = 13
flag = xor(key1, key2)

print('crypto{{{}}}'.format(flag.decode()))