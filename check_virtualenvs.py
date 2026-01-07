import os
p = os.path.join(os.path.expanduser('~'), '.virtualenvs')
print('Path:', repr(p))
print('Exists:', os.path.exists(p))
if os.path.exists(p):
    print('Is file:', os.path.isfile(p))
    print('Is dir:', os.path.isdir(p))