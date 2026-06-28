from model.modello import Model

def main():
    model = Model()

    c = 2004
    b="disk"

    print(f"Costruisco il grafo con c = {c,b}...")

    model.build_graph(c,b)
    n_nodi, n_archi = model.get_stats()

    print(f" il grafo creato contiene {n_nodi} nodes e {n_archi} edges")

    deb=model.get_deb_conn()
    k,listatop=model.top_connesse()
    print(f" il grafo creato contiene {deb} debolmente connessi")
    print(f"la componente èiù grande ha{k} nodi")
    for a in listatop:
        print(f"{a.id},{a.city},{a.datetime}")

if __name__ == "__main__":
    main()