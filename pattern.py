from connections import con

class pattern():
    def __init__(self,id):
        """
        Constructor of the class
        :param id: Integer
        """
        self.id = id;
        self.pattern = ""
        self.section = 0
        #povar instancia
        self.getPatternInDb(id)

    def getPatternInDb(self,id):
        """
        get pattern pf the id
        :param id:
        :return:
        """
        c = con()
        #retorna uma tupla (id,pattern,section)
        aux = c.getPattern(id)
        #pegando o pattern
        self.pattern = aux[1]
        #pegando a section
        self.section = aux[2]

    def getPattern(self):
        """
        Return the pattern
        :return: String
        """
        return self.pattern

    def getSection(self):
        """
        Return the section
        :return: Integer
        """
        return self.section

    def getId(self):
        """
        Return id
        :return: Integer
        """
        return self.id