class Sin():
    """Classe responsável pela analise de sinônimos"""
    synonymous = [
        ['importância','significativo','grave','serio','considerável','interresante'],
        ['ilustre','influente','eminente','prestigioso']
    ]
    def checkIsSin(self,s1,s2):
        for i in range(len(self.synonymous)):
            if((s1 in self.synonymous[i]) and (s2 in self.synonymous[i])):
                return (s1,s1)
        return False

