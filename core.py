from prebot import prebot
from analyze import analyze
from section import section
from responseSet import responseSet
from collections import OrderedDict
from connections import con

import os, time

class chatCore():

    def __init__(self):
        """
        Construct of the class
        """
        #secção inicial
        self.sectionActual = 0;
        self.sections = []
        self.patterns = []

    def levenshtein(self,s1, s2):
        """
        Calculating distance from Levenshtein
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
        #creating list of tokens
        pre = prebot()
        s1Token = pre.createToken(s1)
        s2Token = pre.createToken(s2)
        s2Token = s2Token[::-1]

        if(len(s2Token)>len(s1Token)):
            return self.compareTo(s2,s1)

        #initialing variables of control
        total = len(s1Token) + len(s2Token)
        distance = len(s1Token)-len(s2Token)

        while(s2Token):
            word = s2Token.pop()
            if word in s1Token:
                s1Token.remove(word)
            else :
                distance += 1

        return 100-((distance*100)/total)


    def getPatterns(self):
        return self.patterns

    def getSectionActual(self):
        return self.sectionActual


    def init(self):
        """
        Init the chatbot
        :return:
        """
        #time.ctime(os.path.getmtime('brain.db'))
        a = analyze()
        #get MainSection
        self.sectionActual = a.getSectionMain()
        if self.sectionActual == -1:
            print("Nao ha question main!")
            return 0

        #section main
        s = section(self.sectionActual)
        #get patterns of the section main
        self.patterns = s.getPatterns()
        #get all sections
        self.sections = a.getSections()

    def conversationText(self):
        """
        Start conversation in text mode
        :return:
        """
        entry = input("Voce => ")
        while entry != "!sair":
            #receives a dictionary containing the patterns and score
            aux = self.compareToAll(entry)
            #select the biggest score
            pattern = self.getBiggestScore(aux)
            #geting the response
            res = responseSet(int(pattern))
            response = res.getResponse()
            #response of the Lia
            print("Lia => " + response.getResponse())
            #getting action
            self.takeDecision(response.action)
            entry = input("Voce => ")



    def getBiggestScore(self,scores):
        """
        Get biggest score of the dict and return
        :param scores:
        :return: Pattern
        """
        od = OrderedDict(sorted(scores.items()))
        #print(od)
        #get only pattern
        return od.popitem()[1]

    def compareToAll(self,entry):
        """
        Compare entry with all the patterns of section actual
        :param entry: String
        :return: Dict
        """
        #dictionary that stores the pattern and similarity score
        aux = {}
        for p in self.patterns:
            aux.update({int(self.compareTo(entry,str(p))):p})

        return aux

    def changeSection(self,name):
        """
        Change flow of the conversation
        :param name: String
        :return:
        """
        c = con()
        aux = c.getSectionByName(name)
        print(aux)



    def setPatterns(self,patterns):
        """
        Set a new list of pattern
        :return:
        """
        self.patterns = patterns


    def takeDecision(self,action):
        """
        Causes the core to make a decision
        :param action: List
        :return:
        """
        #if nothing
        if(action==None):
            return None
        #if action is jump
        if(action[0]=="jump"):
            self.changeSection(action[1])