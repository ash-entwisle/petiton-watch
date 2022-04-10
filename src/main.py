from src.lib.util import log
from src.lib.petitionwatcher import PetitionWatcher as pw
import time

def main(url: str):
    req = pw(url)
    log(f"Petition ID: {req.id} by: {req.creator} status: {req.state}")
    log(f"Title: {req.title}")
    req.close()
    count = 0
    while True:
        if time.localtime().tm_sec %12 == 0:
            count += 1
            req = pw(url)
            log(f"Signatures: {req.signatures} ({req.signatures*100//100000}%) status: {req.state}")
            if count % 10 == 0:
                req.dumpJSON()
            req.close()
            time.sleep(11)