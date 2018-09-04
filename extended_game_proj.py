'''Name: Subhasish Sarkar
   Game Type: Advanced game
 '''
#
 #this is the dictionary that shall be used as a lookup table in the main battle algorithm
 #notice the structure of the dictionary, where the Keys are tuples and values are strings
 #notice also that the tuple[0]==key only when tuple[0] has the stronger element. As you will see tuple[0] always has the unit of User A
 #and tuple[1] always has the unit of User B. So essentially this dictionary gives out the outcome of every battle when either User A is winning or
 #user B is winning
battle_dict = {('Archer','Soldier'):'Archer',
                ('Archer','Knight'):'Knight',
                ('Soldier','Knight'):'Soldier',
                ('Soldier','Archer'):'Archer',
                ('Knight','Archer'):'Knight',
                ('Knight','Soldier'):'Soldier'}

#This is taking input of user A's name as a string
usr_A = input('\nEnter your Name Commander #1! ')

#these are taking the 3 units, and a count variable for each unit, so as to later increment the count variable and get the number of units
#of each type that a user has taken
unit_a = "Soldier"
a_count = 0
unit_b = "Knight"
b_count = 0
unit_c = "Archer"
c_count = 0

#this is the list where user A's army will be stored
units_list_a = []

#these are flags that are used to break the while loop while taking inputs from the user
#exit_flag_a and loop_breaker_b are for the while loop for user A
#exit_flag_b and loop_breaker_b are for the while loop for user B
#essentially when exit_flag_a is set to 1 or when loop_breaker_b is set to True within the while loop, the while loop breaks
#this is put in to ensure that the user can stop making his army or can quit the game at any point in time while he is still making his army
exit_flag_a = 0
loop_breaker_a = False
exit_flag_b = 0
loop_breaker_b = False

#money given to the user to spend on making his army
money = 10
print('\nYou are given $'+str(money)+' to buy units\n')

#this is the loop that runs while input is being taken from user A
#user A is shown this menu till he runs out of money, and the money variable becomes 0
#or if user A chooses to quit making his army in which case loop_breaker_a is set to True and the while loop breaks
#or if user A decides to quit the game in which case exit_flag_a becomes 1 and the while loop breaks
while exit_flag_a == 0 and loop_breaker_a == False and money > 0:
        purchase = input(''' Which unit do you want to purchase?
                1. Soldier
                2. Knight
                3. Archer

                Please enter:
                "1" for Soldier,
                "2" for Knight,
                "3" for Archer,
                "4" to Stop Making Army, or
                "5" to Exit the Game
                Enter your choice here: ''')


        #the following if-else statements show the unit user A will purchase for every number that he inputs
        #if user A chooses to quit making his army, he can choose option 4
        #if user A wants to quit the game, he can choose option 5
        if purchase == "5":
                    exit_flag_a = 1
                    break

        elif purchase == '1':
                    money = money - 1
                    a_count += 1
                    #since units_list_a is a list, whenever user A chooses a unit, it gets added to the list to make his army
                    units_list_a.append(unit_a)
                    print ('\nYou have recruited a soldier. You now have'+' $'+str(money)+' left')
                    print(units_list_a)

        elif purchase == '2':
                    money = money - 1
                    b_count += 1
                    units_list_a.append(unit_b)
                    print ('\nYou have recruited a Knight. You have'+' $'+str(money)+' left')
                    print(units_list_a)

        elif purchase == '3':
                    money = money - 1
                    c_count += 1
                    units_list_a.append(unit_c)
                    print ('\nYou have recruited an Archer. You have'+' $'+str(money)+' left')
                    print(units_list_a)

        elif purchase == "4":
                loop_breaker_a = True
                break

        #if user A enters any other text into the input prompt other than the numbers in the menu, this error message will be shown
        #the loop shall continue until he enters a valid input, i.e., a number between 1-5
        else:
                print("\nPlease enter a valid input.\n")
                continue

