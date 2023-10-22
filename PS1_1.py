# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:34:33 2023

@author: 401
"""
#%% Print_values function definition
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print("a,b,c:",a,b,c)
        else:
            if a>c:
                print("a,c,b:",a,c,b)
            else:
                print("c,a,b:",c,a,b)
    elif b>c:
             if a>c:
                 print("a,c,b:",a,c,b)
             else:
                 print("c,a,b:",c,a,b)
    else:
        print("c,b,a:",c,b,a)
#%% Print values experiment
#1 a=11 b=2 c=13
Print_values(11,2,13) 
#2 a=2 b=4 c=7
Print_values(2,4,7) 
#3 a=8 b=1 c=5
Print_values(8,1,5) 
#4 a=15 b=13 c=7
Print_values(15,13,7) 
#5 a=3 b=12 c=6
Print_values(3,12,6) 
#6 a=2 b=8 c=1
Print_values(2,8,1) 

