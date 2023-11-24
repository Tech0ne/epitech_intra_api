##############################
##    ___ _ _         _   
##   / __| (_)___ _ _| |_ 
##  | (__| | / -_) ' \  _|
##   \___|_|_\___|_||_\__|
##                        
##############################

from .imports import *
from .globals import *
from .picture import *
from .utils import *

class Client:
    def __init__(self, token: str) -> None:
        self.token = token
        self.session = Session()
        self.session.cookies.set("user", self.token, domain="intra.epitech.eu")

        self.login = None

        self.profile = None
        self.pairs = []
        self.flags = {}

        self.get_profile(True)

    def get_profile(self, force_update = False) -> dict:
        if force_update or self.profile is None:
            self.profile = http_get_json(self.session, BASE_URL + "/user/?format=json")
        self.login = self.profile.get("login")

        if type(self.profile.get("picture")) == str:
            self.profile["picture"] = Picture(self.session, BASE_URL + self.profile["picture"])
        if type(self.profile.get("picture_fun")) == str:
            self.profile["picture_fun"] = Picture(self.session, BASE_URL + self.profile["picture_fun"])
                
        if type(self.profile.get("ctime")) == str:
            self.profile["ctime"] = datetime.strptime(self.profile.get("ctime"), "%Y-%m-%d %H:%M:%S")
        if type(self.profile.get("mtime")) == str:
            self.profile["mtime"] = datetime.strptime(self.profile.get("mtime"), "%Y-%m-%d %H:%M:%S")
        
        return self.profile
    
    def load_pairs(self) -> list:
        if self.login is None:
            raise ValueError("Could not retreive pairs without a login (Client.login, automaticly set after Client.get_profile)")
        self.pairs = http_get_json(self.session, BASE_URL + f"/user/{self.login}/binome?format=json").get("binomes")
        if self.pairs is None:
            self.pairs = []
            return self.pairs
        for i in range(len(self.pairs)):
            if type(self.pairs[i].get("picture")) == str:
                self.pairs[i]["picture"] = Picture(self.session, BASE_URL + self.pairs[i]["picture"])
    
    def load_flags(self) -> dict:
        if self.login is None:
            raise ValueError("Could not retreive flags without a login (Client.login, automaticly set after Client.get_profile)")
        self.flags = http_get_json(self.session, BASE_URL + f"/user/{self.login}/flags?format=json").get("flags")
        if self.flags is None:
            self.flags = {}
            return self.flags
        

    def __getattr__(self, __name: str):
        if self.profile is None:
            return None
        return self.profile.get(__name)
    
    def __getitem__(self, __name):
        if self.profile is None:
            return None
        return self.profile[__name]