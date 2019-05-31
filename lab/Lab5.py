# -*- coding: utf-8 -*-
import pydot
import numpy.random as rand
import networkx as nx
from networkx.drawing.nx_pydot import write_dot


players_count = 2
tree_depth = 7


def get_tree(depth, players):
    tree = nx.balanced_tree(2, depth - 1)
    for i in range(2 ** (depth - 1) - 1, 2 ** depth - 1):
        wins = rand.randint(-10, 10, players)
        tree.nodes[i]['wins'] = [tuple(wins)]
    return tree


def induction(tree, parent, players, player=0):
    wins = []
    max_win = 0
    for subtree_root in tree[parent].keys():
        if 'wins' not in tree[subtree_root] and subtree_root > parent:
            induction(tree, subtree_root, players, (player + 1) % players)
            node_max_win = tree.nodes[subtree_root]['wins'][0][player]
            for win in tree.nodes[subtree_root]['wins']:
                if win[player] > node_max_win:
                    node_max_win = win[player]
            if not len(wins) or node_max_win == max_win:
                wins.extend(tree.nodes[subtree_root]['wins'])
                max_win = node_max_win
            elif node_max_win > max_win:
                wins = tree.nodes[subtree_root]['wins']
                max_win = node_max_win
        if len(wins):
            tree.nodes[parent]['wins'] = wins


def solve(tree, players):
    ways_ = []
    leafs = [name for name, node in tree.nodes.items() if 'wins' in node]
    induction(tree, 0, players)
    for leaf in leafs:
        if tree.nodes[leaf]['wins'][0] in tree.nodes[0]['wins']:
            ways_.append(nx.shortest_path(tree, 0, leaf))
    return ways_


def get_labels(tree):
    labels = {}
    for k, v in tree.nodes.items():
        wins_label = "\n" + "\n".join("/".join(str(x) for x in win) for win in v['wins']) if 'wins' in v else ""
        labels[k] = str(k) + wins_label
    return labels


def print_tree(tree, file_name, ways_):
    write_dot(tree, "tree.dot")
    graph = pydot.graph_from_dot_file("tree.dot")[0]
    graph.obj_dict['attributes']["size"] = '"10,10!"'
    graph.obj_dict['attributes']["dpi"] = "720"

    for k, v in get_labels(tree).items():
        node = graph.get_node(str(k))[0]
        node.set('label', v)
        node.set('fontsize', '32')

    colors_list = ['blue', 'green', 'red', 'yellow', 'brown', 'purple']
    for way in ways_:
        color = colors_list.pop(0)
        for i in range(len(way) - 1):
            edge = graph.get_edge(str(way[i]), str(way[i + 1]))[0]
            if not edge.get('color'):
                edge.set('color', color)
            else:
                graph.add_edge(pydot.Edge(way[i], way[i + 1], color=color))
    graph.write_png(file_name)


game = get_tree(tree_depth, players_count)
print_tree(game, 'graph.png', [])
ways = solve(game, players_count)
print_tree(game, 'solved_graph.png', ways)
