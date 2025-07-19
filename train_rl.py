
from rl_agent import RLAgent
from feedback import simulate_feedback

states = ["vivid", "formal", "short", "creative"]
actions = ["original", "ai-written", "reviewed", "final"]
agent = RLAgent(states, actions)

for episode in range(100):
    state = states[episode % len(states)]
    action = agent.select_action(state)
    
    reward = simulate_feedback(state, action)
    next_state = states[(episode + 1) % len(states)]

    agent.update(state, action, reward, next_state)

    print(f"Episode {episode+1}: Query={state}, Selected={action}, Reward={reward}")
