from prebot import prebot
from analyze import pattern

class chatCore():
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

        print("total "+str(total) + " distancia "+str(distance))

        return 100-((distance*100)/total)


    def getResponse(self,input):
        """
        Get response for the input, basead in pattern
        :param input:
        :return:
        """


p = pattern()



c = chatCore()
print(c.compareTo("pele eh considerado o rei do futebol no pais","roberto carlos eh considerado o rei da musica no pais"))
