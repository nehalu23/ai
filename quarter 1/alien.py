a = True
# explaination about the project
print('-----------------------------------------------------')
print('| alidu to english or english to alidu              |')
print('| alidu is a language of planet earth of universe 6 |')
print('-----------------------------------------------------')
#x------x------x------x------x------x------x------x------x------x------x------x------x

# to pause the program until user press enter
proceed = input("\npress enter to continue...")
#x------x------x------x------x------x------x------x------x------x------x------x------x

#dictionary
lang = {"hello":"wewe",}
#main program start
while a == True:
        # asking bout what operation user want to perform
        print('\n----------------------------------------------------------------')
        print('''
        [1] Translate into English
        [2] Translate into Alidu
        [3] Add a new word
        [4] Exit.
        ''')
        print('----------------------------------------------------------------')
        action = input("enter number from 1-3 to perform an operation as labeled above\n----------------------------------------------------------------\n")
        #x------x------x------x------x------x------x------x------x------x------x------x------x

        # validating value that user have entered
        if action == "1" or action == "2" or action == "3":
                print("you have entered ",action)
        # exit if entered 4
        elif action == "4":
                print("\n\nYour program has been terminated...\n\n")
                a = False
                break
        else:
                print(action,"is not a valid value,You can only enter no. from 1 to 3")
        print('----------------------------------------------------------------')
        #x------x------x------x------x------x------x------x------x------x------x------x------x

        #if entered 1, translate to english
        if action == "1":
                con = input("enter an Alidu word: ")
                for x,y in lang.items():
                        if y == con:
                                print("----------------------------------------------------------------\n","|",y,"means ",x,'in Alidu',"|\n","----------------------------------------------------------------\n")
                proceed1 = input("press enter to continue...\n")       
        
        #if entered 2, translate to alidu
        if action == "2":
                con = input("enter an English word: ")
                ans = lang[con]
                print('----------------------------------------------------------------')
                print('|',con,'means',ans,'in english |')
                print('----------------------------------------------------------------')
        proceed2 = input("press enter to continue...\n")

        #if entered 3, add a new word
        if action == "3":
                val1 = input("enter word in English: ")
                val2 = input("enter same word in Alidu: ")
                lang[val1] = val2 
        print('----------------------------------------------------------------')
        print('|',val1,'means',val2,'|')
        print('----------------------------------------------------------------')
        proceed2 = input("press enter to continue...\n")


        