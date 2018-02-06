from connections import con

class response():
    def __init__(self,id):
        self.id = id
        self.patternId = 0
        self.response = ""
        #povoar instancia
        self.getResponseIdPattern()

    def getResponseIdPattern(self):
        """
        Get the response for a specific id pattern
        :return: String
        """
        c = con()
        #pega uma tupla (id,response,idPattern)
        aux = c.getResponse(self.id)
        print(aux)


teste = response(4)