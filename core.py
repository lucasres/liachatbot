from prebot import prebot
from analyze import analyze
from section import section
from collections import OrderedDict

class chatCore():

    def __init__(self):
        """
        Construct of the class
        """
        #secção inicial
        self.sectionActual = 0;
        self.patterns = []

    def levenshtein(self,s1, s2):
        """
        Calculando a distância de Levenshtein
        :param s1: String
        :param s2: String
        :return: Int
        """
        if len(s1) < len(s2):
            return self.levenshtein(s2, s1)

        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1  # than s2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def compareTo(self,s1,s2):
        """
        compares the first string with the second returning the equivalence in percentage
        :param s1: List
        :param s2: List
        :return: Float
        """
        #criando a lista de tokens
        pre = prebot()
        s1Token = pre.createToken(s1)
        s2Token = pre.createToken(s2)
        s2Token = s2Token[::-1]

        if(len(s2Token)>len(s1Token)):
            return self.compareTo(s2,s1)

        #iniciando variaveis de controle
        total = len(s1Token) + len(s2Token)
        distance = len(s1Token)-len(s2Token)

        while(s2Token):
            word = s2Token.pop()
            if word in s1Token:
                s1Token.remove(word)
            else :
                distance += 1

        return 100-((distance*100)/total)


    def getResponse(self,input):
        """
        Get response for the input, basead in pattern
        :param input:
        :return:
        """

    def getPatterns(self):
        return self.patterns

    def getSectionActual(self):
        return self.sectionActual


    def init(self):
        """
        Init the chatbot
        :return:
        """
        a = analyze()
        #get MainSection
        self.sectionActual = a.getSectionMain()
        if self.sectionActual == -1:
            print("Nao ha question main!")
            return 0

        #section main
        s = section(self.sectionActual)
        #pegando padrões da section main
        self.patterns = s.getPatterns()

    def conversationText(self):
        """
        Start conversation in text mode
        :return:
        """
        entry = input("Voce => ")
        while entry != "!sair":
            #recebe um dicionario contendo os padroes e o score
            aux = self.compareToAll(entry)
            #seleciona o maior score
            pattern = self.getBiggestScore(aux)
            print(str(pattern))
            entry = input("Voce => ")



    def getBiggestScore(self,scores):
        """
        Get biggest score of the dict and return
        :param scores:
        :return: Pattern
        """
        od = OrderedDict(sorted(scores.items()))
        print(od)
        #pega somente o Pattern
        return od.popitem()[1]

    def compareToAll(self,entry):
        """
        Compare entry with all the patterns of section actual
        :param entry: String
        :return: Dict
        """
        #dicionario que armazena o padrao e o score de similaridade
        aux = {}
        for p in self.patterns:
            aux.update({int(self.compareTo(entry,str(p))):p})

        return aux

c = chatCore()
print(c.compareTo("pele eh considerado o rei do futebol no pais","roberto carlos eh considerado o rei da musica no pais"))
c.init()
c.conversationText()
