from connections import con
from interpretResponse import interpretResponse

class response():
    def __init__(self,id):
        if(isinstance(id,int)):
            self.id = id
            self.patternId = 0
            self.response = ""
            #povoar instancia
            self.getResponseIdPattern()
            self.action = self.interpretResponse()
        elif(isinstance(id,tuple)):
            #(id,response,patternId)
            self.id = id[0]
            self.response = id[1]
            self.patternId = id[2]
            self.action = self.interpretResponse()

    def getResponseIdPattern(self):
        """
        Get the response for a specific id
        :return: String
        """
        c = con()
        #getting one tuple (id,response,idPattern)
        aux = c.getResponse(self.id)
        #The patternId is the previous one
        self.patternId = aux[2]
        #getting response
        self.response = aux[1]

    def getResponse(self):
        """
        Return the response
        :return: Sring
        """
        return self.humanOnlyResponse(self.response)

    def getPatternId(self):
        """
        Return the response
        :return: Sring
        """
        return self.patternId

    def getAction(self):
        """
        Return the action of the response
        :return: List
        """
        return self.action

    def interpretResponse(self):
        """
        Interpret the action of the response
        :return: List
        """
        ir = interpretResponse(self.response)
        return ir.getAction()

    def humanOnlyResponse(self,response):
        """
        Getting only response for human
        :param response: String
        :return: String
        """
        ir = interpretResponse(response)
        return ir.getUnActionPart()