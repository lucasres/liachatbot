from prebot import prebot

class interpretResponse():

    def __init__(self,pIinput):
        """
        Construct of the class
        """
        self.tokens = []
        self.tokens =self.tokenTable(pIinput)
        self.action = []
        self.action = self.analizeResponse()


    def tokenTable(self,inp):
        """
        Generate the table of tokens
        :param inp: String
        :return: List
        """
        p = prebot()
        aux = p.removeSpaces(inp)
        return aux.split(' ')

    def getTokens(self):
        """
        Get tokens value
        :return: List
        """
        return self.tokens

    def separeteTokens(self):
        """
        Analyze all tokens, returns a list with 2 elements, the first is the not compiled part of the response and the second is the compiled part of the response
        :param tks: List
        :return: List
        """
        #aux strings
        notanalize = ""
        analize = ""
        for tk in self.tokens:
            if(tk[:2] == "{{" and tk[-2:] == "}}"):
                analize = tk
            else:
                notanalize += " " + tk

        return [notanalize,analize]

    def analizeResponse(self):
        """
        This method analize the part dynamic of the entry user
        :return: List
        """
        #get part for will analise
        pAnalize = self.separeteTokens()[1][2:-2]
        #separate
        aux = pAnalize.split('=')
        #set the action
        if aux[0] == "jump":
            return ["jump",aux[1]]
        else:
            return None

    def getAction(self):
        """
        Return the action of analise
        :param self:
        :return: List
        """
        return self.action