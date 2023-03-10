# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#
#
# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
    return f"Hello {name}!"
# This type of string formatting does not work in codingbat.com
# maybe due to older version because it was introduced only in Python 3.6


# This is the OG of Python formatting and has been in the language since the very beginning.
def hello_name_1(name):
    old_v = "Hello {} !".format(name)
    return old_v

