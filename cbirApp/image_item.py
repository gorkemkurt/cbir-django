from dataclasses import dataclass
from numpy import double
import json


@dataclass
class ImageItem:
    name: str
    src: str
    score: double
    width: int
    height: int

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
