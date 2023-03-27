class User:
    def __init__(self, name):
       self._name = name

    def get_name(self):
        return self._name

    name = property(get_name)

class Superlative:
    def __init__(self, name, create_date):
        if isinstance(name, str):
           self._name = name
        else: print("Superlative must be a string")

        # if isinstance(create_date, str):
        #    self._create_date = SOME FUNCTION THAT PULLS IND ATE

    def get_name(self):
        return self._name
        
    name = property(get_name)

    # def get_create_date(self):
    #     return self._create_date
    # phone = property(get_create_date)

class Votes:
    def __init__(self, superlative_id, candidate_id):
        self._superlative_id = superlative_id
        self._candidate_id = candidate_id
    
    def get_superlative_id(self):
        return self._superlative_id

    superlative = property(get_superlative)

    def get_candidate_id(self):
        return self._candidate_id

    candidate_id = property(get_candidate_id)
