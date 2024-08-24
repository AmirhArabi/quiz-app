import json

from flet import *
import requests


def MainNavBar(page):
    def change_route(e, page):
        print(page.route)
        routes = {'0': '', '1': 'profile_page', '2': 'leaderboard', '3': 'settings_page'}
        page.go('/{}'.format(routes[str(e.control.selected_index)]))

    route_to_index = {'/': 0, '/profile_page': 1, '/leaderboard': 2, '/settings_page': 3}

    current_route = page.route

    selected_index = route_to_index.get(current_route, 0)

    item = NavigationBar(
        bgcolor="transparent",
        height=60,
        width=300,
        expand=False,
        expand_loose=False,
        selected_index=selected_index,  # Use the selected_index
        elevation=0,
        label_behavior=NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
        on_change=lambda e: change_route(page=page, e=e),
        destinations=[
            NavigationDestination(icon=icons.HOME_OUTLINED, selected_icon=icons.HOME_ROUNDED, label="Home", ),
            NavigationDestination(icon=icons.PERSON_2_OUTLINED, selected_icon=icons.PERSON_ROUNDED, label="Profile"),
            NavigationDestination(icon=icons.BAR_CHART, label="LeaderBoard"),
            NavigationDestination(icon=icons.SETTINGS_OUTLINED, selected_icon=icons.SETTINGS_ROUNDED, label="Setting")
        ],
    )
    return item


def get_qustions(page, category):
    if category is None:
        category = "Earth"
    base_url = "http://127.0.0.1:8000/api/categories/{}/questions".format(category)
    user = page.session.get("user_data")
    print("user data", user)
    token = page.session.get("user_data")['token']
    headers = {
        "Authorization": token
    }
    req = requests.get(base_url, headers=headers)
    if req.status_code == 200:
        data = json.loads(req.text)
        return data
    else:
        print(req.status_code)


def get_userresults(page, token):
    base_url = "http://127.0.0.1:8000/api/userresult/"

    headers = {
        "Authorization": token
    }
    try:
        req = requests.get(base_url, headers=headers)
        req.raise_for_status()
        data = json.loads(req.text)
        if not data:
            raise ValueError("Data is empty")
        print('data', data[-1])
        return data[-1]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except ValueError as val_err:
        print(f"No data received: {val_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return False
