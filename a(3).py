def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
while True:
    
    nterms =int( input("enter the terms: "))

# check if the number of terms is valid
    print("Fibonacci sequence:")
    for i in range(nterms):
           print(fibo(i))
