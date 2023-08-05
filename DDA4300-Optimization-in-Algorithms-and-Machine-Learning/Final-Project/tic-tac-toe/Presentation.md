## Introduction

So here comes to the Tic-Tac-Toe game part. 
We know playing t-t-t game is a sequential decision making process, so in the requirement of this question we're supposed to use previous MDP knowledge to give a model for cross-player agent for choosing action. To find the best policy, I have tried many possible approaches like MDP with direct tabular method, value iteration, Q-learning and Neural Networks.

## Game Setting and Notations

So to begin with, how can it be formulated in an MDP problem. 
Because we cannot  know the result until  the last step comes out. So we consider a whole game as one iteration.  And at end of each game, I feedback the result as giving reward to the previous steps to update the value of each state. When choosing action in playing game, I pick the position with the highest value in available space. For keeping track of trajectory of all states in each game for the agent to learn, and separately record value of a state for cross-player and circle-player.

So when finally choosing action in a game, I will pick the position with the highest state value based on observation of this state in available space.
Here is an example of starting game. After training the agent of cross-player, and it has 9 available square, so the agent will choose the place with largest value to put its token. And if I turns into second round of cross-player, the value of already unavailable places will be 0 likeliness.

## Value Iteration Method

To solve this, I tried applying value iteration and MDP to teach a learning agent playing tic-tac-toe. Where I extracted all the possible states and initialize their values, then run value iteration over all the states until convergence. In each step of next value iteration, I use the policy that I gained from the previous value that I find in the last iteration. 
And I set an indicator variable myself to judge whether the value iteration converges to an optimal global policy.

$\delta=max\{\delta, |(V -V_{new})|\}$ 

