#1/usr/bin/python3
def add_argv(argv):
    n = len(argv) - 1
    
    if n == 0:
        print('{:d}'.format(n))
        return
    
    else:
        
        total = 0
        
        for i in range(1,n):
            total += int(argv[i])

        print('sum of variables: {:d}'.format(total))

if __name__ == '__main__':
    import sys
    add_argv(sys.argv)
