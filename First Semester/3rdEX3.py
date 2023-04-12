mylist = list(map(str, input().split()))
#mylist = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
length = len(mylist)
data = dict()
answer = []
wlist = [0]*length #Будем записывать кортежами (набор букв, длина) и, если они совпадают, то закидывать в один массив

for i in range(length):
    wtuple = "".join(sorted(list(set(mylist[i])))), len(mylist[i])
    wlist[i] = wtuple

for i in range(length):
    if wlist[i] in data.keys():
        data[wlist[i]].append(mylist[i])
    else:
        data[wlist[i]] = [mylist[i]]

for i in data.keys():
    answer.append(data[i])

print(answer)