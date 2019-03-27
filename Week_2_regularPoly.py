
# coding: utf-8

# In[ ]:


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

