""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import time


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# login credentials

# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    # session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    #get followers of "Popeye" and "Cinderella"
    popeye_followers = session.grab_followers(username="sephora", amount="full", live_match=True, store_locally=True)
    # time.sleep(600)
    # cinderella_followers = session.grab_followers(username="Cinderella", amount="full", live_match=True, store_locally=True)

    #find the users following "Popeye" WHO also follow "Cinderella" :D
    # popeye_cinderella_followers = [follower for follower in popeye_followers if follower in cinderella_followers]
