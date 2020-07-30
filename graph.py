import graphviz

def get_color(p, c):
    color='black'
    while not p.annotation():
        if p.label == 'if:True':
            return 'blue'
        elif p.label == 'if:False':
            return 'red'
        p = p.parents[0]
    return color

def get_peripheries(p):
    annot = p.annotation()
    if annot  in {'<start>', '<stop>'}:
        return '2'
    if annot.startswith('<define>') or annot.startswith('<exit>'):
        return '2'
    return '1'

def get_shape(p):
    annot = p.annotation()
    if annot in {'<start>', '<stop>'}:
        return 'oval'
    if annot.startswith('<define>') or annot.startswith('<exit>'):
        return 'oval'

    if annot.startswith('if:'):
        return 'diamond'
    else:
        return 'rectangle'


def to_graph(registry, arcs=[], comment='', get_shape=lambda n: 'rectangle', get_peripheries=lambda n: '1', get_color=lambda p,c: 'black'):
    graph = Digraph(comment=comment)
    for nid, cnode in registry.items():
        if not cnode.annotation():
            continue
        sn = cnode.annotation()
        graph.node(cnode.name(), sn, shape=get_shape(cnode), peripheries=get_peripheries(cnode))
        for pn in cnode.parents:
            gp = pn.get_gparent_id()
            color = get_color(pn, cnode)
            graph.edge(gp, str(cnode.rid), color=color)
    return graph
