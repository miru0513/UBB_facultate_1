#Solve the problem from the first set here
def number(m):
    x=0
    l=[0,0,0,0,0,0,0,0,0,0]
    #we add every appearance of the digits
    while m>0:
        l[m%10]=l[m%10]+1
        m=m//10
    #if 0 appears,then we look for the next number that appears (at least once) and we keep it in a variable
    if l[0]>0:
        for i in range(1,len(l)):
            if l[i]>0:
               x=i
               l[i]=l[i]-1
               break
    #and now we build the number using the frequency array
    for i in range (0,len(l)):
        while l[i]>0:
            x=x*10
            x=x+i
            l[i]=l[i]-1
    return x

m=int(input("Please introduce a natural number "))
print("The smallest number formed with the same digits is",number(m))
      
