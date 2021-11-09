# input
# nice day
# love
# output
# btgz oet

normal_string = input()
encrypt_key = input()

len_enc_key = len(encrypt_key)

for i in range(len(normal_string)):
    if normal_string[i] == " ":
        print(normal_string[i], end="")
        continue
    n, e = ord(normal_string[i])-97, ord(encrypt_key[i%len_enc_key])-96
    ret = n-e if n-e >= 0 else 26+n-e
    print(chr(ret+97), end="")