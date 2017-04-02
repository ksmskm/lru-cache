import sys
from lru import LRUCache


def main():
    sys.stdout.write('SIZE ')
    n = sys.stdin.readline().rstrip('\n')
    try:
        n = int(n)
    except:
        sys.stdout.write('ERROR\n')
        return

    cache = LRUCache(int(n))
    sys.stdout.write('SIZE OK\n')

    while True: 
        command = sys.stdin.readline().rstrip('\n')
        if command == 'EXIT':
            break

        command_args = command.split(' ')
        if len(command_args) == 3 and command_args[0] == 'SET':
                key = command_args[1]
                val = command_args[2]
                cache.set(key, val)
                sys.stdout.write('SET OK\n')
        elif len(command_args) == 2 and command_args[0] == 'GET':
                key = command_args[1]
                item = cache.get(key)
                if item:
                    sys.stdout.write('GOT %s\n' % item)
                else:
                    sys.stdout.write('NOTFOUND\n')
        else:
            sys.stdout.write('ERROR\n')
            

if __name__ == "__main__":
    main()
