from connections import con

class pattern():
    def __init__(self,id):
        """
        Constructor of the class
        :param id: Integer or Tuple
        """
        if(isinstance(id,int)):
            self.id = id;
            self.pattern = ""
            self.section = 0
            #povar instancia
            self.getPatternInDb(id)
        elif(isinstance(id,tuple)):
            self.id = id[0]
            self.pattern = id[1]
            self.section = id[2]


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

    def getSection(self):
        """
        Return the section that the pattern is contained
        :return: Int
        """
        return self.section

    def __str__(self):
        """
        Magic method for String
        :return: String
        """
        return self.pattern

    def __int__(self):
        """
        Magic method for Integer
        :return:
        """
        return self.id