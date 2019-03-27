
# coding: utf-8

# In[31]:


cube = 126
guess = 0
num_guesses = 0
epsilon = 0.1
step = 0.0001


# condition = (abs(guess ** 3) - cube <= epsilon) and (guess <= cube)

while (abs(guess ** 3) - cube <= epsilon) and (guess**3 <= cube):
           
    num_guesses += 1
    guess += step
    
print("Number of guesses: ", num_guesses)
    
if (abs(guess ** 3) - cube <= epsilon):
    print(guess, "is close to cuberoot of",cube,"with an approximation of",step)
else:
    print("Could not find the cube root.")
   
        


# In[32]:


print(guess**3)

