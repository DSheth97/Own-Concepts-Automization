def countzero(arr):
    count=0
    if(0 in arr):
        count=arr.count(0)
    return count

def skipzeroes(j,k):
    pos=0
    i=j
    if(i>12):
        i=0
    global c
    if(countzero(deck1)!=0):    

        #print("Inside skipzeroes now:")
        #print("Received j and k = ",j,k)
        #print("Entering loop now")
        while(c!=k):
            #print("i,j,deck are ",i,j,deck1)
            if(deck1[i]==0):
                c=c+1
                pos=i
                i=i+1
            else:
                i=i+1
            if(i>12):
                i=0
            
        
        c=0
        return pos
    else:
        print("Final Deck formed = ",deck1)




    

a=1
i=0
k=int(input())
k=k+1
deck2=[1,0,2,0,3,0,4,0,5,0,6,0,7]
deck1=[0,0,0,0,0,0,0,0,0,0,0,0,0]
fin=[1,2,3,4,5,6,7,8,9,10,11,12,13]
'''while(countzero(deck1)!=0):
    if (deck1[i]==0):
        print(deck1," if 0")
        deck1[i]=a
        print(deck1," if 0")
        i+=(c*k)
        a+=1
        print(i,a," i and a are")
    if(i>12):
        i=deck1.index(0)
        i+=(c*k)
        c=2*c
        print("\tc= ",c)
        print(i," in if")
    else:
        print(deck1," braking now")
print(deck1)    '''    
c=0
while(countzero(deck1)!=0):
    print("zeroes left = ",countzero(deck1))
    if (deck1[i]==0):
        deck1[i]=a
        a=a+1
        #print("Deck after insertion",deck1)
        i=skipzeroes(i,k)
        #print("i= ",i," deck = ",deck1," after skipzeroes")
print(deck1)       
        
        
        
        
        
