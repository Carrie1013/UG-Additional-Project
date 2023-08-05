## Project_Report_120090272

### Question: Tic-Tac-Toe Game

In this problem, we want to develop the optimal strategy for the cross-player. We assume that the cross-player plays first, and the opponent is a random player. That is, the opponent puts a circle in an empty square with equal probability in each round. Please formulate the 3 × 3 tic-tac-toe game as an MDP problem and find the optimal policy. In addition, what can you tell about the optimal first step for the cross player in the 4 × 4 tic-tac-toe game?

### MDP background in this Question

##### 1. Background

To formulate the game into an MDP problem, the environment should be characterized by a Markov transition equation where the value of transition probablility for subsequent state and reward depends only on the immediate state and action: $p(s', r|s,a)$.

When an agent in state $S_t$ takes an action $A_t$ as prescribed by a policy $\pi$, it transitions to a state $S_{t+1}$ and receives a reward $R_{t+1}$. The Agent interacting with the MDP environment thus gives rise to a trajectory: $S_0,A_0,R_1,S_1,A_1,R_2,S_2,...$ and the goal of an agent is to maximize the long term return, which is defined as the discounted sum of future return: $G_t=\sum\limits_{k=0}^{\infin}\gamma^kR_{t+k+1}=R_{t+1}+\gamma G_{t+1}$.

##### 2. Optimization

In this game we use State-Value function of a state $s$ under current policy $\pi$, and the value is the expected return from following policy $\pi$ when starting in state $s$: $v_{\pi}(s)=E_{\pi}[G_t|S_t=s]$. In the meanwhile, the Action-Value function is the value of taking action $a$ in state $s$ under policy $\pi$ and thereafter following the policy: $q_{\pi}(s,a)=E_{\pi}[G_t|S_t=s,A_t=a]$.

According to the Bellman equation: $v_{\pi}(s)=E[G_t|S_t=s]=E_{\pi}[R_{t+1}+\gamma G_{t+1}|S_t=s]=\sum\limits_a\pi(a|s)\sum\limits_{s',r}p(s',r|s,a)[r+\gamma v_{\pi}(s')]$. So the Bellman optimality equation for state values is given by $v_*(s)=\mathop{max}\limits_a\sum\limits_{s',r}p(s',r|s,a)[r+\gamma v_{\pi}(s')]$.

### Design of MDP

As given in the requirement, the cross-player is what we need to find an optimal policy for, and the circle-player is a random player. After the cross-player plays, the move by the opposing player is considered a change in the environment resulting from the agent’s actions. The new state the agent lands in is a board where the opposing player has already made his/her move.

##### 1. Value Iteration Method

###### Part I: Algorithm

###### Part II: Notation and Environment settings

State-value: `{[0,0,0,0,0,0,0,0,0]:0}`
At each iteration of game, record `self.states` as: `[[0,...,0],[0,...,1],...,[1,...,0]]` 

###### Part III: Mechanism Design

##### Q-learning Method

###### Part I: Algorithm

```pseudocode
Initialize Q=(s, a), for all s in S, a in A[s],arbitrarily except that Q(terminal, ·)=0
For each Iteration do:
	Initialize S
	Loop for each step of episode:
		Choose A from S using policy derived from Q (eg, eps-greedy)
		Take action A, Observe R, S‘
		Q(S,A) <-- Q(S,A) + step_size * [R + gamma * max_a Q(S’,A) - Q(S, A)]
		S <-- S‘
	untill S is terminal
```

###### Part II: Notation and Environment settings

State-value: 

###### Part III: Mechanism Design

Result Plot

##### Comparison of VI and Q-learning

Value Iteration is a model based method and Q-learning is a model-free off policy method

VI needs to know the environment transition model $p(r|s,a)$ and $p(s'|s,a)$ to update the state-value
While Q-learning only needs to 

VI solved by dynamic programming idea, but Q-learning

VI is a fixed-point mapping

## Notes on 0417 and 0419

MDP: 

- MDP - generative model
- MDP - model-free method 
- MDP - table based (DP)



- Online Programming: desicion flow follows with information flow
- DP: offline learning
- State Aggregation



- 另一个组：RL+Retrained模型 (Transition --- Random视为)

- Idea: 

  - MDP with VI: Formula + Experiment performance (只用了前面的Random) 
    $\Rightarrow$ 只在游戏结束产生可evaluate的return，加Cyclic意义不大
    - 3*3 ($V(s)\leftarrow V(s)+\alpha(V(s')-V(s))$, Bellman Equation解)
    - 4*4 (rate明显变慢)
  - MDP with RL: Formula + Experiment performance 
    - Tabular Q-Learning Agents
      $Q(S, a)\rightarrow Q(S,a)+\alpha[R_a(S,S')+\gamma·\mathop{max}\limits_{a'} Q(S',a')]$ 
    - Model-free value controled Agents (只写了formula，没必要but可以加experiment)
      (状态空间小于2w，大模型适用)
  - MDP v.s. Deep Neural Network: 
    - How $\rightarrow$ Formulate as classification model
    - (分类模型---分为X获胜、O获胜、平局，训练后的一系列可能的动作传递给我们的模型，然后选择最有可能产生预期结果的动作---一种选择较高value的表现)
  - MDP VI v.s. RL /// MDP v.s. Artificial Neaural Network
    - RL加入了判断指标，converge rate变慢
    - 小空间内表现不明显，大空间内Accuracy变高
    - 和Deep Learning的Accuracy比较

  - Conclusion

- How to model as MDP ---> Intuitive solution: Tabular ---> Better solution: model-based Value Iteration (Already a random value iteration because the next step is always unsure -- pick by probability of 1/possible position) ---> For larger state-action space:model-free Q-learning+epsilon greedy ---> More states solution: Neural Network (not very explainable)

### Part I. MDP with VI