#Once the while loop breaks and exit_flag_a from the loop is set to 1 by the user picking option 5, to exit the game
#this message is shown and the code stops here,essentially stopping the Game because the rest of the code is inside the else statement
if exit_flag_a == 1:
    print ("\nCommander",usr_A,"has quit the game.\n")

else:
    #if the user decides not to quit the game then the rest of the program executes
    #this block of code basically asks the user if he wants to purchase medical supplies for his medic
    #medic_supp_qs is a variable that stores the answer of the user
    #med_supp_a and med_supp_b are the amount of medical supplies that user A and user B buy respectively
    #the user can only purchase medical supplies if the money variable is > 0
    #the user can purchase medical supplies within their budget of money that is left over after they have purchased their army
    #If the user tries to purchase more supplies than he has money for, an error message is shown
    #if the user types a wrong input when the question of buying medical supplies is prompted, the default is set to give the user 0 supplies
    #if the user chooses not to buy any medical supplies then med_supp variable is set to 0 and the user does not get any medical supplies
    medic_supp_qs = input('\nDo you want to purchase supplies for your medic? (Y/N): ')
    if medic_supp_qs == 'Y' or medic_supp_qs == 'y' or medic_supp_qs == 'yes' or medic_supp_qs == 'Yes' or medic_supp_qs == "YES":
        med_supp_a = int(input("\nEnter the number of supplies you want to purchase: "))
        while med_supp_a > money:
            print("\nYou do not have sufficient funds. Please buy supplies worth less than or equal to $"+str(money))
            med_supp_a = int(input("Enter the number of supplies you want to purchase: "))
            continue
        print('\nYou have purchased',med_supp_a,'supplies for your medic.')

    elif medic_supp_qs == 'N' or medic_supp_qs == 'n' or medic_supp_qs == 'no' or medic_supp_qs == 'No' or medic_supp_qs == "NO":
        print('\nYou have not purchased any medic supplies.\n')
        med_supp_a = 0

    else:
        print("\nYou have not entered a valid answer. As punishment, No medics have been given to you.")
        med_supp_a = 0

    print("\n",usr_A,'The units you have purchased are:',a_count,' Soldiers,',b_count,'Knights,',c_count,'Archers, and',med_supp_a,'Medicinal Supplies\n')
    print(usr_A,"Your army is",units_list_a)
    print('\nCommander',usr_A,'Your army has been assembled!\n')

    #After this prompt is displayed to user A, User B is then asked for his inputs. The logic is the same

    usr_B = input ('\nEnter your name Commander #2! ')

    units_list_b = []

    money = 10
    a_count = 0
    b_count = 0
    c_count = 0

    print('You are given $'+str(money)+' to buy units\n')
    while exit_flag_b == 0 and loop_breaker_b == False and money > 0:
            purchase = input(''' Which unit do you want to purchase?
                            1. Soldier
                            2. Knight
                            3. Archer

                            Please enter:
                            "1" for Soldier,
                            "2" for Knight,
                            "3" for Archer,
                            "4" to Stop Making Army, or
                            "5" to Exit the Game
                            Enter your choice here: \n''')
            if purchase == '5':
                exit_flag_b = 1
                break

            elif purchase == '1':
                money = money - 1
                a_count += 1
                units_list_b.append(unit_a)
                print ('\nYou have recruited a soldier. You now have'+' $'+str(money)+' left')
                print(units_list_b)

            elif purchase == '2':
                money = money - 1
                b_count += 1
                units_list_b.append(unit_b)
                print ('\nYou have recruited a Knight. You have'+' $'+str(money)+' left')
                print(units_list_b)

            elif purchase == '3':
                money = money - 1
                c_count += 1
                units_list_b.append(unit_c)
                print ('\nYou have recruited an Archer. You have'+' $'+str(money)+' left')
                print(units_list_b)

            elif purchase == "4":
                loop_breaker_b == True
                break

            else:
                print("\nPlease enter a valid input.")
                continue

    if exit_flag_b == 1:
        print("\nCommander",usr_B,'has quit the game.')

    else:
        #if the user decides not to quit the game then the rest of the program executes
        #this block of code basically asks the user if he wants to purchase medical supplies for his medic
        #medic_supp_qs is a variable that stores the answer of the user
        #med_supp_a and med_supp_b are the amount of medical supplies that user A and user B buy respectively
        #the user can only purchase medical supplies if the money variable is > 0
        #the user can purchase medical supplies within their budget of money that is left over after they have purchased their army
        #If the user tries to purchase more supplies than he has money for, an error message is shown
        #if the user types a wrong input when the question of buying medical supplies is prompted, the default is set to give the user 0 supplies
        #if the user chooses not to buy any medical supplies then med_supp variable is set to 0 and the user does not get any medical supplies
        medic_supp_qs = input('\nDo you want to purchase supplies for your medic? (Y/N): ')
        if medic_supp_qs == 'Y' or medic_supp_qs == 'y' or medic_supp_qs == 'yes' or medic_supp_qs == 'Yes' or medic_supp_qs == "YES":
            med_supp_b = int(input("\nEnter the number of supplies you want to purchase: "))
            while med_supp_b > money:
                print("\nYou do not have sufficient funds. Please buy supplies worth less than or equal to $"+str(money))
                med_supp_b = int(input("Enter the number of supplies you want to purchase: "))
                continue
            print('\nYou have purchased',med_supp_b,'supplies for your medic.')

        elif medic_supp_qs == 'N' or medic_supp_qs == 'n' or medic_supp_qs == 'no' or medic_supp_qs == 'No' or medic_supp_qs == "NO":
            print('\nYou have not purchased any medic supplies.\n')
            med_supp_b = 0

        else:
            print("\nYou have not entered a valid answer. As punishment, No medics have been given to you.")
            med_supp_b = 0

        print("\n",usr_B,'The units you have purchased are:',a_count,' Soldiers,',b_count,'Knights,',c_count,'Archers, and',med_supp_b,'Medicinal Supplies\n')
        print(usr_B,"Your army is",units_list_b)
        print('\nCommander',usr_B,'Your army has been assembled!\n')

        #after user B has taken his inputs, the battle begins
        #the battle algorithm first checks for the condition of a tie, wherein the list element at the top of both users' lists will be the same
        #If that is not the case then the battle algorithm executes further

        print("\nTHE BATTLE BEGINS!!\n")

        #flag_a and flag_b are flag boolean variables which are set to False at the start and will toggle to True whenever either user wins
        #if user A wins, flag_a is set to True
        #if user b wins, flag_b is set to True
        #if the round ends in a tie, both flags remain at False
        #rnd is a variable that represents the round of the battle. it gets incremented after the end of every round
        flag_a = False
        flag_b = False
        rnd = 1

        #this block of code is executed in the special case where either user A or user B or both have not selected any units
        #if user A hasnt selected any units, then the length of his list will be 0, thus user B will win automatically
        #if user B hasnt selected any units, then the lenght of his list will be 0, thus user A will win automatically
        #if both users havent selected units, then the lenght of both their lists will be 0, and the battle gets cancelled
        if len(units_list_a) == 0 and len(units_list_b) == 0:
            print('\nBoth Commanders have not selected armies. BATTLE IS CANCELLED!!!!')

        elif len(units_list_b) == 0:
            print('\nCommander',usr_B,'LOSES by default for not selecting any units!!!')

        elif len(units_list_a) == 0:
            print('\nCommander',usr_A,'LOSES by default for not selecting any units!!!')

        #after making the check that both users have taken units, the battle algorithm starts
        else:
            #this loop iterates over units_list_a and basically acts as a way for the battle to progress from round to round
            #since there is a while loop inside which ensures that the algorithm doesnt throw an error due to list index being out of range, it
            #doesnt matter if the for loop iterates over units_list_a or units_list_b
            for loop_iter in units_list_a:
                while (len(units_list_a)>0 and len(units_list_b)>0):
                    #this is where the check for the tie happens
                    #when two units of the same type fight each other, they both kill each other, thus the top elements from both lists are popped
                    #popped elements are stored inside a variable called loser
                    #this is then used by the medics to append that unit to the end of the list
                    #rnd is then incremented to indicate the end of a round
                    if units_list_a[0] == units_list_b[0]:
                            print('\nRound',rnd,'ends in a draw!')
                            loser = units_list_a.pop(0)
                            #this check is made to ensure that units are revived and appended to the back to the list only
                            #if the user has any medical supplies left
                            #if the user has run out of medical supplies, the unit simply dies (gets popped from the list and doesnt get appended)
                            #this check is done everytime a unit dies
                            if med_supp_a > 0:
                                units_list_a.append(loser)
                                print("\nMedic saves Commander", usr_A,"'s unit!!!")
                                med_supp_a = med_supp_a - 1
                                print("Medicinal Supplies Left: $" + str(med_supp_a) + "\n")
                            elif med_supp_a == 0:
                                print("\n",usr_A,"has no more medicinal supplies left. Unit dies!")
                            loser = units_list_b.pop(0)

                            if med_supp_b > 0:
                                units_list_b.append(loser)
                                print("\nMedic saves Commander", usr_B, "'s unit who joins at the back of the army!!!")
                                med_supp_b = med_supp_b - 1
                                print("Medicinal Supplies Left: $" + str(med_supp_b) + "\n")
                            elif med_supp_b == 0:
                                print("\n",usr_B,"has no more medicinal supplies left. Unit dies!")
                            flag_a = False
                            flag_b = False
                            rnd += 1

                    #if the battle does not end in a tie, this else statement is executed
                    else:
                        #unit_tuple is a tuple of the current top elements from both the lists in battle
                        #as the elements get popped from both the lists as per the outcome of every battle, this unit_tuple is updated with the
                        #current elements that need to fight after every round
                        #unit_tuple has the top element from units_list_a in index 0 and the top element from units_list_b in index 1
                            unit_tuple = (units_list_a[0],units_list_b[0])

                            #this is where unit_tuple is searched for, within the battle_dict dictionary
                            #once a match is obtained, a check is made to see whether the tuple[0] is the same as the value or not
                            #if that condition is satisfied, it is concluded that user A wins
                            #if tuple[1] is the same as the value, then User B has won
                            for battle_tuple in battle_dict.keys():
                                if unit_tuple == battle_tuple and battle_tuple[0] == battle_dict[(battle_tuple)]:

                                    if battle_tuple[0] == "Knight": #if a[0] is knight and b[0] is an archer
                                                                    #doesnt matter what the next element is, it will get trampled.

                                        if len(units_list_b)<=1: #this basically checks if the opposing list has more than one element
                                                                #if the opposing list has more than one element then the Knight cannot use its trample ability
                                                                #the game basically becomes a round of the basic game where a Knight beats an Archer
                                            print("\nCommander", usr_A, "wins round",rnd,"\n")
                                            flag_a = True
                                            flag_b = False

                                        else:
                                            #if the opposing army has more than 1 element, then special abilities are used
                                            loser = units_list_b.pop(0) #doesnt matter what the next element is, it will get trampled.
                                            print("\nCommander", usr_A, "'s Knight tramples Commander",usr_B,"'s next unit!!!")
                                            print("Commander", usr_A, "wins round",rnd,"\n")
                                            if med_supp_b > 0:
                                                units_list_b.append(loser)
                                                print("\nMedic saves Commander", usr_B, "'s unit who joins at the back of the army!!!")
                                                med_supp_b = med_supp_b - 1
                                                print("Medicinal Supplies Left: $" + str(med_supp_b) + "\n")
                                            elif med_supp_b == 0:
                                                print("\n",usr_B,"has no more medicinal supplies left. Unit dies!")

                                            flag_a = True
                                            flag_b = False


                                            if len(units_list_b) >= 3:
                                                #this also ensures that there are more than 1 elements in the opposing list
                                                #it also checks for the special condition where there are 3 archers lined back to back
                                                #in which case both the knight and the opposing archer use their special abilities
                                                if units_list_b[1] == "Archer": #now if the next element in the opposing army is an archer,it will shoot the knight by using its special ability
                                                    loser = units_list_a.pop(0)
                                                    print("\nCommander", usr_A,"'s Knight tramples, but Commander", usr_B, "'s Archer shoots down the surviving Knight!!")
                                                    print("Commander", usr_B, "wins round",rnd,"\n")
                                                    if med_supp_a > 0:
                                                        units_list_a.append(loser)
                                                        print("\nMedic saves Commander", usr_A,"'s unit!!!")
                                                        med_supp_a = med_supp_a - 1
                                                        print("Medicinal Supplies Left: $" + str(med_supp_a) + "\n")
                                                    elif med_supp_a == 0:
                                                        print("\n",usr_A,"has no more medicinal supplies left. Unit dies!")

                                                    #since special abilites are being used, the winner of this round changes to the other user
                                                    flag_a = False
                                                    flag_b = True

                                                #if none of the special abilities are utilised, the result is the same as that of the basic game
                                                else:
                                                    print("\nCommander", usr_A, "wins round",rnd,"\n")
                                                    flag_a = True
                                                    flag_b = False


                                    elif battle_tuple[0] == "Archer": #if a[0] is Archer and b[0] is Soldier
                                        if len(units_list_b)>1: #checks for the length of the opposing list to ensure that special ability of the archer can be used
                                            if units_list_b[1] == "Archer": #if the unit after the soldier is an archer, it can use its special ability to kill the surviving archer
                                                flag_a = False
                                                flag_b = True
                                                print("\nCommander", usr_A,"'s Archer shoots down", usr_B,"'s Soldier")
                                                print("Commander", usr_B,"'s next Archer shoots down the surviving Archer")
                                                loser = units_list_a.pop(0)
                                                print("Commander", usr_B, "wins round",rnd,"\n")

                                                if med_supp_a > 0:
                                                    units_list_a.append(loser)
                                                    print("\nMedic saves Commander", usr_A,"'s unit!!!")
                                                    med_supp_a = med_supp_a - 1
                                                    print("Medicinal Supplies Left: $" + str(med_supp_a) + "\n")

                                                elif med_supp_a == 0:
                                                    print("\n",usr_A,"has no more medicinal supplies left. Unit dies!")


                                            else:
                                                print("\nCommander", usr_A, "wins round",rnd,"\n")
                                                flag_b = True
                                                flag_a = False

                                        else:
                                            print("\nCommander", usr_A, "wins round", rnd, "\n")
                                            flag_a = True
                                            flag_b = False


                                    elif battle_tuple[0] == "Soldier": #if a[0] is Soldier and b[0] is Knight
                                        if len(units_list_b) > 1: #checks whether the opposing list has more than one unit
                                            if units_list_b[1] == "Archer": #if the unit after the knight is an archer, it can use its special ability to kill the surviving soldier
                                                loser = units_list_a.pop(0)
                                                print("\nCommander", usr_A,"'s Soldier beats Commander", usr_B,"'s Knight!!!")
                                                print("\nCommander",usr_B,"'s Archer shoots down Commander",usr_A,"'s surviving Soldier!!!")
                                                if med_supp_a > 0:
                                                    units_list_a.append(loser)
                                                    print("\nMedic saves Commander", usr_A,"'s unit who joins at the back of the army!!!")
                                                    med_supp_a = med_supp_a - 1
                                                    print("Medicinal Supplies Left: $" + str(med_supp_a) + "\n")
                                                elif med_supp_a == 0:
                                                    print("\n",usr_A,"has no more medicinal supplies left. Unit dies!")

                                                #since special abilitites are being used, the winner is user B
                                                flag_a = False
                                                flag_b = True
                                                print("\nCommander", usr_B, "wins round",rnd,"\n")

                                            #if special abilities are not used the result is the same as that of the basic game
                                            else:
                                                flag_a = True
                                                flag_b = False
                                                print("\nCommander", usr_A, "wins round",rnd,"\n")

                                        else:
                                            flag_a = True
                                            flag_b = False
                                            print("\nCommander", usr_A, "wins round",rnd,"\n")

                                    loser = units_list_b.pop(0)
                                    #the rnd variable gets incremented after every round of fight to indidcate the end of the round
                                    rnd +=1
                                    if med_supp_b > 0:
                                        units_list_b.append(loser)
                                        print("\nMedic saves Commander", usr_B,"'s unit who joins at the back of the army!!!\n")
                                        med_supp_b = med_supp_b - 1
                                        print("\nMedicinal Supplies Left: $" + str(med_supp_b) + "\n")
                                    elif med_supp_b == 0:
                                        print("\n",usr_B,"has no more medicinal supplies left. Unit dies!")

                                #the logic and mechanics if user B wins is the same as that of User A winning
                                #this below section is for when the winner of the battle is User B
                                elif unit_tuple == battle_tuple:

                                    if battle_tuple[1] == "Knight": #if b[0] is knight and a[0] is an archer
                                        if len(units_list_a)<=1:
                                            print("Commander", usr_B, "wins round",rnd,"\n")
                                            flag_b = True
                                            flag_a = False
                                        else:
                                            loser = units_list_a.pop(0) #doesnt matter what the next element is, it will get trampled.
                                            print("\nCommander", usr_B, "'s Knight tramples Commander", usr_A,"'s next unit!!")
                                            print("\nCommander", usr_B, "wins round",rnd,"\n")
                                            if med_supp_a > 0:
                                                units_list_a.append(loser)
                                                print("\nMedic saves Commander", usr_A, "'s unit who joins at the back of the army!!!")
                                                med_supp_a = med_supp_a - 1
                                                print("Medicinal Supplies Left: $" + str(med_supp_a) + "\n")
                                            elif med_supp_a == 0:
                                                print("\n",usr_A,"has no more medicinal supplies left. Unit dies!")

                                            print("\nCommander", usr_B, "'s Knight tramples!!")
                                            flag_b = True
                                            flag_a = False

                                            if len(units_list_a) >= 3:
                                                if units_list_a[1] == "Archer": #now if the next element is an archer,it will shoot the knight
                                                    loser = units_list_b.pop(0)
                                                    print("\nCommander", usr_B,"'s Knight Tramples but Commander",usr_A,"'s Archer shoots down the surviving Knight!!!")
                                                    print("Commander", usr_A, "wins round",rnd,"\n")
                                                    if med_supp_b > 0:
                                                        units_list_b.append(loser)
                                                        print("\nMedic saves Commander", usr_B,"'s unit who joins at the back of the army!!!")
                                                        med_supp_b = med_supp_b - 1
                                                        print("Medicinal Supplies Left: $" + str(med_supp_b) + "\n")
                                                    elif med_supp_b == 0:
                                                        print("\n",usr_B,"has no more medicinal supplies left. Unit dies!")

                                                    flag_b = False
                                                    flag_a = True
                                                else:
                                                    print("\nCommander",usr_B,"wins round",rnd,"\n")
                                                    flag_b = True
                                                    flag_a = False



                                    elif battle_tuple[1] == "Archer": #if b[0] is Archer and a[0] is Soldier
                                        if len(units_list_a)>1:
                                            if units_list_a[1] == "Archer":
                                                flag_b = False
                                                flag_a = True
                                                loser = units_list_b.pop(0)
                                                print("\nCommander", usr_B,"'s Archer shoots down Commander", usr_A,"'s Soldier")
                                                print("Commander", usr_A,"'s next Archer shoots down the surviving Archer\n")
                                                print("Commander", usr_A, "wins round",rnd,"\n")
                                                if med_supp_b > 0:
                                                    units_list_b.append(loser)
                                                    print("\nMedic saves Commander", usr_B,"'s unit who joins at the back of the army!!!\n")
                                                    med_supp_b = med_supp_b - 1
                                                    print("Medicinal Supplies Left: $" + str(med_supp_b) + "\n")
                                                elif med_supp_b == 0:
                                                    print("\n",usr_B,"has no more medicinal supplies left. Unit dies!")
                                                #print("Commander B's Archer shoots down A's Soldier")
                                                #print("Commander A's next Archer shoots down the surviving Archer")
                                            else:
                                                print("\nCommander", usr_B, "wins round",rnd,"\n")
                                                flag_b = True
                                                flag_a = False
                                        else:
                                            print("\nCommander", usr_B, "wins round",rnd,"\n")
                                            flag_b = True
                                            flag_a = False

                                    elif battle_tuple[1] == "Soldier": #if b[0] is Soldier and a[0] is Knight
                                        if len(units_list_a) > 1:
                                            if units_list_a[1] == "Archer":
                                                loser = units_list_b.pop(0)
                                                print("\nCommander", usr_B,"'s Soldier beats Commander", usr_A,"'s Knight!!")
                                                print("Commander", usr_A,"'s Archer shoots down the surviving Soldier!!!")
                                                print("Commander", usr_A,"wins round",rnd,"\n")
                                                if med_supp_b > 0:
                                                    units_list_b.append(loser)
                                                    print("\nMedic saves Commander", usr_B,"'s unit!!!\n")
                                                    med_supp_b = med_supp_b - 1
                                                    print("Medicinal Supplies Left: $" + str(med_supp_b) + "\n")
                                                elif med_supp_b == 0:
                                                    print("\n",usr_B,"has no more medicinal supplies left. Unit dies!")

                                                flag_b = False
                                                flag_a = True

                                            else:
                                                flag_b = True
                                                flag_a = False
                                                print("\nCommander", usr_B, "wins round",rnd,"\n")

                                        else:
                                            flag_b = True
                                            flag_a = False
                                            print("\nCommander", usr_B, "wins round",rnd,"\n")


                                    loser = units_list_a.pop(0)
                                    rnd+=1
                                    if med_supp_a > 0:
                                        units_list_a.append(loser)
                                        print("\nMedic saves Commander", usr_A,"'s unit!!!\n")
                                        med_supp_a = med_supp_a - 1
                                        print("Medicinal Supplies Left: $" + str(med_supp_a) + "\n")
                                    elif med_supp_a == 0:
                                        print("\n",usr_A,"has no more medicinal supplies left. Unit dies!")



            #After the battle is done, the outcome is decided by looking at the flag variables
            #Outcomes can also be decided by looking at the length of both lists
            #if flag_a is True at the end of the last round, then User A has won the battle
            #if flag_b is True at the end of the last round, then User B has won the battle
            #if the length of units_list_a becomes 0, it means the User A has used up all his units and thus User B wins
            #if the length of units_list_b becomes 0, it means the User B has used up all his units and thus User A wins
            if flag_a == False and flag_b == False and len(units_list_a) == 0 and len(units_list_b)== 0:
                print('\nNEITHER OF YOU WIN, THE BATTLE ENDS IN A DRAW!!!!!!')

            elif flag_a == False and flag_b == False and len(units_list_a)<1:
                print("\nCommander",usr_A,"has run out of units!")
                print('\nCommander', usr_B, 'WINS THE BATTLE!!!!!!')

            elif flag_a == False and flag_b == False and len(units_list_b)<1:
                print("\nCommander",usr_B,"has run out of units!")
                print('\nCommander', usr_A, 'WINS THE BATTLE!!!!!!')

            elif flag_a == False and flag_b == False:
                print('\nNEITHER OF YOU WIN, THE BATTLE ENDS IN A DRAW!!!!!!')

            else:
                        if len(units_list_a) < 1:
                            print('\nCommander', usr_B, 'WINS THE BATTLE!!!!!!') #B still has a unit left in his army while A has used up all his units

                        elif len(units_list_b) < 1:
                            print('\nCommander', usr_A, 'WINS THE BATTLE!!!!!!')

                        else:
                            if flag_a == True:
                                print('\nCommander', usr_A, 'WINS THE BATTLE!!!!!!')
                            elif flag_b == True:
                                print('\nCommander', usr_B, 'WINS THE BATTLE!!!!!!')
