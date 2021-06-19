def hello():
    s = 'hi'  # s keeps a reference to 'hi' and have ownership
    print (s)   # use 'hi' for something
hello()       # s finishes and decreases the reference count