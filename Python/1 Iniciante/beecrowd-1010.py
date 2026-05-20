# beecrowd | 1010

c1, q1, p1 = input().split()
c2, q2, p2 = input().split()

c1, q1, p1 = int(c1), int(q1), float(p1)
c2, q2, p2 = int(c2), int(q2), float(p2)

total = q1*p1+q2*p2

print(f'VALOR A PAGAR: R$ {total:.2f}')