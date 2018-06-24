import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('CartPole-v0')

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        env.render()
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
            
    return totalreward

def train():
    counter = 0
    bestparams = None
    bestreward = 0

    for _ in range(10000):
        counter += 1
        parameters = np.random.rand(4) * 2 - 1
        reward = run_episode(env,parameters)
        if reward > bestreward:
            bestreward = reward
            bestparams = parameters
            if reward == 400:
                break
                
                
    return counter, bestparams

Counter, finalParameters = train()
print(Counter,finalParameters)