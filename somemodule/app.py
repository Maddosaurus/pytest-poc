def main():
    print(do_some_print('Bar'))

def do_some_print(some):
    return('Foo {} Baz'.format(some))

if __name__ == '__main__':
    main()