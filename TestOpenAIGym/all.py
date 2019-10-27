import gym
import sys
list = ['CartPole-v0','MountainCar-v0', 'MsPacman-v0', 'Hopper-v1']

elm = list[int(sys.argv[1])]
env = gym.make(elm)
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()
