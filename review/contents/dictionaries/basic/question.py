from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Dictionaries'
level = 'basic'

references = [
    ('Lecture: Lists and Dictionaries',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/slides/12-Lists_1pps.pdf'),
    ('Lab 4',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/lab/lab04/lab04.php'),
    ('Discussion 5',
     'http://www-inst.eecs.berkeley.edu/~cs61a/fa13/disc/discussion05.pdf'),
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker': make_concept_question,
         'questions': lambda: concept_questions},
        {'name': 'What would Python print?',
         'id': 'print',
         'maker': make_print_question,
         'questions': lambda: print_questions},
]

concept_questions = [
    {'description': """What type of objects can be used as keys for
        dictionaries? What type of objects can be used as values?""",
    'solution': """Any <b>immutable</b> object can be used as a key --
    this includes numbers, strings, and tuples. Mutable objects, such
    as lists and dictionaries, are not allowed to be used as keys.
    Anything can be used as a value, however."""
    },

    {'description': """How many objects can a single key map to?""",

    'solution': """A single key can only map on to one value. That
    value can, however, be a sequence like a tuple or a list, so you
    can effectively map to multiple things (but it still only counts
    as one value)."""
    },

    {'description': """Are dictionaries ordered?""",

    'solution': """Python dictionaries are not ordered. If you were to
    iterate through the dictionary, the order in which you iterate
    through them is not necessarily the ordre in which you added them.
    """
    },
]

print_questions = [
    {'prompts': [
        ("logins = {'albert': 'cs61a-tg'}",),
        ("logins['albert']", "'cs61a-tg'"),
        ("logins['cs61a-tg']", "KeyError"),
        ("logins['allen'] = None",),
        ("len(logins)", '2'),
        ("""for elem in logins:
...     print(elem)""", """allen
albert  # not necessarily in that order"""),
        ("""for key, value in logins.items():
...     print(key, value)""", """allen None
albert cs61a-tg # not necessarily in that order"""),
        ]},
]

code_questions = [
    {'description': """Question Description.""",
     'code': """
def foo(test):
    return 'this is a test'
""",
    'solution': 'hi'
    }
]

env_questions = [
    {'code': """
def code(test):
    return test
""",
'solution': 'hi',
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

