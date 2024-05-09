#!/bin/python3

import math
import os
import random
import re
import sys
import array
#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    decallage = abs(min(arr))
    freq = [0]*(max(arr)+1+decallage)


    for i in arr :
        freq[i+decallage]+=1
       
    sorted_arr = [0]*(len(arr))
    
    indice=0
    j=0
    for num in freq:
        for k in range(0,num):
            sorted_arr[j]=indice-decallage
            j+=1
        indice+=1 
        
    return sorted_arr
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
