from ._base import BaseParser


class Books(BaseParser):
    def parse(self):
        container = self._html.find("c-wiz", jsrenderer="LRovxc")
        items = container.findAll("div", jscontroller="tKHFxf")
        for item in items:
            films_name = item.find("div", class_="Epkrse")
            films_price = item.select_one(".VixbEe")
            films_link = item.find("a")
            link = "https://play.google.com" + films_link.get("href")
            self._data.append({"Books name": films_name.text, "Price": films_price.text, "Link": link})


class Games(BaseParser):
    def parse(self):
        container = self._html.find("c-wiz", jsrenderer="LRovxc")
        items = container.findAll("div", jscontroller="tKHFxf")
        for item in items:
            game_name = item.find("div", class_="ubGTjb")
            game_category = item.find("span", class_="w2kbF")
            game_evaluation = item.select_one(" div:nth-child(3) > div > span > span.w2kbF")
            game_link = item.find("a")
            link = "https://play.google.com" + game_link.get("href")
            self._data.append({"Name of the game":game_name.text, "Category": game_category.text, "Rating": game_evaluation.text, "Link": link})


class Films(BaseParser):
    def parse(self):
        container = self._html.find("c-wiz", jsrenderer="LRovxc")
        items = container.findAll("div", jscontroller="tKHFxf")
        for item in items:
            films_name = item.find("div", class_="Epkrse")
            films_price = item.select_one(".VixbEe")
            films_link = item.find("a")
            link = "https://play.google.com" + films_link.get("href")
            self._data.append({"Films name": films_name.text, "Price": films_price.text, "Link": link})