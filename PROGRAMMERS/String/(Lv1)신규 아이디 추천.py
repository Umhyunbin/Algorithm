import re

def solution(new_id):
    new_id = new_id.lower()
    
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    if new_id[0] == '.' or new_id[-1] == '.':
        new_id = new_id.strip('.')
    
    if len(new_id) == 0:
            new_id += 'a'
            
    if len(new_id) > 15:
        new_id = new_id[:15]
        
    if new_id[-1] == '.':
        new_id = new_id.rstrip('.')
        
    while len(new_id) < 3:
        new_id += new_id[-1]
            
    return new_id
