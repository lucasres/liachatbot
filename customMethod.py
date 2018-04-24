class customMethod():
    def __init__(self):
        """
        Construct of the class
        """

    def call(self,method):
        """
        Call method of Custom Method Class
        :return:
        """ 
        eval("self."+method+"()")



    #################################################
    # YOUR CUSTOM METHOD
    #################################################


    def helloWord(self):
        """
        Hello Word :)
        :return:
        """
        print("ola mundo :)")