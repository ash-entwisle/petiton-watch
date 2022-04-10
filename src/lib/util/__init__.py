from datetime import datetime


def log(info, silent: bool = False):
    # gets current date and time
    timenow = datetime.now().strftime("%H:%M:%S")
    datenow = datetime.now().strftime("%Y-%m-%d")
    # opens log file for the day
    with open(f"./src/data/logs/{datenow}.log", "a") as logfile:
        # formats the input data
        data = f"[{timenow}] {info}"
        # writes data to file
        logfile.write(f"\n {data}")
        # outputs data to screen
        if not silent:
            print(data)


# input formatting
def getInput(txt: str):
    data = input(f"[--:--:--] {txt} >> ")
    log(f"{txt} >> {data}", silent=True)
    return data


# turns y/n into bool
def ynToTF(inp: str):
    if inp.upper() == "Y":
        return True
    else:
        return False


