vec1 = [1,2]
vec2 = [3,4]

position = [1,1]

def move(start_Point, vecTOR):
    end_Point = []
    for i in range(len(start_Point)):
        end_Point += [start_Point[i] + vecTOR[i]]
    return end_Point

def vector_len(new_move, position):
    vector_len = 0
    for i in range(len(new_move)):
        costruct = position[i] - new_move[i]
    for j in range(len(new_move)):
        vector_len = costruct[j] ** 2
    vector_len = vector_len ** 0.5
        
        
            
        
        
    
new_move = move(position, vec1)
last_move = move(new_move, vec2)

