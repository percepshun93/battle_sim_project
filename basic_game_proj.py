'''Name: Subhasish Sarkar
   Game Type: Basic game
 '''


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
    print(usr_A,'The units you have purchased are:',a_count,' Soldiers,',b_count,'Knights,','and',c_count,'Archers\n')
    print("Your Army: ",units_list_a)
    print('Commander',usr_A,'Your army has been assembled!\n')

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
        print("Commander",usr_B,'has quit the game.')
    else:
        print(usr_B,'The units you have purchased are:',a_count,' Soldiers,',b_count,'Knights,','and',c_count,'Archers\n')
        print(units_list_b)
        print('\nCommander',usr_B,'Your army has been assembled!\n')

        #after user B has taken his inputs, the battle begins
        #the battle algorithm first checks for the condition of a tie, wherein the list element at the top of both users' lists will be the same
        #If that is not the case then the battle algorithm executes further

        print("\nTHE BATTLE BEGINS!!\n")

        #iter_a and iter_b are list iterator variables. they are set to 1 as a starting point
        #they increment by 1 if a unit dies
        #iter_a increments if a unit from units_list_a dies
        #iter_b increments if a unit from units_list_b dies
        #winner_list is an empty list which will store the winner of every round once the battle takes place
        #flag_a and flag_b are flag boolean variables which are set to False at the start and will toggle to True whenever either user wins
        #if user A wins, flag_a is set to True
        #if user b wins, flag_b is set to True
        #if the round ends in a tie, both flags remain at False
        #rnd is a variable that represents the round of the battle. it gets incremented after the end of every round
        iter_a = 1
        iter_b = 1
        winner_list = []
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
                while (iter_a<=len(units_list_a) and iter_b<=len(units_list_b)):
                    #this is where the check for the tie happens
                    #when two units of the same type fight each other, they both kill each other, thus the list iterators both increment
                    #to indicate that the next to units need to go into battle
                    #rnd is then incremented to indicate the end of a round
                    if units_list_a[iter_a-1] == units_list_b[iter_b-1]:
                            print('Round',rnd,'ends in a draw!\n')
                            iter_a = iter_a + 1
                            iter_b = iter_b + 1
                            flag_a = False
                            flag_b = False
                            rnd += 1

                    #if the battle does not end in a tie, this else statement is executed
                    else:
                            #unit_tuple is a tuple of the current elements from both the lists in battle
                            #as the iterators iter_a and iter_b are incremented as per the outcome of every battle, this unit_tuple is updated with the
                            #current elements that need to fight after every round
                            #unit_tuple has an element from units_list_a in index 0 and an element from units_list_b in index 1
                            unit_tuple = (units_list_a[iter_a-1],units_list_b[iter_b-1])

                            #this is where unit_tuple is searched for, within the battle_dict dictionary
                            #once a match is obtained, a check is made to see whether the tuple[0] is the same as the value or not
                            #if that condition is satisfied, it is concluded that user A wins
                            #if tuple[1] is the same as the value, then User B has won
                            for battle_tuple in battle_dict.keys():
                                if unit_tuple == battle_tuple and battle_tuple[0] == battle_dict[(battle_tuple)]: #user A has won
                                    print('Commander',usr_A,'wins round',rnd,'\n')
                                    flag_a = True
                                    flag_b = False
                                    iter_b = iter_b + 1
                                    winner_list = units_list_a[iter_a-1]
                                    rnd += 1

                                elif unit_tuple == battle_tuple: #user B has won
                                    print('Commander',usr_B,'wins round',rnd,'\n')
                                    flag_b = True
                                    flag_a = False
                                    iter_a = iter_a + 1
                                    winner_list = units_list_b[iter_b-1]
                                    rnd += 1

            #After the battle is done, the outcome is decided by looking at the flag variables
            #Outcomes can also be decided by looking at the iterator variables
            #if flag_a is True at the end of the last round, then User A has won the battle
            #if flag_b is True at the end of the last round, then User B has won the battle
            #if iter_a goes beyond the length of units_list_a, it means the User A has used up all his units and thus User B wins
            #if iter_b goes beyond the length of units_list_b, it means the User B has used up all his units and thus User A wins
            #in some cases the flags may be set to false at the same time only user A runs out of units, in that case the correct prompt is shown here
            if not(flag_a == False and flag_b == False) and iter_a > len(units_list_a): #in some cases the flags may be set to false at the same time only user A runs out of units, in that case the correct prompt is shown here

                print('\nCommander', usr_A, 'has run out of units!!')
                print('\nCommander',usr_B,"has",winner_list,"standing!!!")
                print('\nCommander', usr_B, 'WINS THE BATTLE!!!!!!\n') #B still has a unit left in his army while A has used up all his units

            elif not(flag_a == False and flag_b == False) and iter_b > len(units_list_b):#in some cases the flags may be set to false at the same time only user B runs out of units, in that case the correct prompt is shown here

                print('\nCommander', usr_B, 'has run out of units!!')
                print('\nCommander',usr_A,"has",winner_list,"standing!!!")
                print('\nCommander', usr_A, 'WINS THE BATTLE!!!!!!\n')

            elif flag_a == False and flag_b == False:
                        print('\nNEITHER OF YOU WIN, THE BATTLE ENDS IN A DRAW!!!!!!\n')

            else:
                    if iter_a > len(units_list_a):

                        print('\nCommander', usr_A, 'has run out of units!!')
                        print('\nCommander',usr_B,"has",winner_list,"standing!!!")
                        print('\nCommander', usr_B, 'WINS THE BATTLE!!!!!!\n') #B still has a unit left in his army while A has used up all his units

                    elif iter_b > len(units_list_b):

                        print('\nCommander', usr_B, 'has run out of units!!')
                        print('\nCommander',usr_A,"has",winner_list,"standing!!!")
                        print('\nCommander', usr_A, 'WINS THE BATTLE!!!!!!\n')

                    else:
                        if flag_a == True:

                            print('\nCommander',usr_A,"has",winner_list,"standing!!!")
                            print('\nCommander', usr_A, 'WINS THE BATTLE!!!!!!\n')
                        elif flag_b == True:

                            print('\nCommander',usr_B,"has",winner_list,"standing!!!")
                            print('\nCommander', usr_B, 'WINS THE BATTLE!!!!!!\n')
