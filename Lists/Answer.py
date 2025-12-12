if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(N):
        inp=input().split()
        if inp[0]=="insert":
            L.insert(int(inp[1]),int(inp[2]))
        elif inp[0]=="append":
            L.append(int(inp[1]))
        elif inp[0]=="pop":
            L.pop()
        elif inp[0]=="print":
            print(L)
        elif inp[0]=="remove":
            L.remove(int(inp[1]))
        elif inp[0]=="sort":
            L.sort()
        else:
            L.reverse()
