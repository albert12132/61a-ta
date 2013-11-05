from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Higher-Order Functions'
level = 'exam'

references = [
    ('Lecture: Higher-Order Functions',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/04-HoF_1pps.pdf'),
    ('Lab 2',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab02/lab02.php'),
    ('Discussion 2',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion02.pdf'),
]

notes = ''

contents = [
    {'name': 'Environment Diagrams',
     'id': 'env',
     'maker': make_env_question,
     'questions': lambda: env_questions},
]

env_questions = [
    {
        'code': """
def f(x):
    return lambda y: x(y)

def g(x):
    return lambda : f(x) + f(y)

y = 2
result = f(g(f))""",
    },
    {
        'code': """
def always_roll(n):
    return lambda s0, s1: n

def make_bad_strategy(p):
    def strategy(s0, s1):
        # next line is bad style!
        return always_roll(1 - p)(s0, s1)
    return strategy

num_rolls = make_bad_strategy(1)(50, 50)""",
    },
    {
        'code': """
def test(fn):
    def new_fn(x):
        if x > 10:
            return new_fn(x % 10)
        else:
            return fn(x)
    return new_fn
x = 10
new = test(lambda score: score - x)
new(42)""",
    },
    {
        'code': """
x = 4
def foo(foo):
    def bar(y):
        y += foo
        return lambda : y + x
    foo += 3
    return bar
x = 5
foo(5)(4)()""",
    },
    {
        'code': """
def dream1(f):
    kick = lambda x: mind()
    def dream2(secret):
        mind = f(secret)
        kick(2)
    return dream2

inception = lambda secret: lambda: secret
real = dream1(inception)(42)""",
    },
    {
        'code': """
def albert(albert):
    albert = albert()
    def albert():
        albert = lambda albert: albert
        return albert(albert)
    return albert

albert(lambda: albert)()""",
    },
]

eval_output_question = [
    {
        'code': """
def new(year):
    sign = 'snake'
    def red(env):
        if env == year:
            return sign
        else:
            return new
    return red

new, foo = lambda x: x * x, new
""",
    'prompts': [
        """foo(2013)""",
        """foo(new)""",
        """foo(new(4))(16)""",
        """foo(11)(11)""",
        """foo(2)(4)(2)""",
        ]
    },
]

eval_output_solutions = [
    {'prompts': [
        'foo(2013)',
        'foo(new)',
        'foo(new(4))(16)',
        'foo(11)(11)',
        'foo(2)(4)(2)',
    ], 'answers': [
        {'eval': 'FUNC',
         'output': 'FUNC'},
        {'eval': 'FUNC',
         'output': 'FUNC'},
        {'eval': "'snake'",
         'output': "'snake'"},
        {'eval': "'snake'",
         'output': "'snake'"},
        {'eval': '4',
         'output': '4'},
    ]},
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

