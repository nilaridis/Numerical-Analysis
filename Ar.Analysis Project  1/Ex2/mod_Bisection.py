import math
import time 
import random 

MAX_REPS = 20
tol = 1e-5/2

def func(x):
    return 54*(x**6) + 45*(x**5) -102*(x**4) -69*(x**3) +35*(x**2) +16*x-4

def mod_Bisection(x,y,lim):
    i = 0 
    while y-x >= lim and i != MAX_REPS:
        i+= 1
        randomNumber = random.uniform(x,y)
        
        if (abs(func(randomNumber)) >= lim):
            if(func(randomNumber)*func(x))<0 :
                y = randomNumber 
            else:
                x = randomNumber 
        else:
            break 

    return randomNumber,i

def printFunction(a,b,tol):
    print("----------------------------")
    start = time.perf_counter()
    newValue, times = mod_Bisection(a,b,tol)
    end = time.perf_counter()
    totalTime = end - start 
    print(f"Η ριζα ειναι {newValue:.5f} και βρεθηκε μετα απο {times} επαναληψεις")
    print(f"Συνολικος Χρονος : {totalTime:.5f}.")



printFunction(-2.0,-1.0,tol)
# printFunction(-0.7,-0.66,tol)
printFunction(0.0,0.4,tol)
printFunction(0.4,1.0,tol)
printFunction(1.0,2.0,tol)






