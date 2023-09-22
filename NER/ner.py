
import nltk
import pandas as pd
import warnings
from speech import  Micro_voice
warnings.filterwarnings("ignore")
#nltk.download()
text = """
A multi-agency manhunt is under way across several states and Mexico after
police say the former Los Angeles police officer suspected in the murders of a
college basketball coach and her fiancÃ© last weekend is following through on
his vow to kill police officers after he opened fire Wednesday night on three
police officers, killing one.
"In this case, we're his target," Sgt. Rudy Lopez from the Corona Police
Department said at a press conference, Bangladesh.
The suspect has been identified as Christopher Jordan Dorner, 33, and he is
considered extremely dangerous and armed with multiple weapons, authorities
say. The killings appear to be retribution for his 2009 termination from the
 Los Angeles Police Department for making false statements, authorities say.
Dorner posted an online manifesto that warned, "I will bring unconventional
and asymmetrical warfare to those in LAPD uniform whether on or off duty."
"""
#text = Micro_voice()
entities = []
labels = []
sentence = nltk.sent_tokenize(text)
for sent in sentence:
  for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)), binary = False): # nltk.ne_chunk extract named entities from text 
    if hasattr(chunk, 'label'):
      entities.append(' '.join(c[0] for c in chunk))
      labels.append(chunk.label())
entities_labels = list(set(zip(entities,labels)))

entities_df = pd.DataFrame(entities_labels)
entities_df.columns = ["Entities", "Labels"]

print(entities_df)
