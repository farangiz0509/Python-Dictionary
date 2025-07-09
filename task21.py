

def count_names(names: list[str]) -> dict[str, int]:
    counter = {}  
    for name in names:
        counter[name] = names.count(name)
        
        return counter
    
    
Name_list = ['ali' , 'vali', 'sami' , 'ali' , 'vali', 'sami']   
result = count_names(Name_list)    

print(result) 
        
    

