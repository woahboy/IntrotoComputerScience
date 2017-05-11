def make_hashtable(nbuckets):
    table = []
    [table.append([]) for i in range(nbuckets)]
    return table

print make_hashtable(3)
