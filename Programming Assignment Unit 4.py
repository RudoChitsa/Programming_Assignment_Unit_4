def is_divisible(r, c):     
    return r % c == 0 
def is_power(r, c):     
        if r == c:         
            return True     
        if c ==  1:         
            return False     
        if not is_divisible(r, c):         
            return False     
        return is_power(int(r/c), c)                              
        print("is_power(10, 2) returns: ", is_power(10, 2)) 
        print("is_power(27, 3) returns: ", is_power(27, 3)) 
        print("is_power(1, 1) returns: ", is_power(1, 1)) 
        print("is_power(10, 1) returns: ", is_power(10, 1)) 
        print("is_power(3, 3) returns: ", is_power(3, 3))


