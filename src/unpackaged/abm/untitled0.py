# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:40:00 2020

@author: leechiyan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:35:49 2019

@author: leechiyan
"""
import random
import operator
#Let's now look at an external library: matplotlib.pyplot. matplotlib.pyplot is used to plot data in graphs.
import matplotlib.pyplot
import agentframework
import environment
import matplotlib.animation 




def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
#make our agent coordinations change an arbitrary number of times
num_of_iterations=100
neighbourhood = 20
agents=[]
environment = environment.get_environment()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Let's create a list with num_of_agents agent coordinates.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood,y,x))

carry_on = True	

def update(frame_number):
    
    fig.clear()
    global carry_on
    
#Move the agents.    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        if random.random() < 0.1:
            carry_on = False
            print("stopping condition")  
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance=distance_between(agents_row_a, agents_row_b)
        
'''
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
'''
#Essentially the frames argument can be either a number, an iterable, or a generator function.
# interval controls the speed of the sheeps.

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=200)
matplotlib.pyplot.show()
'''
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=200)
    canvas.show()
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()
'''