

def draw_grids(n):
    n=int(n)
    if n>0:
        p=(n-1)*5+1
        for i in range(p):
            if i%5==0:
                for j in range(p):
                    if j==p-1:
                        print '+'
                    elif j%5==0:
                        print '+',
                    else:
                        print '-',
            else:
                for j in range(p):
                    if j==p-1:
                        print '/'
                    elif j%5==0:
                        print '/',
                    else:
                        print ' ',

draw_grids(3)
draw_grids(4)
