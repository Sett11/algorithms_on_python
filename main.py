import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf,factorial
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back,sudoku,kad
from functools import reduce
from itertools import product,zip_longest,permutations
from copy import deepcopy
from operator import mul,add,sub,truediv,mod
from decimal import Decimal
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)
def fucken_indentations():
   ...

def tokenize(expression):
    if not expression:
        return []
    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

def is_number(d):
    p=re.compile(r"\A[-]?\d+(?:\.\d+)?\Z")
    return bool(p.search(d))

class Environment(dict):
    def __init__(self, operators = {}, functions = {}, variables = {}, keywords = {}):
        self.update(operators = operators, functions = functions, variables = variables, keywords = keywords)

class Func:
    def __init__(self, params, expr, interpreter):
        self.params, self.expr = params, expr
        self.env = Environment(interpreter.env["operators"], interpreter.env["functions"])
        self.ary = len(params)
        self.interp = interpreter

    def __call__(self, *args):
        self.env["variables"].update(zip(self.params, args))
        return self.interp.eval_postfix(self.interp.shunting_yard(self.expr, self.env), self.env)

class Interpreter:
    def __init__(self):
        variables = {}
        functions = {}
        operators = {
            "+":add,
            "-":sub,
            "*":mul,
            "/":truediv,
            "%":mod,
            "=": self._assign_var
        }
        keywords = ["fn"]
        self.env = Environment(operators, functions, variables, keywords)

    def input(self, expression):
        tokens = tokenize(expression)
        if not tokens:
            return ""
        if tokens[0] in self.env["keywords"]:
            if tokens[0] == "fn":
                new_fn_name = tokens[1]
                if new_fn_name in self.env["variables"]:
                    raise Exception("Cannot overwrite variable with function!")
                assign_op_index = tokens.index("=>")
                params = tokens[2:assign_op_index]
                if len(params) != len(set(params)):
                    raise Exception("Duplicate parameters specified!")
                expr = tokens[assign_op_index+1:]
                for token in expr:
                    if token.isalpha() and token not in params:
                        raise Exception("Function body contains unknown variables!")
                new_fn = Func(params, expr, self)
                self.env["functions"][new_fn_name] = new_fn
                return ""
        else:
            value = self.eval_expr(tokens)
        return value

    def eval_expr(self, tokens):
        return self.eval_postfix(self.shunting_yard(tokens))

    def _assign_var(self, name, value):
        if name in self.env["functions"]:
            raise Exception("Cannot overwrite function with variable!")
        self.env["variables"][name] = value
        return value

    def shunting_yard(self, expression, env = None):
        if env is None:
            env = self.env
        def precedence(operator):
            if operator == '+' or operator == '-':
                return 2
            elif operator == '*' or operator == '/' or operator == '%':
                return 3
            elif operator == "=":
                return 1
            else:
                raise Exception("%s is not a valid operator." % operator)
        def is_left_assoc(operator):
            if operator == "=":
                return False
            return True

        output = []
        operators = []
        for token in expression:
            if is_number(token):
                try:
                    output.append(int(token))
                except ValueError:
                    output.append(float(token))
            elif token in env["functions"]:
                operators.append(token)
            elif token in env["variables"]:
                output.append(token)
            elif token in env["operators"]:
                if operators and operators[-1] in env["operators"]:
                    o1 = token
                    o2 = operators[-1]
                    while operators and o2 in env["operators"] and ((is_left_assoc(o1) and precedence(o1) <= precedence(o2)) or (not is_left_assoc(o1) and precedence(o1) < precedence(o2))):
                        output.append(env["operators"][operators.pop()])
                        try:
                            o2 = operators[-1]
                        except IndexError:
                            break
                operators.append(token)
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(" and operators[-1] in env["operators"]:
                    output.append(env["operators"][operators.pop()])
                try:
                    operators.pop()
                except IndexError:
                    raise Exception("ERROR: Mismatched parentheses!")
                if operators and operators[-1] in env["functions"]:
                    output.append(env["functions"][operators.pop()])
            else:
                output.append(token)
        while operators:
            if operators[-1] in env["operators"]:
                output.append(env["operators"][operators.pop()])
            elif operators[-1] in env["functions"]:
                output.append(env["functions"][operators.pop()])
            else:
                raise Exception("Invalid function!")
        return output

    def eval_postfix(self, tokens, env = None):
        if env is None:
            env = self.env
        if tokens is None:
            return ""
        output = []
        for _, token in enumerate(tokens):
            if isinstance(token, (int,float)):
                output.append(token)
            elif isinstance(token, Func):
                try:
                    args = [env["variables"][output.pop()] if output[-1] in env["variables"] else output.pop() for _ in range(token.ary)]
                except IndexError:
                    raise Exception("ERROR: Incorrect number of arguments passed to function!")
                result = token(*args)
                output.append(result)
            elif callable(token):
                right = output.pop()
                left = output.pop()
                if right in env["variables"]:
                    right = env["variables"][right]
                if isinstance(right, str):
                    raise Exception("ERROR: Variable referenced before assignment!")
                if left in env["variables"] and token != env["operators"]["="]:
                    left = env["variables"][left]
                result = token(left, right)
                output.append(result)
            elif isinstance(token, str):
                output.append(token)
        if len(output) > 1:
            raise Exception("ERROR: Invalid syntax!")
        try:
            if output[0] in env["variables"]:
                return env["variables"][output[0]]
            elif isinstance(output[0], str):
                raise Exception("Undeclared variable referenced!")
            else:
                return output[0]
        except IndexError:
            return ""
        
I=Interpreter()
I.input("fn avg x y => (x + y) / 2")
print(I.input("avg 4 2"))