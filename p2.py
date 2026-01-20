import sys
sys.path.append(r"C:\Users\Sumit Suryawanshi\Combo-3\Python\Project")
from smart_calculator import *
print(responses[0])
print(responses[1])
while True:
    t1=input("Please Ask:")
    for w in t1.split():
        if w.upper() in operations.keys():
            try:
                l1=extract_num(t1)
                r=operations[w.upper()](l1[0],l1[1])
                print(r)
                break
            except:
                print("Please Ask Correct Question")
                break
        elif w.upper() in commands.keys():
            commands[w.upper()]()
            break
    else:
        print(responses[4])
        print(responses[5])
