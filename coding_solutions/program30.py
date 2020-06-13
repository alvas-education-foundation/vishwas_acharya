#Program to calculate Electricity Bill
unit=int(input("Enter the unit consumed: "))
#//Reads input from user and store in variable unit
def Bill_Calc(unit):#function definition
    
    if(unit<=100):
          #below 100 units
        print(unit*10);
    
    elif(unit<=200):
           #below 200 units
        print((100*10)+(unit-100)*15);
    
    elif((unit<=300)):#below 300 units
        print((100*10)+((200-100)*15)+(unit-200)*20);
    
    else:   #above 300 units
        print((100*10)+((200-100)*15)+((300-200)*20)+(unit-300)*25);
Bill_Calc(unit)#function call
