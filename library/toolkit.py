import json


class Tool:
    def __init__(self, name, description, func, args, kwargs, input_type, output_type):
        self.name = name
        self.description = description
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.input_type = input_type
        self.output_type = output_type

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class ToolKit:

    def __init__(self):
        self.tools = {}

    def add_tool(self, name, description, func, args, kwargs, input_type, output_type):
        self.tools[name] = Tool(name, description, func, args, kwargs, input_type, output_type)

    def get_tool(self, name):
        return self.tools[name]


    def get_tools(self):
        return self.tools

    def save_tools(self, path):
        with open(path, "w") as f:
            json.dump(self.tools, f)

    def load_tools(self):
        



    

        
