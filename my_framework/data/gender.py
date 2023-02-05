import json


class Gender:
    def __init__(self, **kwargs):
        self.count = 168019 if 'count' not in kwargs.keys() else kwargs['count']
        self.gender = 'male' if 'gender' not in kwargs.keys() else kwargs['gender']
        self.name = 'Igor' if 'name' not in kwargs.keys() else kwargs['name']
        self.probability = 1.0 if 'probability' not in kwargs.keys() else kwargs['probability']

    @classmethod
    def create_from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def update_dict(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)

    def get_dict(self):
        return json.loads(self.__dict__)
