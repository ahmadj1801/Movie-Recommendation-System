import urllib
from urllib.request import urlopen

import simplejson
import io


class Google:
    __query = ''

    def __init__(self):
        pass

    def __init__(self, search_param):
        self.__query = search_param
        self.download_image()

    def download_image(self):

        try:
            pass
        except FileNotFoundError:
            print("DID NOT DOWNLOAD!!!")
            pass
