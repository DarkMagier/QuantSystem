import io,sys
class sstream(io.StringIO):
    __instance=None
    def __new__(cls, *args, **kwargs):
        # print("this is new")
        if sstream.__instance==None:
            sstream.__instance=io.StringIO.__new__(cls,*args,**kwargs)
            sstream.__instance.__buff=list()
        return sstream.__instance
    def __init__(self):
        # print("this is init")

        pass

    def write(self, *args, **kwargs):
        for item in args:
            self.__buff.append(item.__str__())
        for item in kwargs:
            self.__buff.append(item.__str__())

        return self
    def readline(self, *args, **kwargs):
        try:
            buff_get=self.__buff[0]
            self.__buff.pop()
            if self.__buff[0]=='\n':
                buff_get+=self.__buff[0]
                self.__buff.pop()
            return buff_get
        except Exception as e:
            return e
    def read(self, *args, **kwargs):
        return "".join(self.__buff)
    def display(self,file=sys.stdout):
        print(self.__buff,file=file)