# Vaccum Cleaner Agent

def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("enter the current location of the vaccum \t") 
    status_input = input("enter the state "+" " + location_input + "\t") 
    status_input_complement = input("enter the state of other room \t")
    initial_state = {'A' : status_input , 'B' : status_input_complement}
    print("initial location condition" + str(initial_state))

    if location_input == 'A':
        print("vacuum is placed in location A")
        if status_input == '1':
            print("location A is dirty.")
            goal_state['A'] = '0'
            cost += 1                      
            print("cost for cleaning A " + str(cost))
            print("location A has been cleaned.")

            if status_input_complement == '1':
                print("location B is dirty.")
                print("moving right to location B. ")
                cost += 1                
                print("cost for moving RIGHT : " + str(cost))
                goal_state['B'] = '0'
                cost += 1                       
                print("cost for sucking : " + str(cost))
                print("location B has been cleaned. ")
            else:
                print("no action" + str(cost))
                print("location B is already clean.")

        if status_input == '0':
            print("location A is already clean ")
            if status_input_complement == '1':
                print("location B is Dirty.")
                print("moving RIGHT to location B. ")
                cost += 1                       
                print("cost for moving RIGHT : " + str(cost))
                goal_state['B'] = '0'
                cost += 1                     
                print("cost for sucking the dirt : " + str(cost))
                print("location B has been cleaned. ")
            else:
                print("no action " + str(cost))
                print(cost)
                print("location B is already clean.")

    else:
        print("vacuum is placed in location B")
        if status_input == '1':
            print("location B is dirty.")
            goal_state['B'] = '0'
            cost += 1  
            print("cost for cleaning : " + str(cost))
            print("location B has been cleaned.")

            if status_input_complement == '1':
                print("location A is dirty.")
                print("moving LEFT to the location A. ")
                cost += 1  
                print("cost for moving LEFT : " + str(cost))
                goal_state['A'] = '0'
                cost += 1  
                print("cost for sucking the dirt : " + str(cost))
                print("Location A has been Cleaned.")

        else:
            print(cost)
            print("location B is already clean.")

            if status_input_complement == '1': 
                print("location A is dirty.")
                print("moving LEFT to location A. ")
                cost += 1  
                print("cost for moving LEFT " + str(cost))
                goal_state['A'] = '0'
                cost += 1  
                print(" cost for sucking the dirt " + str(cost))
                print("location A has been cleaned. ")
            else:
                print("no action " + str(cost))
                print("location A is already clean.")

    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))


vacuum_world()
