# beecrowd | 1048

old_sal = float(input())

if old_sal <= 400:
    rajs_per = 15

elif old_sal <= 800:
    rajs_per = 12
    
elif old_sal <= 1200:
    rajs_per = 10

elif old_sal <= 2000:
    rajs_per = 7

else:
    rajs_per = 4

rajs = old_sal * (rajs_per / 100)
new_sal = old_sal + rajs

print(f'Novo salario: {new_sal:.2f}\nReajuste ganho: {rajs:.2f}\nEm percentual: {rajs_per} %')
