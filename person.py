
class person:
    def __init__(self, name) :
         self.saved_name = name


    def get_name(self):
         return self.saved_name

if __name__ == '__main__':
     #this code is for testing
     p1 = person("Dave")
     p2 = person("Jenny")

