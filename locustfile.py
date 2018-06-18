import random
stop_at = 0
while True:
    num = random.randint(1, 1000000)
    if num == stop_at:
        break
    print (num)