To update the value function, I use the same idea on Bellman equation in the previous problems , I will not explain it here again, the value is like this $V_{k+1}(s)=\mathop{max}\limits_a(R(s,a)+\gamma\sum\limits_{s'\in S}P(s'|s,a)V_k(s'))$, the Transition probability I choose here is choosing action by uniform distribution $p = \frac1{\text{\# of possible outcome indices}}$, and because at each step I choose random as policy so it can also be considered as same priciple with the Random VI in the problem 4.

To retrive the optimal policy after the value iteration, we define policy as:
$\pi(s)=\text{argmax}_aR(s,a)+\gamma\sum\limits_{s'\in S}P(s'|s,a)V_{k+1}(s')$
I tried this value iteration and find that the value of states converges quickly.

## Problems on time and space complexity

However, in my experiment of previous trial, I find the time and memory size which is the space of this algorithm grows exponentially when I expanded my 3x3 puzzle into 4x4. So this imply that the algorithm is not good enough for a condition with even larger space like chess and go or something.

So what if I change the value updating process into another way. Assume that we don't know the transition probability of one state to another state, we need the agent to find its best policy by exploring instead of directly interact with observable environment. So here I choose to introduce Q-learning.

## Q-learning Method

The algorithm is like: here we update the value for every iteration

Use the training method to test for several rounds, we come to an ideal result in a quicker space, because the group presented on Wednesday has already explained this in detail with simulating Trained player, Random player, and even Retrained player, so i don't talk much on the experiment here on Q-learning.

So what lead to this result comparing with classical value iteration?

（可以不说

Instead of requires that both the policy (value function) in this environment and the environment under this policy (value function). the Q-learning method will try to learn the optimal strategy in each step, and the optimal strategy for the agent's environment will be obtained after several iterations. It think of the environment as the characteristic variable and the strategy as the output, to find the policy (or value function) in this environment.

## Deep Learning Approach: idea

Furthermore I have tried another method with deep learning to solve this problem. Although I find it not work better than value iteration and q-learning very much in this tic-tac-toe game. Because the limitation of this game settings. For example the total space is not large enough for deep learning, Neural Network will reduce the explainability for this model and so on. But I believe it can have greate performance on many other more complicated condition.

Here is my logic of designing this solution and my structure of neural network. I simulate the game for 10k times and keep all pairs of states, actions, q-value, and result. With putting them into a Deep neural network, it can be kind of like a classification model which classify the sequence states into cross-player win, circle-player win or tie. And I trained my network for 100 episode to get the following result.

In the experiment, I tried the trained cross player seperately play with the Trained and Random agent, compute out the win rate of trained agent to indicate its performance then get this result. We can find that it has a considerable outcome here is this page. 



















## Introduction

So here comes to the Tic-Tac-Toe game part. 
We know playing t-t-t game is a sequential decision making process, so in the requirement of this question we're supposed to use previous MDP knowledge to give a model for cross-player agent for choosing action. To find the best policy, I have tried many possible approaches like MDP with direct tabular method, value iteration, Q-learning and Neural Networks.

## Game Setting and Notations

So to begin with, how can it be formulated in an MDP problem. 
Because we cannot  know the result until  the last step comes out. So we consider a whole game as one iteration.  And at end of each game, I feedback the result as giving reward or penalty to the previous steps to update the value of each state. When choosing action in playing game, I pick the position with the highest value in available space. For keeping track of trajectory of all states in each game for the agent to learn, I flatten the square matrix to a one dimensional vector with length of squares, with 1,0,-1 represent the X, None, O, 3 pieces. And separately record value of a state for cross-player and circle-player.

So when finally choosing action in a game, I will pick the position with the highest state value based on observation of this state in available space.
Intuitively, I would like to map the next state of each state into value number. I come up an idea to use a memory board to keep the value of each state like this, in the process of playing game, im gonna update the value by this equation, so as number of iterations go large, the number of apearance of a state will have larger effect on its value. So after playing enough games with keeping the records, we can always find an optimal solution.

However, it comes up with another problem that because the policy made by the agent in simulation process of game is random. So it's hard to traverse all states in possible state space in a small number of iteration. 

## Value Iteration Method

To solve this, I tried applying value iteration and MDP to teach a learning agent playing tic-tac-toe. Where I extracted all the possible states and initialize their values, then run value iteration over all the states until convergence. In each step of next value iteration, I use the policy that I gained from the previous value that I find in the last iteration. And I set an indicator variable myself as $\delta=max\{\delta, |(V -V_{new})|\}$ to judge whether the value iteration converges to an optimal global policy.

To update the value function, I use the same idea on Bellman equation in the previous problems , I will not explain it here again, the value is like this $V_{k+1}(s)=\mathop{max}\limits_a(R(s,a)+\gamma\sum\limits_{s'\in S}P(s'|s,a)V_k(s'))$, the transition probability I choose here is choosing action by uniform distribution $p = \frac1{\text{\# of possible outcome indices}}$, and because at each step I choose random as policy so it can also be considered as same priciple with the Random VI in the problem 4.

To retrive the optimal policy after the value iteration, we define policy as:
$\pi(s)=\text{argmax}_aR(s,a)+\gamma\sum\limits_{s'\in S}P(s'|s,a)V_{k+1}(s')$
I tried this value iteration and find that the value of states converges quickly.

## Problems on time and space complexity

However, in my experiment of previous trial, I find the time and memory size which is the space of this algorithm grows exponentially when I expanded my 3x3 puzzle into 4x4. So this imply that the algorithm is not good enough for a condition with even larger space like chess and go or something.

So what if I change the value updating process into another way. Assume that we don't know the transition probability of one state to another state, we need the agent to find its best policy by exploring instead of directly interact with observable environment. So here I choose to introduce Q-learning and turn the problem into a model-free solution.

## Q-learning Algorithm

The algorithm is like:

## Q-learning Method

Use the training method to test fro several rounds, we come to an ideal result in a quicker space, because the group presented on Wednesday has already explained this in detail with simulating Trained player, Random player, and even Retrained player, so i don't talk much on the experiment here on Q-learning.

So what lead to this result comparing with classical value iteration?

## Value-Iteration v.s. Q-learning

The main difference on this two solution is model based and model-free.

The Model-based approach attempts to model the environment and select the optimal strategy based on that environment. It requires that both the policy (value function) in this environment and the environment under this policy (value function) , so this strategy is kind of like an MDP generative  model.
On the other side, the Model-free method will try to learn the optimal strategy in each step, and the optimal strategy for the agent's environment will be obtained after several iterations. It think of the environment (or observations) as the characteristic variable and the strategy as the output. It is to find the policy (or value function) in this environment, this is a kind of decision model.

The other difference was led by policy rewarding. For example in my Value Iteration method above, it was an on-policy strategy, which means, the method of learning and the method of reward are the same, in my game of iteration, I always use my updated value for next episode of iteration.
But in q-learning, it uses off-policy strategy which means that the methods of learning and rewarding are different. 



## Deep Learning Approach: idea

Furthermore I have tried another method with deep learning to solve this problem. Although I guess it will not work better than value iteration and q-learning very much in this tic-tac-toe game. Because the limitation of this game settings. For example the total space is not large enough for deep learning, Neural Network will reduce the explainability for this model and so on. But I believe it can have greate performance on many other more complicated condition.

Here is my logic of designing this solution and my structure of neural network. I simulate the game for 10k times and keep all pairs of states, actions, q-value, and result. With putting them into a Deep neural network, it can be kind of like a classification model which classify the sequence states into cross-player win, circle-player win or tie. And I trained my network for 100 episode to get the following result.

In the experiment, I tried the trained cross player seperately play with the Trained and Random agent, compute out the win rate of trained agent to indicate its performance then get this result. We can find that it has a considerable outcome here is this page. 



## Summary

- We discussed the value-iteration problem and it's variance on different conditions

- Key take take-away message:

  For VI:


  For tic-tac-toe:
  Q-learning is better than Value Iteration in time and space complexity
  Deep Reinforcement Learning has better acc than basic MDP problem in complicated problem

- Potential future directions and Limitation::

  For VI and its variation:

  For tic-tac-toe:
  Expand the game from 3x3 or 4x4 to a larger space, try in other strategy game

### Appendix

- Algorithm on Value-Iteration in this solution

```pseudocode
For i in range(max_iterate=5):
	delta = 0
	for state in states:
		done != 0, state_index, player, legal_moves = [state_index where state_value == 0]
		legal_values = []
		for action in legal_moves:
			possible_indices(states, state, action) ---> list
			p = 1/len(possible_indices)
			action_value = 0
			for i in possible_indices:
				if player = 1: value = x_values[i]
				if player = 0: value = o_values[i]
				action_value += p*value
			legal_values.append(action_value)
		if player:
        delta = max(delta, abs(x_values[state_index]-max(legal_values)))
        x_values[index] = gamma * max(legal_values)
    else:
        delta = max(delta, abs(o_values[state_index]-max(legal_values)))
        o_values[index] = gamma * max(legal_values)
		
```

- Algorithm for Q-learning
  Experiment result for Q-learning
  Q-learning可以加速的证明equations
- Deep learning Experiment结果
  深度学习网络结构

















