
r0 = 1
seq = [[r0]]
nodes = [1,2,3,4,5,6,7]
edges = [[1,2],[3,4],[3,5],[3,1],[6,5],[7,5]]

while len(nodes)>0:
    r = seq[len(seq)-1]
    x = []
    for ri in r:
        deli = nodes.index(ri)
        del(nodes[deli])
        i = 0
        while i<len(edges) :
            pair = edges[i]
            if pair[1]==ri:
                x.append(pair[0])
                
                deli = edges.index(pair)
                del(edges[deli])
                
            elif pair[0]==ri:
                x.append(pair[1])

                deli = edges.index(pair)
                del(edges[deli])
            else: i+=1
    if(len(x)>0):
        seq.append(x)
print(seq)
