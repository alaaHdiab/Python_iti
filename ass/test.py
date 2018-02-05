lst=[];
lst2=[];
'''
def inner(i):
    
    for k in range(i,(i*i)+1,i):
            
            #print(k,end='');
            #lst.append(k);
            #return lst;
            #lst.append(k);
            lst.append(k);       
'''

def ff(n):
    
    for i in range(1,n+1):
        
        
        #print(i);
        #inner(i);
        lst=[];
        for k in range(i,(i*i)+1,i):
            lst.append(k);
        lst2.append(lst);    
    return lst2

    # num=input("enter number:");
    # ff(int(num));
    # print(lst2)

