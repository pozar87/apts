def find_all_paths(graph, start, end, mode="OUT", maxlen=None):
    import networkx as nx

    start_nodes = start if isinstance(start, list) else [start]
    end_nodes = end if isinstance(end, list) else [end]

    for s in start_nodes:
        for e in end_nodes:
            # networkx.all_simple_paths cutoff is in edges,
            # so maxlen-1 if maxlen is the number of nodes.
            cutoff = maxlen - 1 if maxlen is not None else None
            try:
                # Return generator instead of list to save memory and time
                yield from nx.all_simple_paths(graph, s, e, cutoff=cutoff)
            except nx.NodeNotFound:
                continue
