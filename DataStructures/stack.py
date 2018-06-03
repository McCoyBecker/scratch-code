class Stack:
    def __init__(self, size):
        self.allocatedsize = size
        self.currentsize = 0
        self.array = []

    def push(self, item):
        
        if self.currentsize == 0:
            self.array.append(item)
            self.currentsize+=1
        
        else:
            if self.currentsize < self.allocatedsize:
                self.array.append(0)
                self.array = [self.array[(i-1+len(self.array))%len(self.array)] for i in range(len(self.array))]
                self.array[0] = item
                self.currentsize+=1

            else:
                print("Stack overflow: too many items")
    


    def pop(self):
        if self.currentsize > 0:
            a = self.array[0]
            popList = [0 for i in range(self.currentsize-1)]
            for j in range(self.currentsize-1):
                popList[j] = self.array[j+1]
            self.array = popList
            self.currentsize = self.currentsize - 1
            return(a)

        else:
            print("Your stack is empty!")

    def top(self):
        if self.currentsize > 0:
            return(self.array[0])
        
        else:
            print("Your stack is empty!")
    

    def currentSize(self):
        return(self.currentsize)

    def isEmpty(self):
        if self.currentsize == 0:
            print("The stack is empty.")

        else:
            print("The stack is not empty.")


