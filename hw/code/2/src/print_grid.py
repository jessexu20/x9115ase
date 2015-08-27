import do_twice as t
def print_inline(str):
    print str,
def do_three(f,str1,str2,col):
    for i in range(col):
        f(str1)
        t.do_four(f,str2)
    f(str1)
def print_grid(row,col):
    for i in range(row):
        do_three(print_inline,"+ ","- ",col)
        print
        for i in range(4):
            do_three(print_inline,"/ ","  ",col)
            print
    do_three(print_inline,"+ ","- ",col)
print_grid(8,8)