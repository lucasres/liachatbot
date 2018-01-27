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

    def cleanQuestions(self,qts):
        """
        Clean questions for will processed
        :param qts: List
        :return: List
        """
        aux = []
        for line in qts:
            if(line[0][:2] == "< " or line[0][:2] == "> "):
                aux.append(line)

        return aux


    def prepareData(self,lines):
        """
        Return only question or response
        :param lines: List
        :return: List
        """
        aux = []
        for line in lines:
            if(line[0][:2] == "< "):
                aux.append([line[0][2:],line[1],'r'])
            elif(line[0][:2] == "> "):
                aux.append([line[0][2:], line[1], 'p'])
        return aux