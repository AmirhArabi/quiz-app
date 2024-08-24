import flet as ft
from router import route


def main(page: ft.Page):
    page.window_width = 400
    page.fonts = {
        'yekan': '/fonts/YekanBakhFaNum-Bold.ttf'
    }
    page.window_height = 870
    page.platform = "ios"
    page.padding = 10
    page.bgcolor = "#f1f1f1"
    page.on_route_change = lambda e: route(page)
    page.go(page.route)


ft.app(target=main, assets_dir='assets')

