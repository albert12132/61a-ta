import re
import html
from urllib.parse import quote_plus

def make_counter():
    i = 0
    def count():
        nonlocal i
        ret = i
        i += 1
        return ret
    return count

question_re = re.compile(r"""
    <\s*question(?:\s+(.+?))?\s*>
""", re.X | re.S)
q_count = make_counter()
def question_sub(match):
    name = match.group(1) if match.group(1) else ''
    return '<h3 class="question" id="q{0}">Question {0}: {1}</h3>'.format(q_count() + 1, name)

solution_re = re.compile(r"""
    <\s*solution\s*>
    (.*?)
    </\s*solution\s*>
""", re.X | re.S)
s_count = make_counter()
def solution_sub(match):
    text = """
    <button id='{0}' class='toggleButton'>
    Toggle Solution<noscript> (enable JavaScript)</noscript>
    </button>

    <div class="solution {0}">{1}</div>
    """.format(s_count(), match.group(1))
    return text

wwpp_re = re.compile(r"<wwpp>\s*<pre><code>(.*?)\s*</code></pre>\s*</wwpp>", re.S)
toggle_re = re.compile(r"""
    ^
    (?!(?:&gt;){3}[ ])
    (?!\.{3}[ ])
    (.*)$
""", re.X | re.M)
def wwpp_sub(match):
    s_num = s_count()
    prompts = '<pre><code>' + toggle_re.sub(
        lambda m: """<span class="blank{0}">______</span><span class="hidden solution {0}">{1}</span>""".format(s_num, m.group(1)),
        match.group(1)) + '</code></pre>'

    text = """
    {0}

    <button id='{1}' class='toggleButton'>
    Toggle Solution<noscript> (enable JavaScript)</noscript>
    </button>
    """.format(prompts, s_num)
    return text

env_re = re.compile(r"<env>\s*<pre><code>(.*?)\s*</code></pre>\s*</env>", re.S)
def env_sub(match):
    tutor_url = 'http://www.pythontutor.com/iframe-embed.html'
    tutor_url += '#mode=display&cumulative=true&py=3&code='
    tutor_url += quote_plus(html.unescape(match.group(1)))

    text = """<pre><code>{0}</code></pre>

    <button id='{1}' class='toggleButton'>
    Toggle Solution<noscript> (enable JavaScript)</noscript>
    </button>
    <div class="solution {1}>
    <iframe width="900" height="500" frameborder="0" src="{2}">
    </iframe>
    </div>
    """.format(match.group(1), s_count(), 
    return text


topic_re = re.compile(r"<topic>(.*) :: (.*)</topic>")
def topic_sub(match):
    return """
    <tr>
      <td>{0}</td>
      <td><a href="{1}/basic/">Questions</td>
      <td><a href="{1}/exam/">Questions</td>
    </tr>
    """.format(match.group(1), match.group(2))

regexes = [
    (question_re, question_sub),
    (solution_re, solution_sub),
    (wwpp_re, wwpp_sub),
    (topic_re, topic_sub),
]

configs = {
}