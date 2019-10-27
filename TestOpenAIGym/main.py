import gym
env = gym.make('CartPole-v0')
env.reset()
for t in range(1000):
    env.render()
    act_rand = env.action_space.sample()
    observation,reward,done, info = env.step(act_rand) # take a random action
    print(observation)
    print(reward)
    print(done)
    print(info)
    print()
    if done:
    	print("Episode finished after {} timesteps".format(t+1))
    	break
env.close()
