import random
import sys
import time


stop_at = 0
for x in range(8):
    num = random.randint(1, 100)
    time.sleep( 300 )
    print(num)