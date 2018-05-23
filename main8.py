# -*- coding: utf-8 -*-
from networkx import DiGraph
from networkx.algorithms.components.strongly_connected import strongly_connected_components

def _graph(formulas):
    """Build the implication graph"""
    G = DiGraph()
    for formula in formulas:
        if len(formula) == 1:
            G.add_edge(-formula[0], formula[0])
            G.add_edge(-formula[0], formula[0])
        else:
            G.add_edge(-formula[0], formula[1])
            G.add_edge(-formula[1], formula[0])

    return G


def satisfiable(formulas, n):
    try:
        next(contradictory_variables(formulas, n))
        print("Nesplnitelna")
    except StopIteration:
        print("Splnitelna")


def contradictory_variables(formula, n, G=None):
    if not G:
        G = _graph(formula)

    # check if a and -a in the same component
    result = [None for i in range(n)]
    for component in strongly_connected_components(G):
        seen = set()
        for literal in component:
            v = abs(literal)
            if v in seen:
                yield v
            else:
                seen.add(v)
                if result[v - 1] is None:
                    result[v - 1] = 'PRAVDA' if literal > 0 else "NEPRAVDA"

    print(result)


def main():
    formulas = []
    with open('3_OK.txt') as f:
        nbvar, nbclauses = f.readline().rstrip().split(' ')
        nbvar = int(nbvar)
        for line in f.readlines():
            formula = [int(x) for x in line.rstrip().split(' ')[:-1]]
            formulas.append(formula)
    satisfiable(formulas, nbvar)


if __name__ == "__main__":
    main()
