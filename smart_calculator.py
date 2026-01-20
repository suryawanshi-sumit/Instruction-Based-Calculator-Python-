responses=["Hello,My name is Machine","What may I help you?","Thank You","Bye-Bye","Sorry,I don't know this","But Next time I will surely do"]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def end():
    print(responses[2])
    print(responses[3])
def extract_num(t1):
    l1=[]
    for w in t1.split( ):
        try:
           l1.append(float(w))
        except:
            pass
    return l1

def sumit():
    print("Sumit is a student of CoDing SeeKho")
    print("He is from Pune")

operations={"ADDITION":add,"SUM":add,"ADD":add,"PLUS":add,"SUB":sub,"SUBTRACT":sub,"MINUS":sub,
            "MULTIPLY":mul,"PRODUCT":mul,"MULTIPLICATION":mul,"DIVISION":div}

commands={"SUMIT":sumit,"BYE":end,"BYE-BYE":end,"EXIT":end}
            
