#!/usr/bin/env python
# coding: utf-8

# In[6]:


test   =[[0, 3, 8, 0, 0, 1, 4, 0, 9],
         [0, 9, 0, 0, 0, 0, 5, 8, 0],
         [2, 0, 0, 7, 9, 0, 0, 0, 0],
         [0, 1, 0, 2, 0, 0, 0, 6, 7],
         [4, 6, 0, 0, 0, 7, 0, 5, 3],
         [5, 8, 0, 6, 3, 9, 0, 2, 0],
         [0, 0, 0, 0, 8, 5, 0, 0, 6],
         [0, 7, 6, 0, 0, 0, 0, 1, 0],
         [1, 0, 9, 3, 0, 0, 2, 4, 0]]


# In[2]:


#defining funciton to find blank spaces

#iterating to each postion to find 0
def find_blank(brd):
    for i in range(len(brd)):
        for j in range (len(brd)):
            if brd[i][j] == 0:
                return i,j #row,col
    else:
        return False


# In[3]:


#defing function to check if number fits at that postion
def check(brd,pos,num):
    for i in range(0,9):
        
        #for checking in rows
        if brd[pos[0]][i] == num and pos[0] != i:
            return False
        
        #for checking in columns
        if brd[i][pos[1]] == num and pos[1] != i:
            return False
    
        #for checking in box
        x = pos[0]//3
        y = pos[1]//3
        
        for i in range(x*3,(x*3)+3):
            for j in range(y*3,(y*3)+3):
                if brd[i][j] == num and (i,j) != pos:
                    return False
    return True

        


# In[4]:


## function to solve the sudoku
def solve(brd):
    
    blank = find_blank(brd)
    
    if blank == False:
        return True
    else:
        row,col = blank
        
    for i in range(1,10):
        if check(brd,(row,col),i) == True:
            brd[row][col] = i
            
            if solve(brd) == True:
                return True
                
            brd[row][col] = 0
        
    return False


# In[7]:


solve(test)


# In[8]:


test


# In[ ]:




