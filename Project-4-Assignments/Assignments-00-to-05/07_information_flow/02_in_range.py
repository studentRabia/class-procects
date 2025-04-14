#Problem Statement
#Implement the following function which takes in 3 integers as parameters:
#Implement the following function which takes in 3 integers as parameters:
#





'''

def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return print(low <= n <= high)

if __name__ == '__main__':
    in_range(2,10,1)
    
'''

def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    # we could have also included an else statement, but since we are returning, it's fine without!
    return False

if __name__ == '__main__':
    print(in_range(5, 20, 50))
