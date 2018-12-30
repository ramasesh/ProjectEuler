def reverse(n):
    # returns the reverse of a number
    reversed = 0
    
    while n > 0:
        reversed = reversed * 10 + n % 10
        n /= 10
        
    return reversed