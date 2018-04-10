from core import chatCore

#instancie chatbot class
c = chatCore()
#storage knowlegue in database
c.init()
#start conversation
c.conversationText()