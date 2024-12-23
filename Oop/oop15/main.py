class List:
    def __init__(self, *data: list[any]):
        self.__data = list(data)

    def __getitem__(self, index):
        if index > len(self.__data):
            return self.__data[-1]
        return self.__data[index]
    
    def __setitem__(self, index, value):
        if index > len(self.__data):
            self.__data[-1] = value
            return self.__data
        self.__data[index] = value
        return self.__data

    def __delitem__(self, index):
        if index > len(self.__data):
            del self.__data[-1]
        del self.__data[index]
