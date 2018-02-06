from connections import con
from pattern import pattern

class section():
    def __init__(self,id):
        """
        Contruct of the class, this call getAllPatternId
        :param id:
        """
        self.id = id
        self.patterns = []
        #povoar lista
        self.getAllPatternsId()


    def getAllPatternsId(self):
        """
        Gets all the patterns of the target section, creating a list with pattern instances
        :param id: Integer
        :return: List
        """
        c = con()
        for p in c.getAllPatternSection(self.id):
            #adicionando na lista um pattern novo
            self.patterns.append(pattern(p[0]))


    def getPatterns(self):
        """
        Return all patterns
        :return:
        """
        return self.patterns


