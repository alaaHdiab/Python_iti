def calc(str,num1,num2=1):
    #shape_inpt(str)
    if str=='t':
        '''
        num1=input('base:');
        num2=input('height:');
        '''
        return .5*int(num1)*int(num2);
    if str=='c':
        #num1=input('redius:');
        return 3.14*int(num1)*int(num1);
    if str=='s':
        #num1=input('n:');
        return int(num1)*int(num1);
    if str=='r':
        #num1=input('width:');
        #num2=input('height:');
        return int(num1)*int(num2);

'''
str=input('enter shape:');
if str=='t':
    num1=int(input('base:'));
    num2=int(input('height:'));
if str=='c':
    num1=int(input('redius:'));
    num2=1
        
if str=='s':
    num1=int(input('n:'));
    num2=1
        
if str=='r':
    num1=int(input('width:'));
    num2=int(input('height:'));
        

#shape_inpt(str)    


print(calc(str,num1,num2));
'''