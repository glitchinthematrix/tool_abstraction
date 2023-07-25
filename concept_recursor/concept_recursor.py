import itertools
import numpy as np
import json
from functools import partial
import sys
sys.path.append('../prompts/')
sys.path.append('../models/')
from gpt import gpt
from prompts import generate_concept_recursion_prompt


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
    Strip off string <object> and </object> from the text
    '''
    text = text.replace("<object>", "")
    text = text.replace("</object>", "")
    return text


class Concept(object):

    def __init__(self, name, parent=None, descriptions=[],children=[]):
       
        self.name = name
        self.parent = parent
        self.descriptions = descriptions
        self.children = children
    
    def get_op(self, model="gpt-3.5-turbo", n=1, temperature=1., max_tokens=1000,stop=None):
        '''
        Sample the language model to generate descriptions of the concept
        '''
        prompt = generate_concept_recursion_prompt(input=self.name, parent=self.parent)
        op = gpt(prompt, model=model, temperature=temperature, max_tokens=max_tokens, stop=stop, n=n)
        return op
        
    def explore_concept(self, model="gpt-3.5-turbo", n=1, temperature=1., max_tokens=1000, stop=None):
        '''
        Explore a concept by generating descriptions of it
        '''
        print('Exploring concept: {}'.format(self.name))
        ops = self.get_op(model=model, n=n, temperature=temperature, max_tokens=max_tokens, stop=stop)
        all_children = []
        for op in ops: 
            barebone_description = get_barebones_description(op)
            self.descriptions.append(barebone_description)
            children = extract_children(op)
            if children is not None:
                all_children.extend(children)           
        self.children = list(set(all_children))
        for child in self.children:
            print('Found child: {}'.format(child))
        return self.descriptions, self.children
    
class ConceptTree(object):

    def __init__(self, root):
        self.root = Concept(root,parent=None)
        self.concepts = [self.root]

    def recurse_tree(self,depth=3):
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
                descriptions, children = concept.explore_concept()
                print(descriptions)
                self.concepts.append(concept)
                for child in children:
                    new_concept = Concept(child,parent=concept.name,descriptions=[])
                    new_queue.append(new_concept)
            queue = new_queue
        return self.concepts
    
    def return_dictionary(self):
        '''
        Create a dictionary of concepts
        '''
        all_concepts = {}
        for concept in self.concepts:
            all_concepts[concept.name] = {}
            all_concepts[concept.name]['parent'] = concept.parent
            all_concepts[concept.name]['descriptions'] = concept.descriptions
            all_concepts[concept.name]['children'] = concept.children
        return all_concepts

def main():

    #some unit tests
    concept_tree = ConceptTree("television")
    concepts = concept_tree.recurse_tree(depth=3)
    all_concepts = concept_tree.return_dictionary()
    print(all_concepts)
    #save dictionary as json file
    with open('../logs/television.json', 'w') as fp:
        json.dump(all_concepts, fp)

if __name__ == "__main__":
    main()