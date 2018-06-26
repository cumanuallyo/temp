import random
import sys
import time

for x in range(8):
    num = random.randint(1, 100)
    sys.stdout.write(str(num)+'\n')
    time.sleep( 300 )