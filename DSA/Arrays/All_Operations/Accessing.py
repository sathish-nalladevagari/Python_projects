# fuction to access random element

class MyArray:
    def __init__(self) :
        self.arr = []
    # Random access
    def random_access(self,index):
        try:
            return self.arr[index]
        except:
            print("Index out of bounds")

    # Insertion

    def insert_element_at_begin(self,element):
        return self.arr.insert(element,0)
    
    def insert_element_at_end(self,element):
        return self.arr.append(element)
    
    def insert_element(self,index,element):
        return self.arr.insert(index,element)
    # Checking
    def check_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
    def print_array(self):
        print(self.arr)
    # deletion
    def delete_at_end(self):
        return self.arr.pop()
    
    def delete_at_begin(self):
        return self.arr.pop(0)
    
    def delete_element(self,element):
        return self.arr.remove(element)
    
    def search_element(self,element):
        if element in self.arr:
            for index in range(len(self.arr)):
                if element == self.arr[index]:
                    print(index)
        else:
            print("Element is not in array")
    
    def sort_array(self):
        return self.arr.sort()
    
arr = MyArray()
arr.insert_element_at_end(1)
arr.insert_element_at_end(2)
arr.insert_element_at_end(3)
arr.insert_element_at_end(4)
arr.insert_element_at_end(2)
arr.insert_element_at_end(1)
arr.check_empty()
arr.insert_element(0,20)
arr.search_element(20)
arr.delete_element(20)
arr.print_array()


    
