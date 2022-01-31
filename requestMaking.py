import requests


def Make_Map_Request(coords, zoom, type_of_map):  # coords - координаты, spn - увеличение, type_of_map - тип карты
    params = {"ll": ",".join([coords[0], coords[1]]),
              "z": str(zoom),
              "l": type_of_map}
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    return requests.get(map_api_server, params=params)
