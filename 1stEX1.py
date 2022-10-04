mystr = input()
k = True
for i in range(len(mystr)):
    if mystr[i] != mystr[len(mystr)-1-i]:
        k=False
        print(k)
        break
if k==True:
    print("True")