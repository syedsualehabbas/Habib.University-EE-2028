import math
import csv

# INSTRUCTIONS >> DO NOT MODIFY EXISTING CODE USE the FUNCTIONS MENTIONED IN THE FILE 
# YOU CAN CREATE YOUR OWN FUNCTIONS IF NEEDED

#Takes size as Input
#Returns Empty hast table of 'size'
#DO NOT MODIFY THIS CODE
def create_hashtable(size): # returns list of dictionaries
    htable=[{}]*size
    for i in range(size):
        htable[i]={"ID": None,
                   "DATA": None}
    return htable
########################HELPER FUNCTION###############################
def nearest_primenumber(num):
    while True:
        if num > 1:
            flag=True
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    flag = False
                    break
            if flag:
                return num
        num += 1

######################################################################
#Takes Existing hashtable, size and a bool indicating wether to increase or decrease the size
#Returns a Tuple Containing new Hash Table and its New Size (Hashtable,newsize)
def resize_hashtable(hashtable,size,increase):
    if increase:
        new_size = nearest_primenumber(size*2)
    else:
        new_size = max(7, nearest_primenumber(size // 2))
    new_hashtable = create_hashtable(new_size)
    for item in hashtable:
        if item["ID"] not in (None , "#"): 
            new_hash = hash_function(item["ID"], new_size)
            while new_hashtable[new_hash]["ID"] not in (None, "#"):
                new_hash = collision_resolver(item["ID"], new_hash, new_size)
            new_hashtable[new_hash] = {"ID": item["ID"], "DATA": item["DATA"]}
    return (new_hashtable, new_size)

##################################################################################3##
############ THIS CODE WAS MAKING A COPY AND THEN INCREASING THE SIZE OF THAT COPY 
##############WHICH WILL NOT ALLOW THE WORKING OF HASH FUNCTION TO BE IMPLEMENTED#########
    # new_hashtable=hashtable.copy()
    # if increase:
        # new_size = nearest_primenumber(size*2)
    # else:
        # a=size//2
        # a=nearest_primenumber(a) 
        # b=size-a
        # count=0
        # if size-b>=7:
        #     for i in new_hashtable:
        #         for j in i:
        #             if i[j]==None and count<=b:
        #                 count+=1
        #                 new_hashtable.pop(new_hashtable.index(i))
########################################################################################
        
    return (new_hashtable, len(new_hashtable))

    

#Takes Key and size as parameters
#Returns Original address of type(int) for the Key using the Hash Function Mentioned in the Document
def hash_function(key, size):
    a=sum(ord(i) for i in key)
    a=a//16   #16 because we have to move four bits right that means dividing by 2^n so 2^4=16
    hash_value=a%size
    return hash_value


##Takes Key , OldAddress  and size as parameters
#Returns new address of type(int) for the Key using the Key Offset method Mentioned in the Document
def collision_resolver(key,oldAddress,size):
    a=sum(ord(i) for i in key)
    offset=a//size
    return (offset+oldAddress)%size

#Takes hashtable, key, data and size and Insert key and Data into the Hash Table 
# After Insertion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable and its Size as a Tuple (hashtable,size)

def put(hashtable,key, data, size):
    hash_value=hash_function(key, size)
    while True:
        if hashtable[hash_value]["ID"] is None:
            break
        hash_value=collision_resolver(key, hash_value, size)
    hashtable[hash_value]["ID"]=key
    hashtable[hash_value]["DATA"]=data
    if loadFactor(hashtable, size)>75:
        hashtable, size=resize_hashtable(hashtable, size, True)
    return (hashtable, size)



#############################################INFINITE LOOP RUNNING#########################
# def put(hashtable,key, data,size):
#     # if loadFactor(hashtable, size)>75:
#     #     hashtable, size=resize_hashtable(hashtable, size, True)
#     # elif loadFactor(hashtable, size)<30 and size>7:
#     #     hashtable, size=resize_hashtable(hashtable, size, False)
#     hash_value=hash_function(key, size)
#     while hashtable[hash_value]["ID"]!=None and hashtable[hash_value]["ID"]!="#":
#         print("hello")
#         hash_value = collision_resolver(key, hash_value, size)
#     hashtable[hash_value]["ID"]= key
#     hashtable[hash_value]["DATA"]=data
#     if loadFactor(hashtable, size)>75:
#         hashtable, size=resize_hashtable(hashtable, size, True)
#     elif loadFactor(hashtable, size)<30 and size>7:
#         hashtable, size=resize_hashtable(hashtable, size, False)
#     return (hashtable, size)
##########################################################################################



#Takes hashtable and size as parameters 
# Returns load factor of type float   
def loadFactor(hashtable,size):
    count=0
    for i in hashtable:
        if i["ID"]!=None and i["ID"]!="#":
            count+=1
    return ((count*100)//size)

#Takes in hash table, key, Name of the Column to be updated, 
# size of hash table, Collision Path and Operation Number as Parameters
#Searches for the key in hashtable and update the Column Name of the hashtable also updates the collision path of the key
#Returns Nothing
def Update(hashtable, key, columnName, size, collision_path, opNumber):
    data, index = get(hashtable, key, size, collision_path, opNumber)  # Unpack tuple
    if index is not None:  
        UpdateAtIndex(hashtable, index, columnName)
# Update the Column Name of the hashtable founf at Index
#Returns Nothing
def UpdateAtIndex(hashtable,index,columnName):
    hashtable[index]["DATA"][columnName]+=1
   
#Takes hash table, key, size , Collision path and Operation Number as parameters
# Searches for the key in Hash table update the Collision path and 
#If key is found returns a Tuple Containing 'DATA' part of the Hash table and the index of the key  
# Return format -> (hashtable[index]['DATA],index)  
#If key is not Found return (None,None)
def get(hashtable, key, size, collision_path, opNumber):
    index=hash_function(key, size)
    check=index  
    path=[]   
    while True:
        if hashtable[index]["ID"]==key:
            path.append(index)
            collision_path[opNumber]=path.copy()
            return (hashtable[index]["DATA"], index)
        elif hashtable[index]["ID"] is None:
            path.append(index)
            collision_path[opNumber]=path.copy()
            print("Item not found")
            break
        else:
            path.append(index)
            index=collision_resolver(key, index, size) 
            if index==check:
                collision_path[opNumber]=path.copy()
                print("Item not found")
                break    
    collision_path[opNumber] = path
    return (None, None) 

#Takes hashtable, key, size , Collision path and operation Number 
# Delete key and Data from the Hash Table 
# After deletion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable 
def delete(hashtable, key, size, collision_path, opNumber):
    index=get(hashtable, key, size, collision_path, opNumber)[1]
    if index is None:
        return hashtable
    hashtable[index]["ID"] = "#"
    hashtable[index]["DATA"] = "#"
    if loadFactor(hashtable, size)<30 and size>7:
        hashtable, size=resize_hashtable(hashtable, size, False)
    return hashtable



# def main():
#     video_records = []
#     with open('watchedVideos.csv', 'r') as file:
#         reader = csv.reader(file, delimiter=';')
#         next(reader)
#         for i in reader:
#             video_records.append({'Video_ID': i[0],'Video_URL': i[1],'Views': int(i[2]),'Likes': int(i[3]),'Dislikes': int(i[4])})
#     return create_VideoHistory(video_records)

# def create_VideoHistory(video_records):
#     hash_table=create_hashtable(7)
#     for record in video_records:
#         ID=record['Video_ID']
#         DATA={'Video_URL': record['Video_URL'],'Views': record['Views'],'Likes': record['Likes'],'Dislikes': record['Dislikes']}
#         hash_table[hash_function(record['Video_ID'], 7)]["ID"]=ID
#         hash_table[hash_function(record['Video_ID'], 7)]["DATA"]=DATA

    






# if __name__ == '__main__':
#     main()
