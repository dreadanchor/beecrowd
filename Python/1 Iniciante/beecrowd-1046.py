# beecrowd | 1046

start, end = map(int, input().split())

time = end - start if start < end else 24 - (start - end)

print(f'O JOGO DUROU {time} HORA(S)')
