#Tokenization using Regular Expressions

import re

def tokenize_text(text):
    print("\nSentence Tokenization")
    sentence = re.split(r'[.!?]', text)
    sentence = [s.split() for s in sentence if s.strip()]
    for i, s in enumerate(sentence, 1):
        print(f"Sentence {i}: {s}")

    print("\nWord Tokenization")
    word = re.findall(r'\w+',text)
    print(word)

if __name__ == "__main__":
    print("Tokenization Application using RE")
    user_text = input("Enter text: ");
    tokenize_text(user_text)
