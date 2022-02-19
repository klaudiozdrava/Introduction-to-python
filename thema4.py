import random


def blackjackclassic():
    p1winrate=0#Πλήθος νικών πρωτου πάικτη
    p2winrate=0#Πληθος νικών δεύτερου παίτη
    drawrate=0#Πλήθος ισοπαλίων
    for i in range(100):
        xartia = []
        figures = ["J", "Q", "K"]
        xarti = [i for i in range(1, 11)] + figures
        color = ["H", "S", "C", "D"]
        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)
        player1=[]
        sum1=0

        while sum1<16:
            sum1=0

            player1.append(xartia.pop())
            for card in player1:
                if card[0] in figures:
                    sum1=sum1+10
                else:
                    sum1=sum1+card[0]

        if sum1>21:
            p2winrate+=1
            # print("P2 wins!")
        else:

            # print("P2 joins the game") #let me add one more player
            player2=[]
            sum2=0

            while sum2<16:
                sum2=0
                player2.append(xartia.pop())

                for card in player2:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2+card[0]

            if sum2>21:
               sum2=0
            if sum1>sum2:
                p1winrate+=1
                # print("P1 wins!")
            elif sum2>sum1:
                p2winrate+=1
                # print("P2 wins!")
            else:
                drawrate+=1
                # print("draw!")

    #Στα 100 παιχνίδια υπολογίζονται και εκτυπώνονται τα στατιστικά παρακάτω
    print("P1 winrate " +str(p1winrate/100))
    print("P2 winrate "+str(p2winrate/100))
    print("Draw "+str(drawrate/100))

#Η συνάρτηση με πειραγμένο το μόιρασμα της τράπουλας σύμφωνα με τα ζητούμενα
#Στην ουσια η λογική ειναι να χωρίσουμε την τράπουλα αρχικά σε δύο συμπληρωματικες τράπουλες
#Η μία απο αυτές θα περιέχει όλα τα χαρτιά που περέχουν φιγόυρα η το 10 ενώ η άλλη ολα τα υπόλοιπα(1 εως 9)
#Επειτα στον πρωτο γυρο ο παικτης 1 τραβαει απο την τραπουλα που περιέχει φιγουρα η το 10
#Ο παικτης 2 τραβάει απο την άλλη τράπουλα (στρον πρωτο γυρο μονο)
#Επειτα αναμειγνυονται σε μια οι δυο τράπουλες και ανακατευεται

def blackjackcorrapted():
    p1winrate = 0  # Πλήθος νικών πρωτου πάικτη
    p2winrate = 0  # Πληθος νικών δεύτερου παίτη
    drawrate = 0  # Πλήθος ισοπαλίων
    for i in range(100):

        xartiafigures=[]#Λιστα που θα περιέχει χαρτια με φιγούρες η το 10
        xartiaxwrisfigures=[]#Λιστα που θα περιεχει ολα τα χαρτια που δεν περιεχουν φιγουρα η το 10
        xartiamefiguresmonohdeka=["J", "Q", "K",10]
        ypoloipaxartia=[i for i in range(1, 10)]
        color = ["H", "S", "C", "D"]

        #Αποθηκευονται ολα τα χαρτια με τα σχετικα χρώματα στις κατάλληλες λίστες
        for i in xartiamefiguresmonohdeka:
            for j in color:
                xartiafigures.append([i,j])#

        for i in ypoloipaxartia:
            for j in color:
                xartiaxwrisfigures.append([i,j])


        random.shuffle(xartiafigures)#Γίνεται ενα ανακατεμα στις δυο τράπουλες χωριστα
        random.shuffle(xartiaxwrisfigures)

        player1 = []


        sum1 = 0
        player1.append(xartiafigures.pop())


        # Αποθηκευεται τυχαιο χαρτί στην μεταβλητη prwtoxartiGiaTonpaikti2 απο
        # την τραπουλα χωρις φιγουρες ωστε να εισαχθει στην πρωτη θέση της συνολικης τράπουλας
        #Εφοσον ο παικτης 2 χρειαστει να πάιξει
        prwtoxartiGiaTonpaikti2 = xartiaxwrisfigures.pop()

        synolikaxartia=xartiaxwrisfigures+xartiafigures#Δημιουργουμε μια τραπουλα συγχωνευοντας τις δυο χωριστές τράπουλες
        random.shuffle(synolikaxartia)

        while sum1 < 16:
            sum1 = 0
            player1.append(synolikaxartia.pop())
            for card in player1:
                if card[0] in xartiamefiguresmonohdeka:
                    sum1 = sum1 + 10
                else:
                    sum1 = sum1 + card[0]


        if sum1 > 21:
            p2winrate += 1

        else:
            player2=[]
            sum2=0
            synolikaxartia.insert(0,prwtoxartiGiaTonpaikti2)
            player2.append(synolikaxartia.pop(0))

            while sum2 < 16:
                sum2 = 0
                player2.append(synolikaxartia.pop())
                for card in player2:
                    if card[0] in xartiamefiguresmonohdeka:
                        sum2 = sum2 + 10
                    else:
                        sum2 = sum2 + card[0]

            if sum2 > 21:
                sum2 = 0
            if sum1 > sum2:
                p1winrate += 1
                # print("P1 wins!")
            elif sum2 > sum1:
                p2winrate += 1
                # print("P2 wins!")
            else:
                drawrate += 1
                # print("draw!")
    print("P1 winrate " + str(p1winrate / 100))
    print("P2 winrate " + str(p2winrate / 100))
    print("Draw " + str(drawrate / 100))






if __name__ == "__main__":

    print("Normal 21 game results")
    blackjackclassic()
    print('----------------------------------------------')
    print('----------------------------------------------')
    print("Shuffled deck results")
    blackjackcorrapted()