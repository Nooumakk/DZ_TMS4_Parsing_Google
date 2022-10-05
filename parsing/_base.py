import requests
from abc import ABC, abstractmethod
import json
from bs4 import BeautifulSoup as Bs


class BaseParser:
    _user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"
    

    def __init__(self, url):
        self._url = url
        
        
    def get_data(self):
        self._data = []
        data = requests.get(self._url, headers={"user_agent": self._user_agent})
        if data.status_code == 200:
            self._html = Bs(data.text, features= "lxml")
            return
        raise RuntimeError("Invalid data: status={}, text={}".format(data.status_code, data.text))


    @abstractmethod
    def parse(self):
        ...
    
    def save(self, file_name):
        with open(file_name, "w") as file:
            file.write(json.dumps(self._data, indent=4, ensure_ascii=False))