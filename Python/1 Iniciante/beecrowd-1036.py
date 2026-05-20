# beecrowd | 1036

A, B, C = map(float, input().split())

delta = B ** 2 - 4 * A * C

if delta < 0 or A == 0:
    print('Impossivel calcular')
    
else:
    R1 = (-B + delta ** (1/2)) / (2 * A)
    R2 = (-B - delta ** (1/2)) / (2 * A)
    print(f'{R1 = :.5f}\n{R2 = :.5f}')