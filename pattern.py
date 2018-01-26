class pattern():
    def __init__(self):
        self.linesOfBrain = []
        self.vars = {}
        self.getBrain()

    def getBrain(self):
        """
        Get source of the brain
        :return: Boolean
        """
        with open('brain.lia', 'r') as fp:
            line = fp.readline()
            while line:
                aux = line.strip()
                self.linesOfBrain.append(aux)
                line = fp.readline()
        return True

    def getLinesOfBrain(self):
        """
        Return all lines of the brain
        :return: List
        """
        return self.linesOfBrain

    def getVars(self):
        """
        Return all vars of the brain
        :return: List
        """
        return self.vars

    def init(self):
        """
        Initialize as brain variables
        :return:
        """
        i = 1
        if(self.linesOfBrain[0]=="[init]"):
            while(self.linesOfBrain[i] != "[endinit]"):
                aux = self.linesOfBrain[i].split('=')
                self.vars.update({aux[0]:aux[1]})
                i+=1

    def questions(self):
        """
        Initialize as brain questions
        :return:
        """


    def section(self):
        """
        Create a structure that stores all the pattern of the section
        :return:
        """


p = pattern()
print(p.getLinesOfBrain())
p.init()
print(p.getVars())

