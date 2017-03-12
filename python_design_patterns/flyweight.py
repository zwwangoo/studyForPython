# -*- coding: utf-8 -*-
'''
享元模式 2017-3-9
'''
import random


class TreeType:
    apple_tree = 1
    cherry_tree = 2
    peach_tree = 3


class Tree(object):
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print 'rander a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y)


def main():
    rnd = random.Random()
    age_main, age_max = 1, 30
    min_poit, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_main, age_max),
                  rnd.randint(min_poit, max_point),
                  rnd.randint(min_poit, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_main, age_max),
                  rnd.randint(min_poit, max_point),
                  rnd.randint(min_poit, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_main, age_max),
                  rnd.randint(min_poit, max_point),
                  rnd.randint(min_poit, max_point))
        tree_counter += 1

    print 'tree rendered: {}'.format(tree_counter)
    print 'tree actually created: {}'.format(len(Tree.pool))

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)

    print '{} == {} ? {}'.format(id(t4), id(t5), id(t4) == id(t5))
    print '{} == {} ? {}'.format(id(t5), id(t6), id(t6) == id(t5))


if __name__ == '__main__':
    main()
