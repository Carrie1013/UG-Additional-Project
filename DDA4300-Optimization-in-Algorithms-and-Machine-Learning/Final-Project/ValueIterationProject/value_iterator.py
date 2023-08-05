#######################################################################
#
# Retrieve the initialized state-value pairs from state_extractor.py
# and apply Value Iteration over all the states several times 
# until convergence (usually not more than 3 loops)
#
#######################################################################
 
import pickle
from utils import *
import matplotlib.pyplot as plt
with open('/Users/qiaochufeng/Desktop/tic-tac/ValueIter/memory/state_value_init.txt', 'rb') as file:
    memory = pickle.load(file)
    
states = memory[0]
x_values = memory[1]
o_values = memory[2]

delta = 5
iter = 0
gamma = 0.9
D =[]
X = [i for i in range(5)]
for i in range(5):
    delta = 0
    for state in states:
        done = check_done(state)
        index = states.index(state)
        player = (sum(state) == 0)  # 0 for o, 1 for x
        if done != 0:
            continue
        legal_moves = [i for i, value in enumerate(state) if value == 0]
        legal_values = []
        for action in legal_moves:
            outcome_indices = possible_outcome_indices(states, state, action)
            p = 1 / len(outcome_indices)
            action_value = 0
            for i in outcome_indices:
                if player:
                    value = x_values[i]
                else:
                    value = o_values[i]
                action_value += p * value          
            iter += (len(legal_moves))
            legal_values.append(round(action_value, 3))  
        updated_value = max(legal_values)
        if player:
            delta = max(delta, abs(x_values[index]-updated_value))
            x_values[index] = gamma * updated_value
        else:
            delta = max(delta, abs(o_values[index]-updated_value))
            o_values[index] = gamma * updated_value   
    D.append(delta)
plt.plot(X, D)
state_action = [states, x_values, o_values]
# print(iter)

# with open('/Users/qiaochufeng/Desktop/tic-tac/ValueIter/memory/state_action.txt', 'wb') as file:
#     pickle.dump(state_action, file)
    
print('Successfully iterated over the states until convergence!')
print('Enjoy it!')
        
    