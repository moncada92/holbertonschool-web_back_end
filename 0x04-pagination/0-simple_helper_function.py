#!/usr/bin/env python3
""" simple helper """


def index_range(*args, **kwargs):

    if (args):
        first = (args[0] * args[1]) - args[1]
        second = args[0] * args[1]
        return (first, second)

    elif (kwargs):
        print(kwargs['page'])
        first = (kwargs['page'] * kwargs['page_size']) - kwargs['page_size']
        second = kwargs['page'] * kwargs['page_size']
        return (first, second)
