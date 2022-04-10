import requests as rq
from src.lib.util import log


class GetReq():
    def __init__(self, url):
        #log("initialising connection...")
        # gets url to be used later
        self.url = url
        # makes HTTP request to url
        self.__data = rq.get(url)
        # checks if data is ok
        self.isok = self.__data.ok

        if self.isok:
            #log("connection established")
            # extracts status code from http req
            self.code = self.__data.status_code
            # checks if code == 404
            self.is404 = self.__isNotFound()
            # extracts html data from http req
            self._body = self.__data.text
            # extracts json data from http req
            self._json = self.__data.json()
        
        # makes sure connection is closed
        self.__data.close()

    # checks if status code is 404
    def __isNotFound(self):
        if self.code == 404:
            self.__data.close()
            return True
    
    def close(self):
        self.__data.close()

    
