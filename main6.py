from collections import OrderedDict, deque

import numpy as np
from itertools import islice


class Tree(object):
    def __init__(self, left: 'Tree', right: 'Tree', value: str) -> None:
        self.left = left
        self.right = right
        self.value = value

    def lookup(self, value, counter=0):
        if value == self.value:
            return self, counter+1
        elif value < self.value:
            if not self.left:
                return None, counter+1
            return self.left.lookup(value, counter=counter+1)
        else:
            if not self.right:
                return None, counter+1
            return self.right.lookup(value, counter=counter+1)

    @staticmethod
    def printTree(root):
        buf = deque()
        output = []
        if not root:
            print('$')
        else:
            buf.append(root)
            count, nextCount = 1, 0
            while count:
                node = buf.popleft()
                if node:
                    output.append(node.value)
                    count -= 1
                    for n in (node.left, node.right):
                        if n:
                            buf.append(n)
                            nextCount += 1
                        else:
                            buf.append(None)
                else:
                    output.append('$')
                if not count:
                    print(output)
                    output = []
                    count, nextCount = nextCount, 0
            # print the remaining all empty leaf node part
            output.extend(['$'] * len(buf))
            print(output)


def createTree(root, i, j, keys):
    if i <= j:
        left = createTree(root, i, int(root[i][j] - 1), keys)
        right = createTree(root, int(root[i][j] + 1), j, keys)
        root_node = Tree(left, right, keys[int(root[i, j])])
        return root_node
    else:
        return None


def optimal_bst(p: list, q: list, n: int, keys: list) -> (list, list):
    e = np.zeros([n + 1, n + 1])
    w = np.zeros([n + 1, n + 1])
    root = np.zeros([n, n])

    e = np.diag(q)
    w = np.diag(q)

    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l
            e[i][j] = np.inf
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j):
                t = e[i, r] + e[r + 1, j] + w[i, j]
                if t < e[i, j]:
                    e[i, j] = t
                    root[i, j - 1] = r
    tree = createTree(root, 0, n - 1, keys)
    Tree.printTree(tree)
    node, counter = tree.lookup('f')
    if not node:
        print('Node not found, counter: {}'.format(counter))
    else:
        print('Node: {}, counter: {}'.format(node.value, counter))

def main():
    data = {}
    data_upper_50000 = {}
    total_freq = 0
    p = [None]
    q = []
    with open('test.txt') as file:
        for line in file.readlines():
            freq, key = line.strip().split(' ')
            freq = int(freq)
            data[key] = freq
            if freq > 0:
                data_upper_50000[key] = freq
            total_freq += freq
    lexi_ordered_data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
    keys_list = list(lexi_ordered_data.keys())
    lexi_ordered_data_upper_50000 = OrderedDict(sorted(data_upper_50000.items(), key=lambda t: t[0]))
    previous_key = None
    for key, value in lexi_ordered_data_upper_50000.items():
        p.append(value / total_freq)
        if previous_key:
            sum_of_dummy = sum(list(islice(lexi_ordered_data.values(), keys_list.index(previous_key) + 1, keys_list.index(key))))
        else:
            sum_of_dummy = sum(list(islice(lexi_ordered_data.values(), 0, keys_list.index(key))))
        q.append(sum_of_dummy / total_freq)
        previous_key = key
    sum_of_dummy = sum(list(islice(lexi_ordered_data.values(), keys_list.index(previous_key) + 1, None)))
    q.append(sum_of_dummy / total_freq)
    optimal_bst(p, q, len(lexi_ordered_data_upper_50000.keys()), list(lexi_ordered_data_upper_50000.keys()))


if __name__ == "__main__":
    main()
