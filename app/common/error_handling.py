class AppErrorBaseClass(Exception):
    pass

class InvalidToken(Exception):
    pass


class ObjectNotFound(AppErrorBaseClass):
    def __init__(self, msg):
        raise 405