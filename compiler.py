from prebot import prebot

class compiler():
    def tokenTable(self,inp):
        """
        Generate the table of tokens
        :param inp: String
        :return: List
        """
        p = prebot()
        aux = p.removeSpaces(inp)
        return aux.split(' ')


    def analise(self,tks):
        """
        Analise all tokens
        :param tks: List
        :return: String
        """
