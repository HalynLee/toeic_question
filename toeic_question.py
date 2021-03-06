from nltk.tokenize import sent_tokenize
import argparse
from random import randint, choice,shuffle
from nltk.corpus import wordnet as wn
import nltk
from word_forms.word_forms import get_word_forms


def find_sentence_place(sentences):
    
    #print original text with order
    for i in range(len(sentences)) :
        print(i, "th ====> ",sentences[i])

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



def get_distractors(word):
    
    result = []
    result.append(word)

    candidates = get_word_forms(word)
    print(candidates)
    
    distractors = list(candidates['a'])
    distractors.extend(list(candidates['v']))
    distractors.extend(list(candidates['n']))

    print(distractors)
    print('=====================')
    
    while len(result) < 4  :
        word = choice(distractors)
        if word not in result :
            result.append(word)
            distractors.remove(word)
        print(result)
        

    return result

def part5(sentence) :
    original_word = None
    candidate_words = []
    word_type = ('RB')
    AtoD = ['(A)','(B)','(C)','(D)']

    text = nltk.word_tokenize(sentence)
    result = nltk.pos_tag(text)
    print(result)

    for word in result :
        if word[1] in word_type:
            candidate_words.append(word[0]) 
    
    print('candidate_words :', candidate_words)
    for word in candidate_words :
        dist_num = 0
        dist = get_word_forms(word)
        for pos in dist.values() :
            print(pos)
            dist_num += len(pos)
        print('dist_num ->', dist_num)
        
        if dist_num > 3:
            original_word = word
            break
    
    if original_word is None :
        print('No original_word')
        return 
    
    print('original_word :', original_word)
    
    distractors = get_distractors(original_word)
    distractors.append(original_word)
    shuffle(distractors)


    print('\n===================================================\n')
    for word in result :
        if word[0] == original_word :
            print('_______', end=' ')
        else :
            print(word[0], end=' ')
    print('\n')

    for i in range(4):
        print(AtoD[i], distractors[i])

    print('\n')




def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--text_dir",
        default=None,
        type=str,
        required=True,
        help="The text that will be used as context for toeic question generation.",
    )
    
    args = parser.parse_args()

    with open(args.text_dir, 'r') as file:
        text_file = file.read()

    sent_list = sent_tokenize(text_file)

    #find_sentence_place(sent_list)
    #sentence_scramble(sent_list)
    part5(sent_list[0])

if __name__ == "__main__":
    main()

