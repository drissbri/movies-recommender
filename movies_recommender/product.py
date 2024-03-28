class Product:
    def __init__(self, idP, name, description):
        self.__idP = idP
        self.__name = name
        self.__description = description

    def get_description(self):
        return self.__description

    def get_name(self):
        return self.__name
    
    def get_idP(self):
        return self.__idP
