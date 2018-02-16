from connections import con
from response import response

class responseSet():
    def __init__(self,id):
        """
        Construct of the class
        :param id:
        """
        self.responses = []
        self.patternId = id

        self.responses = self.getAllResponsePatternId()


    def getAllResponsePatternId(self):
        """
        Get all response for patternid
        :return:
        """
        c = con()
        #uma lista de tuplas [(id,response,patternId),...]
        aux = c.getAllResponsePattern(self.patternId)
        # temporaria para retornar
        tmp = []
        for rs in aux:
            tmp.append(response(rs))

        return tmp


    def getResponses(self):
        """
        Return all responses for the patternId
        :return:
        """
        return self.responses





ts = responseSet(2)
for rs in ts.getResponses():
    print(rs.getResponse())