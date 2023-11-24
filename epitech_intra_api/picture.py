####################
##
####################

from .imports import *

class Picture:
    def __init__(self, session: Session, url: str):
        self.session = session
        self.url = url
        self.content = self.session.get(url).content

        self.image = Image.open(StringIO(self.content))
        self.filename = url.split('/')[-1]