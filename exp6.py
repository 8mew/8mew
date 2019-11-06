slots = []
delay = []

ts1 = 0
ts2 = 417

total = 12

print("Enter Delay in Each Time Slot")

for i in range(total):
    msg = "Delay at " + str(i+1) + ": "
    d = int( input(msg) )
    delay.append(d)

print("If user is assigned Time Slot using Delay")

for i in range(total):
    
    if delay[i] <= 10:
        slots.append(1)
    else:
        slots.append(0)
    
print()
print("Cycle 1")
print()

for i in range(total):
    
    if slots[i] == 1:
        
        print("User", str(i+1), " is assigned a timeslot ", ts1 , "-", ts2)
        ts1 = ts2 + 1
        ts2 = ts1 + 417
        
    else:
        print("User", str(i+1), " is not assigned a timeslot ")

    
ts1 = 0
ts2 = 417

print()
print("Cycle 2")
print()

for i in range(total):
    
    if slots[i] == 1:
        
        print("Timeslot ", ts1 , "-", ts2, "is idle")
        
    else:
        print("User", str(i+1), " is assigned a timeslot " , ts1 , "-", ts2)
    
    ts1 = ts2 + 1
    ts2 = ts1 + 417
    
"""

Enter Delay in Each Time Slot
Delay at 1: 5
Delay at 2: 12
Delay at 3: 13
Delay at 4: 2
Delay at 5: 9
Delay at 6: 10
Enter If user is assigned Time Slot

Cycle 1

User 1  is assigned a timeslot  0 - 417
User 2  is not assigned a timeslot 
User 3  is not assigned a timeslot 
User 4  is assigned a timeslot  418 - 1252
User 5  is assigned a timeslot  1671 - 3340
User 6  is not assigned a timeslot 

Cycle 2

Timeslot  0 - 417 is idle
User 2  is assigned a timeslot  418 - 1252
User 3  is assigned a timeslot  1671 - 3340
Timeslot  5012 - 8769 is idle
Timeslot  13782 - 22968 is idle
User 6  is assigned a timeslot  36751 - 60136

"""
