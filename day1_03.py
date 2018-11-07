def checkio(alist):
    li_2 = []
    n = len(alist)
    for i in range(0,n):
        for j in range(0,n):
            if alist[i] == alist[j] and i != j:
                li_2.append(alist[i])
                break
    n2 = len(li_2)
    for i in li_2:
        print(i,end = " ")

if __name__ == "__main__":
    li_1 = [10,9,10,10,9,8]
    checkio(li_1)
