import random
import sys
import time

animation = "|/-\\"
for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

stop_at = 100
while True:
    num = random.randint(1, 100)
    if num == stop_at:
        break
    sys.stdout.write(str(num))

while True:
    animation = "|/-\\"
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    