A : str = input()
B : str = input()

a1 : int = int(B[-1]) * int(A)
a2 : int = int(B[-2]) * int(A)
a3 : int = int(B[0])  * int(A)
print(f'{a1}\n{a2}\n{a3}\n{int(A) * int(B)}')

"""
A = int(input())
B = list(input())
B.reverse()
for num in B:
    print(int(num) * A)
B.reverse()
print(A * int(''.join(B)))
"""