def do_twice(f,str):
    f(str)
    f(str)
def print_spam(str):
    print str


# do_twice(print_spam,"spam")

def do_four(f,str):
    do_twice(f,str)
    do_twice(f,str)

# do_four(print_spam,"four")
    
    
    