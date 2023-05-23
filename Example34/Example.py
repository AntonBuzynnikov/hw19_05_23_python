data = input('Текст кричалки:')
userSet ={"ё","у","е","э","о","а","ы","я","и","ю"}
def glas(x):
    res = list()
    for i in x:
        sum = 0
        for j in i:
             j = j.lower()
             if j in userSet:
                 sum = sum + 1
        res.append(sum)
    return res
if len(set(glas(data.split(' ')))) == 1:
    print("Парам пам пам")
else:
    print("Пам парам")


