import flet as ft
from ui import UI
from controller import Controller

def main(page: ft.Page):
    ui = UI(page)
    controller = Controller(ui)
    ui.process_project = controller.process_project
    ui.query_embeddings = controller.query_embeddings

ft.app(target=main)