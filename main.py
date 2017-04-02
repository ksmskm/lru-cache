import sys
from lru import LRUCache
from pprint import pprint


def cachePrint(cache):
    for key, val in cache.items():
        print val
    print '==============='


def main():
    cache = LRUCache(5)
    cache.set('a', 'A')
    cache.set('b', 'B')
    cache.set('c', 'C')
    cache.set('d', 'D')
    cache.set('e', 'E')
    cache.set('f', 'F')
    cachePrint(cache.cache)
    cache.get('b')
    cache.set('g', 'G')
    # cachePrint(cache.cache)

    while True: 
        n = sys.stdin.readline().rstrip('\n')
        if n == 'EXIT':
            break
        elif n == 'SET':
            print cache.size
            sys.stdout.write('IT WAS SET\n')
    

if __name__ == "__main__":
    main()


