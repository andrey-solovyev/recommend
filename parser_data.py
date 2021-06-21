import pandas as pd
import models


class Parser:


    @staticmethod
    def deserialize(jsonData):
        objects = []
        data = jsonData
        for o in data:
            objects.append(
                models.Result(id=o['id'],text_twit= o['text_twitt'], person_id=o['person_id']))
        return objects
# [{
# "event_id": 0,
# "date_time": "string",
# "place": "string",
# "brief_description": "string",
# "full_description": "string"
# } ]
