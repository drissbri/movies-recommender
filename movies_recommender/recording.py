class Recording:
    def __init__(self, idR, type, duration):
        self.__idR = idR
        self.__type = type
        self.__duration = duration

    def get_types(self):
        return self.__type