def main():
    N, M = map(int,input().split()) 
    for i in range(1,N,2): 
        print(("." + "|.."*int((i-1)/2) + "|" + "..|"*int((i-1)/2) + ".").center(M,'-'))
    print("WELCOME".center(M,"-"))
    for i in range(N-2,-1,-2): 
        print(("." + "|.."*int((i-1)/2) + "|" + "..|"*int((i-1)/2) + ".").center(M,'-'))

if __name__=='__main__':
    main()
