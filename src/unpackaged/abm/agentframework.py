# -*- coding: utf-8 -*-
"""agentframework
Created on Fri Nov 15 16:27:38 2019

@author: leechiyan
"""
import random


class Agent(object):
    def __init__ (self,environment, agents, neighbourhood, y, x):
        self.y = y
        self.x = x
        self.environment = environment
        self.store = 0
        self.agents=agents
        self.neighbourhood=neighbourhood
        if (x == None, y == None):
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)
        else:
            self.x = x
            self.y = y

    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 99
        else:
            self.y = (self.y - 1) % 99

        if random.random() < 0.5:
            self.x = (self.x + 1) % 99
        else:
            self.x = (self.x - 1) % 99
  
    def eat(self):# can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
            #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


