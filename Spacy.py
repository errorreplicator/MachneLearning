import spacy as sp
import pandas as pd

string = 'My filling is that mr. Piotr will win this turnament on plase one 1  two hundred or three '

sp_nlp = sp.load('en')
spacy_obj = sp_nlp(string)

tokens = [(token.orth_,
           token.prob,
           token.is_stop,
           token.is_punct,
           token.is_space,
           token.like_num,
           token.is_oov) for token in spacy_obj]

pandas_ds = pd.DataFrame(tokens,columns=['text','log_probab','stop?','is punkt?','is space?','number?','out of vocab'])

print(pandas_ds)