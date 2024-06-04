import gymnasium as gym
import browsergym.webarena  # register webarena tasks as gym environments
from agent import DoWhatISayAgent

agent = DoWhatISayAgent()

env = gym.make(
    "browsergym/webarena.310",
    headless=False,
    wait_for_user_message=False,
    action_mapping=agent.get_action_mapping(),
    # task_kwargs={},
)

agent.reset()
obs, info = env.reset()

done = False
while not done:
    action = agent.get_action(obs)
    obs, reward, terminated, truncated, info = env.step(action)
