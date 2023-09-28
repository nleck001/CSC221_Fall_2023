'''
my_print3 module
Author: Ned Lecky
'''


def my_print3(*args, verbose=False, countem=False):
    if verbose:
        print(f'my_print3({args})')

    count = 0
    for arg in args:
        count += 1
        print(arg)

    if countem:
        print(f'count was {count} and {len(args)} was expected')


def a_whole_nother_function(x):
    print('a_whole_nother_function')


' Test Code runs unless you are importing me!'
if __name__ == '__main__':
    a = [3, 4, 5]
    my_print3(3, 5, a, 'ned')
    my_print3(3, 5.8, a, 'ned', verbose=True, countem=True)
