from src.lib.util import log
from src.lib.rq import GetReq
from datetime import datetime
import json 


class PetitionWatcher(GetReq):
    def __init__(self, url: str):
        self.url = url
        super().__init__(self.checkifJSON())
        if self.isok:
            #log("getting data...")
            self._data = self._json["data"]
            self._attributes = self._data["attributes"]
            self.id = self._data["id"]
            self.title = self._attributes["action"]
            self.state = self._attributes["state"]
            self.signatures = self._attributes["signature_count"]
            self.creator = self._attributes["creator_name"]

    
    def checkifJSON(self):
        # checks if url is a json file
        if self.url.endswith(".json"):
            return self.url
        else:
            return f"{self.url}.json"

    def dumpJSON(self):
        log("Dumping JSON")
        timestamp = datetime.now().strftime("%H%M%S%Y%m%d")
        with open(f"./src/data/json/{timestamp}.json", "w") as f:
            json.dump(self._data, f)

