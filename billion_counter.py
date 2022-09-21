import datetime
from threading import Thread 

"""
print("Counter Started at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))

a= 0 
for c1 in range(1000000000):
    a=a+1
    
print(a)

print("Counter ended at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))
"""

print("Counter thread Started at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))

output = {}

def counter1(a,b,t):
    res =0
    for c1 in range(a,b+1):
        res=res+1
   
    output[t]=res
    

# Create a Thread Object using the Thread class of the threading module
t1 = Thread(target=counter1, args=(1,250000000,1,))
t1.start()

# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=counter1, args=(250000001,500000000,2,))
t2.start()

# Create a Thread Object using the Thread class of the threading module
t3 = Thread(target=counter1, args=(500000001,750000000,3,))
t3.start()

# Create one more Thread Object using the Thread class of the threading module
t4 = Thread(target=counter1, args=(750000001,1000000000,4,))
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

result = 0

print(output)

for k,v in output.items():
    result = result+v
    
print(result)


print("Counter thread ended at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))
