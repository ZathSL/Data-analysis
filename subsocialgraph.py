import networkit as nk
import networkit.graph as graph
import networkit.community as cm
import pickle
import gzip


def get_list_nodes(p):
    l = []
    for person in p:
      print(person)
      l.append(users[person])

    return l

filebot = open("/media/sdc/lissandrello/data/bots.txt",'r')
persons = []
for line in filebot:
  print(line); print(str(line)[:-1])
  persons.append(str(line)[:-1])

f = gzip.open("userssocial.gz", 'rb')
users = pickle.load(f)

g = nk.graphio.EdgeListReader(separator=' ', firstNode=0, directed=True).read("/media/sdc/socialgraph.graph")

l1 = get_list_nodes(persons)
l2 = g.nodes()
difference = list(set(l2) - set(l1))
print(f'list of nodes: {l1}')

g2 = g.subgraphFromNodes(difference) #creo il nuovo grafo
print(f'#nodes: {g2.numberOfNodes()}, #edges: {g2.numberOfEdges()}')

#Scrittura del grafo
nodes = g2.nodes()
nodes.sort(reverse=False)
nk.graphio.EdgeListWriter(separator=' ', firstNode=nodes[0], bothDirections=True).write(g2, "/media/sdc/lissandrello/data/subsubsocialgraph.graph")
