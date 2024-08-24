import flet as ft
from flet import *
from utils.utils import MainNavBar, get_userresults


def profile_view(page: ft.Page):
    page.title = "Profile"
    page.bgcolor = "#0D0431"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    user = page.session.get('user_data')
    data = get_userresults(page, user['token'])
    print(user['username'])
    page.navigation_bar = MainNavBar(page)
    if data is False:
        page.add(
            Container(
                border_radius=20,
                border=border.all(2, colors.with_opacity(0.2, "#FFFFFF")),
                bgcolor=colors.with_opacity(0.09, "#FFFFFF"),
                alignment=alignment.center,
                width=page.window_width * 0.9,
                height=page.window_height * 0.5,
                content=Row(
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text(
                            "شما هیچ سابقه بازی ای ندارید",
                            style=TextStyle(
                                size=28,
                                color='white',
                                font_family='yekan'
                            )
                        )
                    ]
                )
            )
        )
    else:
        page.add(
            Stack(
                alignment=alignment.center,

                clip_behavior=ClipBehavior.NONE,
                controls=[

                    Container(
                        content=Column(
                            [
                                Container(
                                    height=150
                                ),
                                Text(
                                    "امتیاز کل",
                                    style=TextStyle(
                                        size=28,
                                        weight=FontWeight.BOLD,
                                        font_family="yekan"
                                    )
                                ),
                                Container(
                                    height=10
                                ),
                                ft.Stack(
                                    controls=[
                                        ft.ProgressRing(
                                            width=120,
                                            height=120,
                                            stroke_width=10,
                                            value=int(data['percent']),
                                            color="#12A505",
                                            bgcolor="#BDBDBD"
                                        ),

                                        ft.Container(
                                            content=Row(
                                                vertical_alignment=MainAxisAlignment.CENTER,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Text(
                                                        f'{int(data['percent'])}',
                                                        style=TextStyle(
                                                            size=42,
                                                            font_family='yekan',
                                                            weight=FontWeight.BOLD
                                                        ),
                                                        text_align=ft.TextAlign.CENTER,
                                                    ),
                                                    Text("%", size=18)
                                                ]
                                            ),
                                            alignment=ft.alignment.center,
                                            width=118,
                                            height=118
                                        )
                                    ],
                                    width=118,
                                    height=118
                                ),
                                Container(
                                    height=10
                                ),
                                Container(
                                    padding=ft.Padding(left=15, right=15, bottom=0, top=0),
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            Divider(
                                                thickness=1.5, color=colors.with_opacity(0.5, "#8D8D8D"),
                                            ),
                                            Row(
                                                height=100,
                                                alignment=MainAxisAlignment.CENTER,
                                                vertical_alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Container(
                                                        expand=1,
                                                        content=Column(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            horizontal_alignment=MainAxisAlignment.CENTER,
                                                            controls=[
                                                                Row(
                                                                    alignment=MainAxisAlignment.CENTER,
                                                                    vertical_alignment=MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        Text(
                                                                            f'{data['wrong']}',
                                                                            style=TextStyle(
                                                                                size=40,
                                                                                font_family='yekan',
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                Row(
                                                                    alignment=MainAxisAlignment.CENTER,
                                                                    vertical_alignment=MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        Text(
                                                                            "سوالات غلط",
                                                                            style=TextStyle(
                                                                                size=20,
                                                                                font_family='yekan',
                                                                                color="#AAAAAA",
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),

                                                            ]
                                                        ),
                                                        alignment=alignment.center
                                                    ),
                                                    ft.VerticalDivider(thickness=1.5),
                                                    Container(
                                                        expand=1,
                                                        content=Column(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            horizontal_alignment=MainAxisAlignment.CENTER,
                                                            controls=[
                                                                Row(
                                                                    alignment=MainAxisAlignment.CENTER,
                                                                    vertical_alignment=MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        Text(
                                                                            f'{data['current']}',
                                                                            style=TextStyle(
                                                                                size=40,
                                                                                font_family='yekan',
                                                                                weight=FontWeight.BOLD
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                Row(
                                                                    alignment=MainAxisAlignment.CENTER,
                                                                    vertical_alignment=MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        Text(
                                                                            "سوالات درست",
                                                                            style=TextStyle(
                                                                                size=20,
                                                                                font_family='yekan',
                                                                                color="#AAAAAA",
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),

                                                            ]
                                                        ),
                                                        alignment=alignment.center
                                                    ),
                                                ]
                                            ),
                                            Divider(
                                                thickness=1.5, color=colors.with_opacity(0.5, "#8D8D8D"),
                                            ),
                                            Container(
                                                border_radius=12,
                                                height=80,
                                                border=border.all(2, colors.with_opacity(0.2, "#FFFFFF")),
                                                bgcolor=colors.with_opacity(0.09, "#FFFFFF"),
                                                alignment=alignment.center,
                                                content=Column(
                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=MainAxisAlignment.CENTER,
                                                    controls=[
                                                        Row(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            vertical_alignment=MainAxisAlignment.CENTER,
                                                            controls=[
                                                                Text(
                                                                    '{} {}'.format(user['first_name'],
                                                                                   user['last_name']),
                                                                    rtl=True,
                                                                    text_align=TextAlign.CENTER,
                                                                    style=TextStyle(

                                                                        size=20,
                                                                        font_family='yekan'
                                                                    ),

                                                                ),
                                                            ]
                                                        ),
                                                        Row(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            vertical_alignment=MainAxisAlignment.CENTER,
                                                            controls=[
                                                                Text(
                                                                    '{}'.format(user['email']),
                                                                    text_align=TextAlign.CENTER,
                                                                    style=TextStyle(
                                                                        size=20,
                                                                        color="#B5B5B5",
                                                                        font_family='yekan'
                                                                    ),

                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                )

                            ],
                            alignment="start",
                            horizontal_alignment="center"
                        ),
                        border_radius=20,
                        border=border.all(2, colors.with_opacity(0.2, "#FFFFFF")),
                        bgcolor=colors.with_opacity(0.09, "#FFFFFF"),
                        alignment=alignment.center,
                        width=page.window_width * 0.8,
                        height=page.window_height * 0.73,

                    ),
                    Image(
                        f'{user['profile_image']}',
                        width=200,
                        height=200,
                        top=-50,
                        left=60,
                        border_radius=15,
                    )
                ]
            )

        )
