import gymnasium as gym
import browsergym.core  # register the openended task as a gym environment
from agent import DoWhatISayAgent

agent = DoWhatISayAgent()

env = gym.make(
    "browsergym/openended",
    headless=False,
    wait_for_user_message=True,
    action_mapping=agent.get_action_mapping(),
    task_kwargs={"start_url": "https://www.google.com/"},
)

agent.reset()
obs, info = env.reset()

done = False
while not done:
    action = agent.get_action(obs)
    obs, reward, terminated, truncated, info = env.step(action)
