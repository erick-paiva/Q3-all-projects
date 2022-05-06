
class InvalidOption(Exception):
    def __init__(self, status_code=400, msg=""):

        self.message = msg

        self.status_code = status_code
        
        
class InvalidValueTask(Exception):
    def __init__(self, status_code=400, msg=""):

        self.message = msg

        self.status_code = status_code