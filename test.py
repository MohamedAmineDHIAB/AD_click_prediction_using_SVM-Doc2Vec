import numpy as np
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')


sentences = ['amine dhiab']
tok_sent = []
for s in sentences:
    tok_sent.append(word_tokenize(s.lower()))

print(tok_sent)
