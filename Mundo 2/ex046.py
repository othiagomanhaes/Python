from time import sleep

print('Os fogos irão estourar em...')
n = 10
for n in range(n, 0, -1):
    sleep(1)
    print(n)
sleep(1)
print('CABOOOM!!')