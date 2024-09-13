"""
Fatorial 

1 = 1
2 = 2 x 1
3 = 3 x 2 x 1
4 = 4 x 3 x 2 x 1
5 = 5 x 4 x 3 x 2 x 1

"""

def cal_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(fact)

cal_fact(5)
