##########################
##   _   _ _   _ _    
##  | | | | |_(_) |___
##  | |_| |  _| | (_-<
##   \___/ \__|_|_/__/
##                    
##########################

from .imports import *

def http_get_json(session: Session, url: str):
    response = session.get(url)
    return response.json()