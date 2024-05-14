from abc import ABC, abstractmethod
import time

from browsergym.utils.obs import flatten_axtree_to_str, flatten_dom_to_str
from browsergym.core.action.highlevel import HighLevelActionSet

from functions import say, click, textinput, load, scroll

class Agent(ABC):
    """
    A template class that defines the required signature of an agent interacting with a browsergym environment.
    """

    @abstractmethod
    def reset(self, seed=None) -> None:
        """
        Resets the agent.
        """
        pass

    @abstractmethod
    def get_action(self, obs: dict) -> str:
        """
        Updates the agent with the current observation, and returns its next action (plus an info dict, optional).

        Parameters:
        -----------
        obs: dict
            The current observation of the environment.
        """
        pass

    def preprocess_obs(self, obs: dict) -> dict:
        """
        Default preprocessing of the observation.
        """
        pass

    def get_action_mapping(self) -> callable:
        """
        Returns a callable that can be used to map the agent actions to executable python code.
        """
        return None
    
class DoWhatISayAgent(Agent):
    def reset(self, seed=None) -> None:
        self.last_n_user_msgs = None
        pass

    def get_action(self, obs: dict) -> str:
        # preprocessing
        obs["dom_txt"] = flatten_dom_to_str(obs["dom_object"])
        obs["axtree_txt"] = flatten_axtree_to_str(obs["axtree_object"])
        obs["raw_html"] = obs["dom_txt"].replace('bid=', 'data-webtasks-id=')

        xprops = obs["extra_element_properties"]

        obs['bboxes'] = {
            k: zip(['x', 'y', 'width', 'height'], xprops[k]['bbox'])
            for k in xprops if xprops[k]['visibility'] == 1.0
        }

        obs['visible'] = {
            k: xprops[k]['visibility'] == 1.0
            for k in xprops
        }

        action = self.do_what_i_say(obs)
        
        print(f'Last action error:\n{obs["last_action_error"]}')

        return action

    def do_what_i_say(self, obs: dict) -> str:
        last_user_message = None
        n_usr_msgs = 0
        for message in obs['chat_messages']:
            if message["role"] == "user":
                last_user_message = message["message"]
                n_usr_msgs += 1

        if self.last_n_user_msgs is None or self.last_n_user_msgs != n_usr_msgs and n_usr_msgs > 0:
            print('last_user_message:', last_user_message)
            action = last_user_message
        else:
            time.sleep(1)
            action = "say('type a command')"
        
        self.last_n_user_msgs = n_usr_msgs

        return action

    def repeat_in_uppercase(self, obs: dict) -> str:
        last_user_message = None
        for message in reversed(obs['chat_messages']):
            print(message.keys())
            if message["role"] == "user":
                last_user_message = message["message"]
                break
        
        time.sleep(1)

        if last_user_message:
            return f"say({repr(last_user_message.upper())})"
        else:
            return "say('Hello, World!')"

    def get_action_mapping(self) -> callable:
        """
        Returns a callable that can be used to map the agent actions to executable python code.
        """
        action_set = HighLevelActionSet(
            subsets="custom",
            custom_actions= [say, click, textinput, load, scroll],
            multiaction=False,
            strict=True)
        return action_set.to_python_code