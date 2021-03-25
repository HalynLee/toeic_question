from nltk.tokenize import sent_tokenize
import argparse
from random import randint


def find_sentence_place(sentences):
    numofsent = len(sentences)
    sent_list = sentences
    j = 1
    choices = []
    AtoD = {1:'(A)', 2:'(B)',3:'(C)', 4:'(D)'} 
    
    #Choose a sentence
    target = randint(1 ,numofsent-1)
    target_sent = sent_list.pop(target)

    #Make choices number
    for i in range(-2,2):
        num = (target + i)%(numofsent-1)
        choices.append(num)
    choices.sort()
    print(choices)

    for i in range(numofsent-1) :
        if i in choices :
            print(sent_list[i], '[',j,']', end=' ')
            j += 1
        else :
            print(sent_list[i], end=' ')

    print('\n===================================================\n')
    print('In which of the positions marked [1],[2],[3] and [4] \ndoes the following sentence best belong?')
    print('\n\n"', target, target_sent , '"\n')
    print('(A) [1]\n(B) [2]\n(C) [3]\n(D) [4]\n')
    print('\n\nAnswer =>', AtoD[choices.index(target-1)+1])



def sentence_scramble(sentences):
    numofsent = len(sentences)
    first_sent = sentences[0]
    print("First = ", first_sent)
    


def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--text_dir",
        default=None,
        type=str,
        required=True,
        help="The text that will be used as context for question generation.",
    )
    
    args = parser.parse_args()

    with open(args.text_dir, 'r') as file:
        text_file = file.read()

    sent_list = sent_tokenize(text_file)
    for i in range(len(sent_list)) :
        print(i, "th ====> ",sent_list[i])

    find_sentence_place(sent_list)
    #sentence_scramble(sent_list)

if __name__ == "__main__":
    main()

