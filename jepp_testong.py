ex1 = str(1.01233333)
ex2 = str(11.9999999)
ex3 = str(00.0001)
#
# # nex1 = format(ex1, '.4f')
# # nex2 = format(ex2, '.4f')
# # nex3 = format(ex3, '.4f')
#
# # digits = 2  # Specify how many digits you want
# # fnum = '122.485221'
# # truncated_float = float(fnum[:fnum.find('.') + digits + 1])
#
# numstring = str(0.99999)
# num = float(numstring[:numstring.index('.')+5])
# print(num)
#
nex11 = float(ex1[:ex1.index(".") + 5])
nex22 = float(ex2[:ex2.index(".") + 5])
nex33 = float(ex3[:ex3.index(".") + 5])

print(nex11)
print(nex22)
print(nex33)
