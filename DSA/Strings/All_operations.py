## All opertions of string

class MyString:
    def __init__(self):
        self.string = ""
    def length(self):
        return len(self.string)
    
    def check_empty(self):
        if len(self.string) == 0:
            print(True)
        else:
            print(False)
    
    def concatinate(self,string1,string2):
        print(self.string+string1+string2)
    
    
    
    def print_string(self):
        print(self.string)
    
    # Toadya commit



string = MyString()


string.concatinate("hello", "world")
string.check_sub_string_search("hello")

string.print_string()
