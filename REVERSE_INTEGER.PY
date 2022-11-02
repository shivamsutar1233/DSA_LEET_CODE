######################################
######## SHIVAM ASHOK SUTAR ##########
######################################

def reverse_integer(x: int) -> int:
    lower = -2**(31)
    upper = 2**(31)-1
    def reverse(n):
        
        if n//10 == 0:
            return str(n%10)
        
        string = reverse(n//10)
        return str(n%10)+string
    
    if x < 0:
        n = int(reverse(abs(x)))
        n = -n
    else:
        n = int(reverse(x))
    if n < lower or n > upper :
        return 0
    return n

if __name__ == "__main__":
    
    ##### Input: x = 123
    ##### Output: 321
    print(reverse_integer(123))
    
    ##### Input: x = -120
    ##### Output: -21
    print(reverse_integer(-120))