import itertools
import numpy as np
from functools import partial
import sys
sys.path.append('../prompts/')
sys.path.append('../models/')
from gpt import gpt
from concept_recursion_prompt import user_prompt_5, user_prompt_10


def extract_children(text):
    '''
    Extract the children of a concept from the text. Each child is tagged by <object> and </object>
    '''
    children = []
    start = 0
    while True:
        start = text.find("<object>", start)
        if start == -1:
            break
        end = text.find("</object>", start)
        if end == -1:
            break
        children.append(text[start + len("<object>"):end])
        start = end + len("</object>")
    if len(children)>0:
        return children
    else:
        return None

def get_barebones_description(text):
    '''
    Strip off <object> </object> from the text
    '''
    start = 0
    while True:
        start = text.find("<object>", start)
        if start == -1:
            break
        end = text.find("</object>", start)
        if end == -1:
            break
        text = text[:start] + text[end + len("</object>"):]
        start = end + len("</object>")
    return text


class Concept(object):

    def __init__(self, name, parent=None, descriptions=[],children=[]):
        self.name = name
        self.parent = parent
        self.descriptions = descriptions
        self.children = children
    
    def get_op(self, n_shot, model="gpt-3.5-turbo", n=3, temperature=0.7, max_tokens=1000,stop=None):

        assert n_shot in [5,10]
        if n_shot == 5:
            prompt = user_prompt_5.format(self.name)
        elif n_shot == 10:
            prompt = user_prompt_10.format(self.name)
        
        op = gpt(prompt, model=model, temperature=temperature, max_tokens=max_tokens, stop=stop, n=n)

        return op
        
    def explore_concept(self, n_shot, model="gpt-3.5-turbo", n=3, temperature=0.7, max_tokens=1000, stop=None):
        '''
        Explore a concept by generating descriptions of it
        '''
        ops = self.get_op(n_shot, model=model, n=n, temperature=temperature, max_tokens=max_tokens, stop=stop)
        all_children = []
        for op in ops: 
            self.descriptions.append(get_barebones_description(op))
            children = extract_children(op)
            if children is not None:
                all_children.extend(children)
            
        self.children = list(set(all_children))
        for child in self.children:
            print('For parent {}, found child: {}'.format(name,child))
        return self.descriptions, self.children
    
class ConceptTree(object):

    def __init__(self, root):
        self.root = Concept(root,parent=None)
        self.concepts = [self.root]

    def recurse_tree(self,depth=3,n_shot=5):
        '''
        Recurse the concept tree to a certain maximum depth
        '''
        #bfs
        queue = [self.root]
        for i in range(depth):
            if len(queue) == 0:
                break
            new_queue = []
            for concept in queue:
                descriptions, children = concept.explore_concept(n_shot=n_shot)                
                self.concepts.append(concept)
                for child in children:
                    new_queue.append(Concept(child, parent=concept))
            queue = new_queue
        return self.concepts


