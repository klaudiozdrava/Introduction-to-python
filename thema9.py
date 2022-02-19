
#Συναρτηση που υπολογιζει την δυαδικη αναπαρασταση ενος αριθμου Ν
#Η λογικη ειναι παρομοια με τον αλγοριθμο της αναπαραστασης δεκαδικου αριθμου σε δυαδικο
#Υπολογιζεται ο reminder της διαιρεσης του αριθμου με το 2
#Αν ειναι 1 προστιθεται στον αριθμο  B_Number η δυναμη του 10 εις την c
#Οπου c αυξανεται κατα 1 σε κάθε υποδιαιρεση του αριθμου Ν
def decimalToBinary(N):

    B_Number = 0
    cnt = 0
    while (N != 0):
        rem = N % 2
        c = pow(10, cnt)
        B_Number += rem * c
        N //= 2#Διαιρεί τον αριθμο Ν καθε φορα με το 2


        cnt += 1

    return B_Number
#Η συναρτηση askisi9 ανοιγει ενα αρχειο και διαβαζει καθε χαρακτηρα.Επειτα με χρηση της ord βρισκουμε την δεκαδικη αναπαρασταση
#του καθε χαρακτηρα.Στον δεκαδικο αριθμο αυτον καλουμε την decimalToBinary για να βρουμε την δυαδικη του αναπαρασταση
def askisi9(arxeio):
    try:
        file = open(arxeio+'.txt', 'r')


        arr=[]
        while 1:
            # διαβαζει χαρακτηρα
            char = file.read(1)
            if not char:
                break
            charNumber=ord(char)

            binaryRep=str(decimalToBinary(charNumber))
            arr.append((7-len(binaryRep))*"0"+binaryRep)#Προσθετει μηδενικα στα πρωτα κ μπιτς

        binary="".join(arr)
        file.close()

        return binary
    except IOError:
        print("File does not exist")
        return []


#Υπολογιζει το μεγιστο πληθος απο 0 που εμφανιζονται συνεχομενα και 1 αντιστοιχα
def findzerosandones(arxeio):
   wholeBinary=askisi9(arxeio)#Το wholeBinary περιεχει ενα μεγαλο αλφαριθμητικο απο 0 και 1

   mostcontZeros=0
   mostcontOnes=0
   tempZeros=0
   tempOnes=0
   for i in wholeBinary:
       if i=="0":
           tempZeros+=1
           if tempZeros>mostcontZeros:
               mostcontZeros=tempZeros
           tempOnes=0
       else:
           tempZeros=0
           tempOnes+=1
           if tempOnes>mostcontOnes:
               mostcontOnes=tempOnes

   return mostcontOnes,mostcontZeros,wholeBinary


if __name__ == "__main__":
    name=input('Δωστε όνομα αρχείου (χωρις το extension)\n')
    ones,zeros,wholeBin=findzerosandones(name)
    # print("ASCII characters to binary in example.text is :")
    # print(wholeBin)
    print("The largest sequence of consecutive zeros is "+str(zeros))
    print("The largest sequence of consecutive ones is "+str(ones))










