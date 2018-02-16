from connections import con

class response():
    def __init__(self,id):
        if(isinstance(id,int)):
            self.id = id
            self.patternId = 0
            self.response = ""
            #povoar instancia
            self.getResponseIdPattern()
        elif(isinstance(id,tuple)):
            #(id,response,patternId)
            self.id = id[0]
            self.response = id[1]
            self.patternId = id[2]

    def getResponseIdPattern(self):
        """
        Get the response for a specific id
        :return: String
        """
        c = con()
        #pega uma tupla (id,response,idPattern)
        aux = c.getResponse(self.id)
        self.patternId = aux[2]
        self.response = aux[1]

    def getResponse(self):
        """
        Return the response
        :return: Sring
        """
        return  self.response

    def getPatternId(self):
        """
        Return the response
        :return: Sring
        """
        return self.patternId

