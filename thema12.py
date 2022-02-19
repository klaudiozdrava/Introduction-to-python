import requests
from thema9 import decimalToBinary
import json

from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession



#Μετατροπη δεκαδικου σε δυαδικο
def ASCIIToBin(N):

    arr=[]
    for char in N:

        charNumber = ord(char)
        binaryRep = str(decimalToBinary(charNumber))
        arr.append((8 - len(binaryRep)) * "0" + binaryRep)

    binary="".join(arr)
    return binary


def thema12():

    r = requests.get('https://drand.cloudflare.com/public/latest',
                      headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    data = r.json()

    latest=data["round"]#Παιρνουμε τον πιο προσφατο γύρο

    lasthundarr=[]
    lasthundarr.append(data)#Προσθετουμε στην λιστα ολο το λεξικο
    dic={}

    with FuturesSession() as session:
        #Διατρεχουμε τα τελευταια 99 δεδομενα απο την υπηρεσια
        futures = [session.get("https://drand.cloudflare.com/public/"+str(latest-i)) for i in range(1,100)]
        for future in as_completed(futures):
            response=future.result()
            temp=json.loads(response.content)
            lasthundarr.append(temp)#Μολις αποκριθει το αιτημα μας αποθηκευουμε ολο το λεξικο ενος συγκεκριμενου γυρου

    #Επειδη με την χρηση της  FuturesSession()  και του παραπανω τροπου οι αιτησεις για την αποκτηση των δεδομενων του γυρου
    #δεν γινονται με την "σειρα",κανουμε μια ταξινομηση με βαση την τιμη του κλειδιου 'round'
    lasthundarr=sorted(lasthundarr, key=lambda x: x['round'])
    ListOfAllCodes=[]#Θα αποτελειται απο τις τιμες του κλειδιου randomness
    for object in lasthundarr:
        ListOfAllCodes.append(object['randomness'])


    randomness="".join(ListOfAllCodes)#μετατρεπει ολες τις τιμες randomness σε ενα αλφαριθμητικο

    bin=ASCIIToBin(randomness)#Μετατροπη σε δυαδικο

    #Παρακατω ελεγχεται η μεγαλυτερη ακολουθια απο μηδενικα και ασσους
    mostcontZeros = 0
    mostcontOnes = 0
    tempZeros = 0
    tempOnes = 0
    for i in bin:
        if i == "0":
            tempZeros += 1
            if tempZeros > mostcontZeros:
                mostcontZeros = tempZeros
            tempOnes = 0
        else:
            tempZeros = 0
            tempOnes += 1
            if tempOnes > mostcontOnes:
                mostcontOnes = tempOnes

    print("Random number is "+randomness+" "+str(len(randomness)))
    print("ASCII characters to binary in https://drand.cloudflare.com/public is: ")
    print(bin)
    print("The largest sequence of consecutive zeros is " + str(mostcontZeros))
    print("The largest sequence of consecutive ones is " + str(mostcontOnes))

if __name__ == "__main__":


    thema12()



