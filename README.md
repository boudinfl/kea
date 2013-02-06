# kea

kea is a simple rule-based tokenizer for French. The tokenization process is decomposed in two steps:
    
1. A rule-based tokenization approach is employed using the punctuation as an 
   indication of token boundaries.

2. A large-coverage lexicon is used to merge over-tokenized units (e.g. fixed 
   contractions such as *aujourd'hui* are considered as one token)

A typical usage of this module is:
    
    import kea
	sentence = "Le Kea est le seul perroquet alpin au monde."
	keatokenizer = kea.tokenizer()
	tokens = keatokenizer.tokenize(sentence)

	['Le', 'Kea', 'est', 'le', 'seul', 'perroquet', 'alpin', 'au', 'monde', '.']
