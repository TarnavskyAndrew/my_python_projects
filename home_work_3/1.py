
def caching_fibonacci():
    
    cache  = {}
    
    def fibonacci(n):
        if debager == True:
            print(cache)
        if n <= 0:
            return 0
        if n == 1: 
            return 1
        if n in cache:
            return cache[n]         
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            if debager == True:
                print(f"num in cache {cache[n]}")
            return cache[n]
             
    return fibonacci         

debager = False

fib = caching_fibonacci()      
print(fib(10))  # 55
print(fib(15))  # 610



    
    
    
    


