import threading 
import time

data={} #'data' is the dictionary to store data

# Create operation 
# Timeout is optional you can continue by passing two arguments without timeout

def create(Key,value,timeout=0):
    if Key in data:
        print("error:key already exists") 
    else:
        if(Key.isalpha()):
            if len(data)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(Key)<=32: #input key_name capped at 32chars
                    data[Key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind Key_name, Key_name must contain only alphabets and no special characters or numbers")#error message3

# Read operation

            
def read(Key):
    if Key not in data:
        print("error: Given key does not exist in database. Please enter a valid key") 
    else:
        b=data[Key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the time
                stri=str(Key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",Key,"has expired") 
        else:
            stri=str(Key)+":"+str(b[0])
            return stri


# Modify operation 


def modify(Key,value):
    b=data[Key]
    if b[1]!=0:
        if time.time()<b[1]:
            if Key not in data:
                print("error: Given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                data[Key]=l
        else:
            print("error: time-to-live of",Key,"has expired")
    else:
        if Key not in data:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            data[Key]=l


# Delete operation


def delete(Key):
    if Key not in data:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=data[Key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del data[Key]
                print("Key is successfully deleted")
            else:
                print("error: time-to-live of",Key,"has expired") 
        else:
            del data[Key]
            print("key is successfully deleted")

