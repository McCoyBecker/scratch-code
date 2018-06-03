class ShiftCipher:
    def __init__(self, affineMultiplier, constantShift):
        self.affineMultiplier = affineMultiplier
        self.constantShift = constantShift

    def encode(self, messageInList):
        for i in range(len(messageInList)):
            if ord(messageInList[i])!=32:
                messageInList[i] = chr((self.affineMultiplier*ord(messageInList[i])%65+self.constantShift)%25+65)
        return(messageInList)

message = list(input("Insert the message you want to encrypt in all caps: "))
MyCipher = ShiftCipher(1,10)
print("The encrypted message is:")
print(''.join(MyCipher.encode(message)))
