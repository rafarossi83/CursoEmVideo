from time import sleep
from emoji import emojize

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize(':fogos_de_artifício:' * 5, language='pt'))