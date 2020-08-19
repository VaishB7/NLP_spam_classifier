import sys
import os
import math

def classify():
    total_Spam_Mails = 0
    total_Ham_Mails = 0
    total_Mails = 0
    vocab_Spam={}
    vocab_Ham = {}
    total_Vocab_Spam = 0
    total_Vocab_Ham = 0
    total_Unique_Vocab = 0


    Vocab = []
    spam_probability_1 = {}
    ham_probability_1 = {}

    mail_models_file = open("nbmodel.txt","r",encoding="latin1")
    split_models = mail_models_file.read().splitlines()
    #print("split",split_models)



    total_Spam_Mails = int(split_models[0])
    total_Ham_Mails = int(split_models[1])
    total_Mails = int(split_models[2])
    total_Vocab_Spam = int(split_models[3])
    total_Vocab_Ham = int(split_models[4])
    #total_Unique_Vocab = int(split_models[7])
    vocab_Spam = eval(split_models[5])
    vocab_Ham = eval(split_models[6])

    #print("TYPE",type(vocab_Spam))

    for spam_keys in vocab_Spam.keys():
        if spam_keys not in vocab_Ham:
            vocab_Ham[spam_keys] = 0

    for ham_keys in vocab_Ham.keys():
        if ham_keys not in vocab_Spam:
            vocab_Spam[ham_keys] = 0

    total_Unique_Vocab = len(vocab_Ham)



    for spam_key, spam_val in vocab_Spam.items():
        spam_probability_1[spam_key] = float(spam_val+1)/float(total_Vocab_Spam+total_Unique_Vocab)

    for ham_key, ham_val in vocab_Ham.items():
        ham_probability_1[ham_key] = float(ham_val+1)/float(total_Vocab_Ham+total_Unique_Vocab)


    probability_spam = float(total_Spam_Mails) / float(total_Mails)
    probability_ham = float(total_Ham_Mails) / float(total_Mails)



    f = open("nboutput.txt", "w")
    input_Directory = sys.argv[1]
    print('input_Directory', input_Directory)

    for src, x, mails in os.walk(input_Directory):
        
        for mailname in mails:
            current_Mail_Directory = os.path.dirname(os.path.abspath(os.path.join(src, mailname)))

            file_path = os.path.abspath(os.path.join(src, mailname))
            
            if file_path.endswith(".txt"):
                Mails = open(file_path, "r", encoding="latin1")
                token_List = Mails.read().split()

                multiplication_spam_upper = math.log(probability_spam,10)
                multiplication_ham_upper = math.log(probability_ham,10)
                #multiplication_spam_lower = 1
                #multiplication_ham_lower = 1
                p_spam_word = 0
                p_ham_word = 0

                for token in token_List:
                    token = token.lower()

                    if token in (vocab_Spam or vocab_Ham):
                        multiplication_spam_upper = math.log(spam_probability_1[token],10)+multiplication_spam_upper
                        #multiplication_spam_lower = multiplication_spam_lower*Vocab[token]
                        multiplication_ham_upper = math.log(ham_probability_1[token],10) + multiplication_ham_upper
                        #multiplication_ham_lower = multiplication_ham_lower*Vocab[token]
                    else:
                        continue

                #1 file done
                p_spam_word = multiplication_spam_upper
                p_ham_word = multiplication_ham_upper

                #print("p_spam_word",p_spam_word)
                #print("p_ham_word", p_ham_word)


                if p_spam_word >= p_ham_word:
                    f.write("spam"+"\t"+file_path+"\n")
                else:
                    f.write("ham"+"\t"+file_path+"\n")
                    #print("HAM")


    f.close()
if __name__ == "__main__":
   
    if (len(sys.argv) == 1):
        print("Enter the directory of the files")
        sys.exit('No file directory Present')
    else:
        classify()
 