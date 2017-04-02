import sys


def main():
    while True: 
        n = sys.stdin.readline().rstrip('\n')
        if n == 'EXIT':
            break
        elif n == 'SET':
            sys.stdout.write('IT WAS SET\n')
    

if __name__ == "__main__":
    main()
