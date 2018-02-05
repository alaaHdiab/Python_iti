def dic(lst):
    
    vv=[];
    res=[];
    dict={}
    for i in lst:
    
    


        if i[0] not in dict:
            dict[i[0]]=[i];
        else:
        
            dict[i[0]].append(i);
    return dict;
    

# lst=[];
# vv=[];
# res=[];
# dict={}
'''
txt=input('enter text:');
lst=(txt.split(' '));
lst.sort();
'''

lst = ["hello", "alaa", "iti"]
'''
for i in lst:
    
    


    if i[0] not in dict:
        dict[i[0]]=[i];
    else:
        
        dict[i[0]].append(i);
        
    
print(dict.items());
'''
