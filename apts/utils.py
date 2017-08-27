def find_all_paths(graph, start, end, mode = 'OUT', maxlen = None):
  def find_all_paths_aux(adjlist, start, end, path, maxlen = None):
      path = path + [start]
      if start == end:
          return [path]
      paths = []
      if maxlen is None or len(path) <= maxlen:
          for node in adjlist[start] - set(path):
              paths.extend(find_all_paths_aux(adjlist, node, end, path, maxlen))
      return paths
  adjlist = [set(graph.neighbors(node, mode = mode))
      for node in range(graph.vcount())]
  all_paths = []
  start = start if type(start) is list else [start]
  end = end if type(end) is list else [end]
  for s in start:
      for e in end:
          all_paths.extend(find_all_paths_aux(adjlist, s, e, [], maxlen))
  return all_paths 
