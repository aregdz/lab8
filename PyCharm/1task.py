#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    a = tuple(map(int, input().split()))

    # Найти одинавовые соседние элементы
    l = 0
    for i, item in enumerate(a):
        if i < len(a)-1:
            if item == a[i+1]:
                l = i +2
                break
        else:
            break

    # вывести элементы от l до конца
    print(a[l:])
