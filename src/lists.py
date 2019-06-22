
class UniqueList(list):

    def __init__(self, max_length=None, *args):
        list.__init__(self, *args)
        self.max_length = max_length#could check for number

    def append(self, string):
        if type(string) is str and len(string) > 0:
            if string in self:
                list.remove(self, string)
            elif self.max_length is not None and len(self) == self.max_length:
                list.pop(self, 0)
            list.append(self, string)