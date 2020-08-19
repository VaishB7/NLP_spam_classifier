import sys
import os


def learn():
    input_Directory = sys.argv[1]
    #print('input_Directory',input_Directory)

    total_Spam_Mails = 0
    total_Mails = 0
    total_Ham_Mails = 0
    Vocab = []
    #total_Unique_Vocab = 0
    total_Vocab_Spam = 0
    total_Vocab_Ham = 0

    vocab_Spam = {}
    vocab_Ham = {}

    for src, x, mails in os.walk(input_Directory):
       
        for mailname in mails:
            current_Mail_Directory = os.path.dirname(os.path.abspath(os.path.join(src, mailname)))
            
            if "spam" in mailname:
                total_Mails+=1
                total_Spam_Mails+=1
                file_path = os.path.abspath(os.path.join(src, mailname))

                
                Mails = open(file_path, "r", encoding="latin1")
                token_List = Mails.read().split()
              

                for token in token_List:
                    total_Vocab_Spam += 1
                    token = token.lower()
                    if token not in vocab_Spam:
                        vocab_Spam[token] = 1
                    else:
                        vocab_Spam[token] += 1


            elif "ham" in mailname:
                total_Mails+=1
                total_Ham_Mails+=1
                file_path = os.path.abspath(os.path.join(src, mailname))
                

                Mails = open(file_path, "r", encoding="latin1")
                token_List = Mails.read().split()


                for token in token_List:
                    total_Vocab_Ham += 1
                    token = token.lower()
                    if token not in vocab_Ham:
                        vocab_Ham[token] = 1
                    else:
                        vocab_Ham[token] += 1

            else:
                print("Not a proper file")

    

    #get in a list and dump it once
    with open('nbmodel.txt', 'w') as file:
        file.write(str(total_Spam_Mails)+"\n")
        file.write(str(total_Ham_Mails)+"\n")
        file.write(str(total_Mails) + "\n")
        file.write(str(total_Vocab_Spam) + "\n")
        file.write(str(total_Vocab_Ham) + "\n")
        #file.write(str(total_Unique_Vocab) + "\n")
        file.write(str(vocab_Spam))
        file.write("\n")
        file.write(str(vocab_Ham))
        #file.write("\n")


if __name__ == "__main__":

    if(len(sys.argv)==1):
        print("Enter the directory of the files")
        sys.exit('No file directory Present')
    else:
        learn()
