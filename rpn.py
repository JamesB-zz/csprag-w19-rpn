#!/usr/bin/env python3

import operator

from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
            print
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            col2 = 'magenta' if arg2<0 else 'white'
            arg1 = stack.pop()
            col1 = 'magenta' if arg1<0 else 'white'
            result = function(arg1, arg2)
            colres = 'red' if result<0 else 'white'
            text = colored(arg1,col1) + colored(token,'yellow') + colored(arg2, col2) + colored('=', 'green') + colored(result,colres)
            print(text)
            stack.append(result)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    print(colored('Welcome to the PRN calculator!', 'blue'))
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", colored(result, 'cyan'))

if __name__ == '__main__':
    main()
