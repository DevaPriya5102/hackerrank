# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:36:50 2025

@author: mvrao
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from collections import Counter

def basic_stats(n,x):
    
    mean = sum(x)/n
    
    sort_x = sorted(x)
    if n%2==0:
        median = (sort_x[n//2 -1] + sort_x[n//2])/2
    else:
        median = sort_x[n//2]
    
    freq = Counter(x)
    max_f = max(freq.values())
    n_mode = [key for key,values in freq.items() if values == max_f]
    mode = min(n_mode)
    
    var = sum((xn -mean)**2 for xn in x)/n
    std = math.sqrt(var)
    
    error = 1.96 * (std / math.sqrt(n))
    low= mean - error
    high = mean +error
    
    
    print(f"{mean:.1f}")
    print(f"{median:.1f}")
    print(f"{mode:.1f}")
    print(f"{std:.1f}")
    print(f"{low:.1f} {high:.1f}")
    
    
n=int(input())
x=list(map(int,input().split()))

basic_stats(n,x)
