import flet as ft

class resources(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        def go_to_startup(e):
            page.go("/startup")

        #page.window_center()

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Online resources", color="black", size=30, weight=ft.FontWeight.BOLD),
                            ft.ElevatedButton("Back to Startup", on_click=go_to_startup)
                        ]
                    )
                )
            ]
        )
