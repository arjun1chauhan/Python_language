# Print a CountDown as before launching

import time
count=int(input("Enter the count down number: "))
print("Countdown Starts")
for i in range(count,0,-1):
    print(i)
    time.sleep(2)

print("Happy new Year")