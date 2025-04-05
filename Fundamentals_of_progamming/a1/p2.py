# Solve the problem from the second set here
#Function to check if a number is prime
def isprime(n):
    ok=1
    if n<2:
        ok=0
    for i in range(2,n//2+1):
        if n%i==0:
            ok=0
    return ok

#Function to look for the twin prime numbers using the isprime function
def twin(n):
    p1=n+1
    p2=n+3
    while isprime(p1)==0 or isprime(p2)==0:
        p1=p1+1;
        p2=p2+1;

    return p1,p2



n=int(input("Please introduce a non-null natural number: "))
print("The twin prime numbers immediately larger than",n,"are",twin(n))
