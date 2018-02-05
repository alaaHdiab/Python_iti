


num=input("enter number:");
for q in range(int(num)):
    for k in range(int(num)-(q+1)):
        print('  ',end='');
    for v in range(q+1):
        print('* ',end='');
    
    print("\n");
    