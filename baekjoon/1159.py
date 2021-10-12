N = int(input())
name_cnt = dict()
for i in range(N):
    fam_name = input()
    name_cnt[fam_name[0]] = name_cnt.get(fam_name[0], 0) + 1
ret = ''.join(sorted([k for k, v in name_cnt.items() if v >= 5]))
ret = "PREDAJA" if ret == '' else ret
print(ret)



# 문제가 뭐 이러지;;
# input

# 18
# babic
# keksic
# boric
# bukic
# sarmic
# balic
# kruzic
# hrenovkic
# beslic
# boksic
# krafnic
# pecivic
# klavirkovic
# kukumaric
# sunkic
# kolacic
# kovacic
# prijestolonasljednikovi