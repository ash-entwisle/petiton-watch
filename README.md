# Depencencies

> requests `pip install requests`

# setup guide

 1. Open a terminal and cd into your project directory
 2. Run `git clone [url] .`
 3. Run `py -3 -m launcher.py`
 4. Enter the URL of the petition you want to monitor


# Disclaimer 

I have not commented the code as of yet. I may in future, but icba atm. 
`src.lib.rq` is a basic requests wrapper for what I need for this project. 
`src.lib.petitionwatcher` handles all the data gathering from the response. 
`src.lib.util` has all the utility functions and classes in that dont need there own module (such as log). 
That should be it. If anything is wrong, open a pull req or @ me on twitter 

