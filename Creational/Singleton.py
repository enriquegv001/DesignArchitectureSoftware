
class Database:
    __instance = None
        
    def __init__(self, url):
        if Database.__instance is not None:
            raise Exception("This class is a signleton class!")
        
        else:
            self.url = url
            Database.__instance = self
    
    @staticmethod
    def getInstance():
        """Static Access Mehtod"""
        if Database.__instance is None:
            Database('http//localhost:0000')
        return Database.__instance
    

if __name__ == "__main__":

    instance1 = Database.getInstance()
    instance2 = Database.getInstance()

    print('Is the same?', instance1 is instance2)





