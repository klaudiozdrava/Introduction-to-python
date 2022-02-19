import random
import numpy as np



allsteps=[]#Θα αποτελειται απο το συνολο των βηματων που απετυθηκαν για να ληξει το παιχνιδι σε καθε επαναληψη
for i in range(100):
    # Το S αντιπροσωπευει το μικρο καπακι, το M το μεσσαιο και το L το μεγαλο
    eidhKapakiwn = ['S', 'M', 'L']*9
    random.shuffle(eidhKapakiwn)#Ανακατευομε την λιστα με τα καπακια απο την οποια επιλεγεται καθε φορα 1

    step=0#Τα βηματα μεχρι να ολοκληρωθει η καθε παρτιδα
    square=[' ']*9#Το 3*3 τετραγωνο
    flag=False
    print(str(i+1)+'  Επανάληψη ')
    while 1:


        positionrow=random.randint(0, 8)#Επιλεγεται τυχαια μια θεση του τετραγωνου

        if flag:
            break

        step += 1

        kapaki=eidhKapakiwn[0]#Διαλεγουμε το πρωτο καπακι και το τοποθετουμε στο τελος της λιστας
        #Ο λογος διοτι αν το καπακι δεν μπορει να τοποθετηθει σε μια τυχαια θεση του τετραγωνου δεν θελουμε να το ''πεταξουμε''
        eidhKapakiwn.append(eidhKapakiwn.pop(0))
        if ord(kapaki)<ord(square[positionrow]) or square[positionrow]==' ':
           kapaki = eidhKapakiwn.pop()#Αφαιρουμε το συγκεκριμενο καπακι απο το συνολο των 27 καπακιων
           square[positionrow]=kapaki#Το τοποθετουμε στο τετραγωνο 3*3

        X = np.array(square)
        X = np.reshape(X, (-1, 3))#Χρησιμοποειται καθαρα για την εμφανιση του τετραγωνου 3*3

        if step>2:

           reversed_list = square[::-1]
           prwthdiagwnios=square[0]+square[4]+square[8]
           deyterhdiagwnios=square[2]+square[4]+square[6]

           #Ελεγχονται οι διαγωνιοι αν ικανοποιουν τις ΧΧΧ ή SML οπου Χ ειναι S ή L ή M
           if len(set(prwthdiagwnios))==1 and prwthdiagwnios[0]!=' ':

               break
           elif (len(set(deyterhdiagwnios))==1 and deyterhdiagwnios[0]!=' '):

               break
           elif prwthdiagwnios=="SML" or prwthdiagwnios[::-1]=="SML":

               break
           elif deyterhdiagwnios=="SML" or deyterhdiagwnios[::-1]=="SML":

               break

           #Ελεγχονται οι γραμμες
           for i in range(0,9,3):
                if square[i]=='S' and square[i+1]=='M' and square[i+2]=='L':
                       flag=True
                       break
                elif reversed_list[i]=='S' and reversed_list[i+1]=='M' and square[i+2]=='L':
                       flag=True
                       break
                elif square[i]==square[i+1]==square[i+2] and square[i]!=' ':
                       flag=True
                       break
           if not flag:
               #Ελεγχονται οι στηλες
               for i in range(3):
                    if square[i]==square[i+3]==square[i+6] and square[i]!=' ':
                        flag=True
                        break
                    elif square[i]=='S' and square[i+3]=='M' and square[i+6]=='L':

                        flag=True
                        break
                    elif reversed_list[i]=='S' and reversed_list[i+3]=='M' and reversed_list[i+6]=='L':

                        flag=True
                        break

    print(X)








    print('--------------------------++---------------------------------------------------')

    allsteps.append(step)

print('\n')
print('Ο μέσος όρος των βημάτων για να ολοκληρωθεί η διαδικασια ειναι  '+str(sum(allsteps)/100))









