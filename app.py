#Local Search Group assignment 
#app.py 
#Group 5
import nqueens
import math
import random


#Annealing function, takes in a board state, a Temperature(always 100), a decay rate and the threshold
#Passes the temperature value and decay rate into scheduling and uses annealing algorithm to choose the best board
def annealing(b, T, decay_rate, threshold):
    current = b
    current.h = nqueens.numAttackingQueens(current)
    
    #Annealing algorithm
    while(T > threshold or current.h != 0):
        
        current.h = nqueens.numAttackingQueens(current)
        rand2 = random.randint(0,(len(nqueens.getSuccessorStates(current))-1))
        neigh = nqueens.getSuccessorStates(current)[rand2]
        neigh.h = nqueens.numAttackingQueens(neigh)
        
        T = scheduling(T, decay_rate)
        E = current.h - neigh.h
        randNum = random.random()
        
        if E > 0:
            current = neigh
        else:
            if math.exp(E/T) > randNum:
                current = neigh
        if T < threshold:
            return current
            
    return current
    

#Scheduling function takes in T and decay_rate, uses scheduling formula in textbook to decrease T and return it
def scheduling(T,decay_rate):
    schedule = T * decay_rate
    return schedule
    
      
def main():
    T = 100
    
    #Board size of 4, and the subsequent output loops
    bSize = 4
    b = nqueens.Board(bSize)
    b.rand()
    decayRate = 0.9
    tHold =  0.000001
    print ("Board Size: " + str(bSize))
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
        
    decayRate = 0.75
    tHold =  0.0000001
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
        
    decayRate = .5
    tHold =  0.00000001    
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
    
    ##############################################################################################################
        
    #Boardsize of 8, and the subsequent output loops
    bSize = 8
    b = nqueens.Board(bSize)
    b.rand()
    decayRate = 0.9
    tHold =  0.000001
    print ("Board Size: " + str(bSize))
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
        
    decayRate = 0.75
    tHold =  0.0000001
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
        
    decayRate = .5
    tHold =  0.00000001    
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
    
    ###############################################################################################################################
    
    #Board size of 16, and the subsequent output loops    
    bSize = 16
    b = nqueens.Board(bSize)
    b.rand()
    decayRate = 0.9
    tHold =  0.000001
    print ("Board Size: " + str(bSize))
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
        
    decayRate = 0.75
    tHold =  0.0000001
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
        
    decayRate = .5
    tHold =  0.00000001    
    x = 0
    while(x < 10):
        print("\n#####################################################\n\nRun " + str(x+1))
        print("Initial Board State: ")
        b.printBoard()
        print("\nh value: " + str(b.h))
        print ("Decay Rate: " + str(decayRate) + "       " + "T Threshold: " + str(tHold))
        d = annealing(b, T, decayRate, tHold)
        print("")
        print("Final board: ")
        d.printBoard()
        print("Final h value: " + str(d.h))
        x+=1
    
main()
