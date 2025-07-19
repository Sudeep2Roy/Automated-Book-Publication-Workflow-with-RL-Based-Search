
import numpy as np
import random

class RLAgent:
    def __init__(self, states, actions, alpha=0.1, gamma=0.6, epsilon=0.1):
        self.state_index = {s: i for i, s in enumerate(states)}
        self.action_index = {a: i for i, a in enumerate(actions)}
        self.q_table = np.zeros((len(states), len(actions)))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.states = states
        self.actions = actions

    def select_action(self, state):
        idx = self.state_index[state]
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        return self.actions[np.argmax(self.q_table[idx])]

    def update(self, state, action, reward, next_state):
        s = self.state_index[state]
        a = self.action_index[action]
        ns = self.state_index[next_state]

        old_value = self.q_table[s, a]
        next_max = np.max(self.q_table[ns])
        new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
        self.q_table[s, a] = new_value
