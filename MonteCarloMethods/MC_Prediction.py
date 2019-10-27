import gym
import numpy as np
from collections import defaultdict



def generate_episode_from_limit_stochastic(bj_env):
    episodes = []
    state = bj_env.reset()
    while True:
        s = state[0]
        
        probs = [0.8,0.2] if s>18 else [0.2,0.8]
        action = np.random.choice(np.arange(2),p=probs)
        print('State: ', s, " Action: ",action)
        next_state, reward , done, info = bj_env.step(action)
        print('new: ', next_state," - ", reward ," - ", done, " - ",info)
        episodes.append((state,action,reward))
        if done:
            break

    return episodes

for i in range(3):
    print(i)
    print(generate_episode_from_limit_stochastic(env))

    def mc_prediction_q(env,num_episodes,generate_episode,gamma=1.0):
        returns_sum = defaultdict(lambda:np.zeros(env.action_space.n))
        N = defaultdict(lambda:np.zeros(env.action_space.n))
        Q = defaultdict(lambda:np.zeros(env.action_space.n))

        for i_episode in range(1,num_episodes+1):
            if i_episode % 1000 = 0 :
                print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
                sys.stdout.flush()
                

        return Q
