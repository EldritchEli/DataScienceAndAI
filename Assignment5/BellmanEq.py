from random import shuffle
from enum import Enum
epsilon = 0.1
gamma =  0.9
delta = 0.2
from typing import List

class State:
    def __init__(self ,val, coord):
        self.val = val

        self.actions = []
        self.coord = coord

    def action_list_to_string(self):
        newlst = []
        for a in self.actions:
            newlst.append(str(a.coord))

        return ' '.join(newlst)


    def __str__(self):
        return "(" + str(self.get_x()) + ", " + str(self.get_y()) + ") has value: "+ str(self.val) + " and actions: " + str(self.action_list_to_string())

    def get_coord(self):
        return self.coord

    def get_x(self):
        return self.coord[0]

    def get_y(self):
        return self.coord[1]

    def get_val(self):
        return self.val

    def set_val(self, new_value):
        self.val = new_value

    def get_actions(self):
        return self.actions

    def add_action(self, state):
        self.actions.append(state)

    def get_max_action(self):
        greatest_state: State = None
        for a in self.actions:
            if greatest_state is None:
                greatest_state = a
            elif a.get_val() > greatest_state.get_val():
                greatest_state = a
        return greatest_state


def listcoord(rows, cols):
    return [(x ,y) for x in range(rows) for y in range(cols)]


def State_list(listval, listcoord, s_mod):
    state_list = []
    for v, c in zip(listval, listcoord):
        state_list.append(State(v ,c))
    for s in state_list:
        for t in state_list:
            abs_x = abs(s.get_x() - t.get_x())
            abs_y = abs(s.get_y() - t.get_y())
            if ((abs_y == 1 and abs_x == 0) ^ (abs_y == 0 and abs_x == 1)):
                s.add_action(t)
    return state_list


def print_action(states):
    for s in states:
        for a in s.get_actions():
            print(s, "goes to", a)
#0.8( 10 + 0.9 * 2) + 0.2(0 + 0.9 * 8)


def value_function(s: State):
    s_val = s.get_val()
    action_val = s.get_max_action().get_val()

    s.set_val((1-delta)*(s_val + gamma*action_val) + delta*(s_val + gamma*s_val))


#TODO add new generation values to new list so that they don't effect other states during current gen.
def new_Generation(s : List[State]):
    indexlist = [i for i in range(len(s))]
    shuffle(indexlist)
    for i in indexlist:
        tmp = s[i].get_val()
        s[i].val = value_function(s[i])
        s[i].set_last_val(tmp)






