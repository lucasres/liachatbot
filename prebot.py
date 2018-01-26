from re import  sub

class prebot():
    def createToken(self, s):
        """
        Criando uma lista de tokens
        :param s: String
        :return: List(String)
        """
        s = self.removeSpaces(s)
        return s.split(' ')

    def removeSpaces(self, s):
        """
        Removendo os espaços esrrados
        :param s: String
        :return: String
        """
        return sub("\\s+", " ", s)