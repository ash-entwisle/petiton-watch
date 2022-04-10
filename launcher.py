from src.main import main
from src.lib.util import getInput, log

url = getInput("Enter URL")
if "https://petition.parliament.uk/archived/petitions/" in url or "https://petition.parliament.uk/petitions/" in url:
    log("Valid URL")
    main(url)
else:
    log("Invalid URL")