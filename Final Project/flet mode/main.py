import flet as ft
from router import views_handler

def main(page: ft.Page):

    padding=ft.padding.all(0)
    
    def route_change(route):
        page.views[-1] = views_handler(page)[page.route]
        page.update()


    page.on_route_change = route_change

    page.go("/startup")


ft.app(target=main)