from prebot import prebot

class pattern():
    def __init__(self):
        #variaveis de controle
        self.linesOfBrain = []
        self.vars = {}
        self.getBrain()
        self.sections = {}

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

    def getSections(self):
        """
        Return all lines of the brain
        :return: List
        """
        return self.sections

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
        #recortando a parte que ja foi analisada
        self.linesOfBrain = self.linesOfBrain[i+1:]

    def questions(self):
        """
        Initialize as brain questions
        :return:
        """
        #controle
        i = 0
        aux = []
        flag = False
        #percorre ate o final
        for line in self.linesOfBrain:
            #controle do tamanho da string
            if(len(line)>9):
                #verificando se eh um bloco
                if(line[:9]=="[section "):
                    #adicionando
                    self.sections.update({i:line[9:-1]})
                    i+=1
                    flag = True
                    if(flag):
                        self.section(aux)
                        aux = []
                        flag = False
            aux.append([line,i])
        self.section(aux)



    def section(self,qts):
        """
        Create a structure that stores all the pattern of the section
        :return:
        """
        pre = prebot()
        aux = pre.cleanQuestions(qts)
        aux = pre.prepareData(aux)
        for line in aux:
            print(line)

p = pattern()
print("linhas lidas")
print(p.getLinesOfBrain())
p.init()
print("variaveis")
print(p.getVars())
p.questions()
print("sections")
print(p.getSections())

