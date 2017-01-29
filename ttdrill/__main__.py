import argparse
import getch
import random
import sys

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default='1234567890_+=-!jk', required=False)
    parser.add_argument('--aggressiveness', type=int, default=5, required=False)

    configuration = parser.parse_args()
    source = configuration.source
    aggressiveness = configuration.aggressiveness
    length = 3

    pattern = ''
    attempt = ''

    def init():
        nonlocal attempt
        nonlocal pattern

        attempt = ''
        pattern = ''.join(random.choice(source) for x in range(length))
        print(pattern)

    init()

    print('running module ttdrill', configuration.aggressiveness, pattern)

    while True:
        c = getch.getch()
        attempt += c
        sys.stdout.write(c)

        if attempt == pattern:
            print('\n\nOK\n\n')
            length += 1
            init()

        if pattern.startswith(attempt):
            continue

        print('\n\nNOT OK\n» {} « vs \n» {} «\n'.format(attempt, pattern))

        missed = pattern[len(attempt) -1]
        if c in source:
            source += (c * aggressiveness)

        source += (missed * aggressiveness)
        length = max(1, length - 1)

        init()


if __name__ == '__main__':
    main()
