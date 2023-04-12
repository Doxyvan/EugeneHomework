def main1():
    num = input()
    answer = ""
    for i in range(len(num)-1,-1,-1):
        answer = answer + num[i]
    if int(num) < 0:
        answer = "-"+answer[:len(answer)-1]
    if -128<int(answer)<127:
        print(int(answer))
    else:
        print("no solution")

if __name__ == "__main__":
    main1()
