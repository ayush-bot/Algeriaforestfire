from concurrent.futures import ThreadPoolExecutor
import time

def print_number(num):
    time.sleep(1)
    return f"number is : {num}"
number=[1,2,3,4,5]


with ThreadPoolExecutor(max_workers=3) as a: #yaha 3 thread use hue hai isliye itna fast hai ye sleep ek sec krne ke baad bhi
    results=a.map(print_number,number)
for i in results:
    print(i)