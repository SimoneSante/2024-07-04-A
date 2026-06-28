from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph =nx.DiGraph()
        self._idMap={}

    def build_graph(self,c,b):
        self._graph.clear()
        self._idMap.clear()

        nodi=DAO.get_nodi(int(c),str(b))
        self._graph.add_nodes_from(nodi)
        for n in nodi:
            self._idMap[n.id]=n

        edges=DAO.get_archi(int(c),str(b))
        for a in edges:
            self._graph.add_edge(self._idMap[a[0]], self._idMap[a[1]])

    def get_stats(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def get_deb_conn(self):
        componenti = list(nx.weakly_connected_components(self._graph))
        return len(componenti)

    def top_connesse(self):
        lista = list(nx.weakly_connected_components(self._graph))

        if len(lista) == 0:
            return 0, []
        largest = max(lista, key=len)

        return len(lista), sorted(largest, key=lambda x: x.datetime)
    def get_anni(self):
        return list(DAO.get_all_years())
    def get_shape(self,c):
        return list(DAO.get_all_shape(c))
