def space(n,i):
    z=n-i;
    for k in range(z):
        print(' ',end='');


def astr(i):
    
    for k in range(i):
        print('*',end='');



for q in range(4):
    space(4,q+1);
    astr(q+1);
    print("\n");
    
