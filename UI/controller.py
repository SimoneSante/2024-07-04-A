import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_ddyear(self):
        self._view.ddyear.options.clear()
        self._view.ddyear.value = None
        lista=self._model.get_anni()
        for l in lista:
            self._view.ddyear.options.append(
                    ft.dropdown.Option(
                        key=str(l),
                        text=str(l),
                    )
                )
        self._view.update_page()


    def fill_ddshape(self,e=None):
        self._view.ddshape.options.clear()
        self._view.ddshape.value = None
        lista=self._model.get_shape(self._view.ddyear.value)
        for l in lista:
            self._view.ddshape.options.append(
                    ft.dropdown.Option(
                        key=str(l),
                        text=str(l),
                    )
                )
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result1.controls.clear()
        try:
            store = int(self._view.ddyear.value)
            k = str(self._view.ddshape.value)
        except ValueError:
            self._view.txt_result1.controls.append(ft.Text("selezionare entrambi gli anni"))
        if store is None or k is None:
            self._view.txt_result1.controls.append(
                ft.Text("selezionare entrambi i campi", color="red")
            )

        self._model.build_graph(store, k)
        stats = self._model.get_stats()
        self._view.txt_result1.controls.append(ft.Text(f"stats:{stats[0]} e {stats[1]}"))
        deb = self._model.get_deb_conn()
        k, listatop = self._model.top_connesse()
        self._view.txt_result1.controls.append(ft.Text(f" il grafo creato contiene {deb} debolmente connessi"))
        self._view.txt_result1.controls.append(ft.Text(f"la componente più grande ha {k} nodi"))
        for a in listatop:
            self._view.txt_result1.controls.append(ft.Text(f"{a.id},{a.city},{a.datetime}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
