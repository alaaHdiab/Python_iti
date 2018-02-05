def str_index(txt,tst):
    lst=[];
    strt=-1;
    for k in txt:
        #lst=[];
        strt+=1;
    
        if k == tst:
        
            rr=txt.index(k,strt)
        
            lst.append(rr);
    return lst;


    #lst=[];



# txt=input('enter full text:');
# tst=input("enter a letter:");


# str_index(txt,tst)
# for k in txt:
#     strt+=1;
    
#     if k == tst:
        
#         rr=txt.index(k,strt)
        
#         lst.append(rr);




#print(lst);