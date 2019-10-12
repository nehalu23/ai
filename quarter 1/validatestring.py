#-----------------------------------------------------------------------------------------------------
#validation

# while loop is used to keep asking user for correct value until his value satistisfies the condition.
while True:
    #user input
    name = input("enter your name: ")
    
    # isapha check that the variable should only contain alphabets
    check_name = name.isalpha()

    #if Check_name returns true break the loop, else ask user to enter correct value..
    if check_name == True:
        break
    else:
        print("please enter correct name \n")


while True:
    #user input
    num = input("enter your number: ") 
    
    # isdigit check that the variable should only contain numbers
    #check_num = num.isdigit()
    count_num = 0
    num_list = []
    num_list.append(num)
    check_first_num = num_list[0][:1]
    if check_first_num == "0":
        count_num += 2    
    
    for i in num:
        count_num += 1
    


    print(count_num)
    
    #if Check_name returns true break the loop, else ask user to enter correct value..
    if  count_num == 13:
        break
    else:
        print("please enter correct number \n")



#-------x-------x-------x-------x-------x-------x-------x-------x-------x-------x-------x-------x-----
