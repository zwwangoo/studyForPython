import atexit

try:
    with open('counterfile') as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0


def incrcounter(n):
    global _count
    _count = _count + n


def savecounter():
    with open('counterfile', 'w') as outfile:
        outfile.write('%d' % _count)


atexit.register(savecounter)
