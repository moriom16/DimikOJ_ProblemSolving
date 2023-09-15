""" 
ইনপুট         আউটপুট
3             odd
100           even
0             even 
1111          odd  
"""

T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2 == 0:
        print("even")
    else:
        print("odd")
