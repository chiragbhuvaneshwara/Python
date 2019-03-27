
# coding: utf-8

# In[66]:


str1 = 'exterminate!' 
str2 = 'number one - the larch'


str2.replace('one','seven')


# In[67]:


str2.index('e')


# In[68]:


str1.index('e')
str1.upper()
# str1


# In[69]:


str2  = str2.capitalize()
str2.swapcase


# In[70]:


str1.replace('e','*')


# In[71]:


str2.find('!')


# In[72]:


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * iterPower(base, exp-1)

iterPower(16,2)


# In[73]:


## Towers of Hanoi

def printMove(frm, to):
    """
    frm: string
    to: string
    
    prints: one move
    
    returns: None
    """
    
    print("Move from ",frm,"to ",to,"\n" )
    
    
    
def Towers_Hanoi(num,frm,to,spare):
    """
    num: int
    frm: string
    to: string
    spare: string
    
    prints: steps to solve towers of Hanoi
    
    returns: None    
    """
    
    
    num = int(num)
    if num == 1:
        printMove(frm,to)
        
    
    else:
        Towers_Hanoi(num-1, frm, spare, to)
        Towers_Hanoi(1,frm,to,spare)
        Towers_Hanoi(num-1,spare,to,frm)
        


## Calling the function
print(Towers_Hanoi(7,"T1","T2","T3"))


# In[74]:


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test = 1
    gcd = 0
    
    if a<b:
        test = a
    else:
        test = b
    
    while test != 1:
        if a%test==0 and b%test==0:
            gcd = test
            test = 2
    
        test -= 1
    
    if gcd == 0:
        return 1
    else:
        return gcd
        


# In[76]:


#Fibonacci Numbers

def fib(x):
    """
    Assumes x as int, x>0
    
    Returns Fibonacci number
    """
    
    if x==0 or x==1:
        return 1
    
    else:
        return fib(x-1) + fib(x-2)
    
fib(12)
    
    


# In[82]:


#Palindrome

def convert_s(s):
    
    s = s.lower()
    res = ''
    for char in s:
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if char == ch:
                res += char
    
    return res

def is_palindrome(s):
    
    if len(s)<=1:
        return True
    else:
        if s[0] == s[-1] and is_palindrome(s[1:len(s)-1]):
            return True
        
        else:
            return False
        
s = convert_s("Able was I, ere I saw Elba....") 
print(s)
print(is_palindrome(s))


# In[1]:


# We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

# First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

# If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

# As you design the function, think very carefully about what the base cases should be.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    present = False
    
    middle = len(aStr)//2
    last = len(aStr)-1
    
    if len(aStr) == 0 or char<aStr[0] or char>aStr[last]:
        return False
    
    elif aStr[middle] == char: 
        return True

    else:
        if char < aStr[middle]:
            aStr = aStr[0:middle:]
            present = isIn(char, aStr)
            return present

        else:
            aStr = aStr[middle::]
            present = isIn(char, aStr)
            return present
    
    
isIn('',"bbccdddd")
        


# In[6]:


##Week 2 programming assignment

def polysum(n, s):
    """
    n: integer > 0, the number of sides of a regular polygon
    s: float > 0, the legth of each side
    
    returns: area + perimeter^2 rounded to 4 decimal points
    """
    import math
    pi = math.pi 
    
    
    area_n = (0.25 * n * (s**2)) / math.tan(pi/n)
    
    perimeter = n * s
    
    res = area_n + (perimeter**2)
    
    res = round(res,4)
    
    return res

polysum(4,10)

