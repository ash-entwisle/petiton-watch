from src.lib.util import log

keycode = [
    "TEST1",
    "TEST2"
]

def getsecret(code):
    log(f"fetching key ({code})")
    code = int(keycode.index(code))
    with open("./src/secrets/secrets.tkn", "r") as scr:
        return scr.readlines()[code]


