#!/usr/bin/env python3
import argparse


def parser_func():
    parser = argparse.ArgumentParser(
                    description='Draws a box from a given height and width!')
    parser.add_argument('height', metavar='h', type=int,
                        help='the height of the box')
    parser.add_argument('width', metavar='w', type=int,
                        help='the width of the box')
    return parser.parse_args()


def draw_box(h, w):
    for i in range(h):
        print('.', end='')
        for j in range(w - 1):
            print('.', end='')
        print()


def main():
    args = parser_func()
    draw_box(args.height, args.width)


if __name__ == '__main__':
    main()
