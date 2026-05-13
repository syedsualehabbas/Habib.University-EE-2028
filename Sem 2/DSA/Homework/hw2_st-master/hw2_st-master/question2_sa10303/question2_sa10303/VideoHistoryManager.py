from VideoHistoryHashTable import *

#Takes in list of Dictionaries in format[{},{}] 
# Returns HashTable in the Format [{'ID':..,"DATA":{}}]

def create_VideoHistory(VideoRecords):
    size=17
    hash_table=create_hashtable(size)
    for record in VideoRecords:
        ID=record['Video_ID']
        DATA={'Video_URL': record['Video_URL'],'Views': record['Views'],'Likes': record['Likes'],'Dislikes': record['Dislikes']}
        put(hash_table, ID, DATA, size)
    return hash_table
################################################################################
# def create_VideoHistory(VideoRecords):
#     hash_table=create_hashtable(7)
#     for record in VideoRecords:
#         ID=record['Video_ID']
#         DATA={'Video_URL': record['Video_URL'],'Views': record['Views'],'Likes': record['Likes'],'Dislikes': record['Dislikes']}
#         hash_table[hash_function(record['Video_ID'], 7)]["ID"]=ID
#         hash_table[hash_function(record['Video_ID'], 7)]["DATA"]=DATA
#     return hash_table
############################################################################3###
    
#Takes as input the Hashtable and Name of Operation file 
# Returns a Tuple with two items 
#   1. collision Path in the format {1:[],2:[]} where the keys are the Operation number
#   2. Final HashTable After All Operations performed.




#################################### NOT WORKING IF THE LENGHT OF LINE IS < 5 ######################
# def perform_Operations(H, operationFile):
#     collision_path = {} 
#     with open(operationFile) as file:
#         operation_number = 1
#         for line in file:
#             line = line.strip() 
#             command, data = line.split(maxsplit=1)
#             video_id, url, views, likes, dislikes = data.split(';')
#             if command == "Delete":
#                 delete(H, video_id, len(H), collision_path, operation_number)
#             elif command == "Watch":
#                 values = data.split(';')
#                 if len(values) == 5:  # Ensure we have all required fields
#                     video_id, url, views, likes, dislikes = values
#                     video_data = {'Video_URL': url,'Views': int(views),'Likes': int(likes),'Dislikes': int(dislikes)}
#                     data, index = get(H, video_id, len(H), collision_path, operation_number)
#                     if index is not None:
#                         Update(H, video_id, "Views", len(H), collision_path, operation_number)
#                     else:
#                         put(H, video_id, video_data, len(H))
#             elif command == "Like":
#                 Update(H, video_id, "Likes", len(H), collision_path, operation_number)
#             elif command == "Dislike":
#                 Update(H, video_id, "Dislikes", len(H), collision_path, operation_number)
#             operation_number += 1
#     return collision_path, H
###############################################################################################################################
def perform_Operations(H, operationFile):
    collision_path = {} 
    with open(operationFile) as file:
        operation_number = 1
        for line in file:
            line = line.strip() 
            parts=line.split(maxsplit=1)
            command, data = parts
            values=data.split(";")
            video_id=values[0]
            if command == "Delete":
                H = delete(H, video_id, len(H), collision_path, operation_number)
            elif command == "Watch":
                values = data.split(';')
                if len(values) == 5: 
                    video_data = {'Video_URL': values[1],'Views':int(values[2])+1,'Likes': int(values[3]),'Dislikes':int(values[4])}
                    data, index = get(H, video_id, len(H), collision_path, operation_number)
                    if index is not None:
                        Update(H, video_id, "Views", len(H), collision_path, operation_number)
                    else:
                        put(H, video_id, video_data, len(H))
            elif command == "Like":
                Update(H, video_id, "Likes", len(H), collision_path, operation_number)
            elif command == "Dislike":
                Update(H, video_id, "Dislikes", len(H), collision_path, operation_number)
            operation_number += 1
    return collision_path, H            

            
#Takes the File name is input 
# Returns the list of Dictionaries to be converted to a hashtable in format [{},{}...]
def main(filename):
    with open(filename) as f:
        lines=[line.strip() for line in f.readlines()]
    headers=lines[0].split(';')
    result=[]
    for line in lines[1:]:
        values=line.split(';')
        values[1]=str(values[1]) 
        values[2]=eval(values[2])  
        values[3]=eval(values[3])
        values[4]=eval(values[4])  
        result.append(dict(zip(headers, values)))
    return result
    

# Driver Code
VideoRecords=main('question2_sa10303/watchedVideos.csv')
# print(VideoRecords)
H=create_VideoHistory(VideoRecords)
# print(H)
print(perform_Operations(H,'question2_sa10303/Operations1.csv'))