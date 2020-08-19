import sys
import os


label = []
path = []

F_H = 0
F_S = 0

P_Spam = 0
R_Spam = 0
F1_score_spam = 0

P_Ham = 0
R_Ham = 0
F1_score_ham = 0

spam_correct_TS= 0
ham_correct_TH= 0
total_spam= 0
total_ham= 0
total = 0

Mails = open("nboutput.txt","r",encoding="latin1")
Lines = Mails.read().splitlines()


for line in Lines:
    
    total +=1
    temp = line.split("\t")
    label.append(temp[0])
    path.append(temp[1])

#print("Label",label)

for i in range(len(label)):
    if "ham" in path[i]:
        
        if label[i] == "ham":
            ham_correct_TH +=1
        else:
            F_H+=1

    elif "spam" in path[i]:
        
        if label[i] == "spam":
            spam_correct_TS +=1
        else:
            F_S+=1
    else:
        continue


accuracy = float(ham_correct_TH + spam_correct_TS)/float(total)


P_Spam = float(spam_correct_TS)/float((spam_correct_TS+F_S))
P_Ham = float(ham_correct_TH)/float((ham_correct_TH+F_H))

R_Spam = float(spam_correct_TS)/float((spam_correct_TS+F_H))
R_Ham = float(ham_correct_TH)/float((ham_correct_TH+F_S))

F1_score_spam = 2*((P_Spam*R_Spam)/(P_Spam+R_Spam))
F1_score_ham = 2*((P_Ham*R_Ham)/(P_Ham+R_Ham))

print("spam precision:",P_Spam)
print("spam recall: ",R_Spam)
print("spam F1 score:",F1_score_spam)
print("ham precision:",P_Ham)
print("ham recall: ",R_Ham)
print("ham F1 score:",F1_score_ham)
print("Accuracy",accuracy)

