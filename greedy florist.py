import os
import sys

#
# Complete the restaurant function below.
#
def restaurant(l, b):
    #
    # Write your code here.
    a=l*b
    t=[]
    for i in range(1,(a//2)):
        if (a%i==0)and (i<=b or i<=l):
            t.append(i)
    t.sort(reverse=True)
    for i in t:
        for j in t:
            if(i==j):
                if(a%i)==0 and i*i<=a:
                    return(a//(i*i))
l=6
b=9
print(restaurant(l, b))
