import re
from collections import deque

import networkx
import itertools
from helpers.utils import get_puzzle_input
import matplotlib.pyplot as plt


# # Part 2
# test_input = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags."""
bag_count = 0
edgey_edges = []
for line in get_puzzle_input(7).splitlines():
    bags = re.findall(pattern=r"(\b(?:\S+\s+){2}(?:bag))", string=line)
    if "no other bag" in bags:
        continue
    numbers = re.findall(pattern=r"(\b\d)", string=line)
    edges = list(itertools.combinations(bags, 2))
    edges = edges[:len(bags) - 1]
    for ind, number in enumerate(numbers):
        edges[ind] = (*edges[ind], int(number))
    edgey_edges.extend(edges)
graph = networkx.DiGraph()
graph.add_weighted_edges_from(edgey_edges)
a = {x[0] for x in networkx.edge_dfs(graph,'shiny gold bag', orientation='reverse')}

# networkx.draw(graph, with_labels=True)
# plt.savefig("bags_graph.png")
def count_downstream(bag, g=graph):
    """
    I do not understand recursion
    Parameters
    ----------
    bag: str
        the bag to look for
    g: networkx.Graph
        The graph of the bag lookups

    Returns
    -------

    """
    count = 0
    dequey = deque()

    def count_bag(b):
        nonlocal count
        for node, attrs in g[b].items():
            n = attrs['weight']
            dequey.extend([node] * n)
            count += n

    count_bag(bag)
    while dequey:
        count_bag(dequey.popleft())
    return count


part_2 = count_downstream("shiny gold bag", graph)