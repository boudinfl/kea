#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
:Name:
    kea

:Authors:
    Florian Boudin (florian.boudin@univ-nantes.fr)

:Version:
    0.21

:Date:
    - 21 nov. 2011

:Description:
    kea is a tokenizer for French. The tokenization process is decomposed in two
    steps:
    
        1. A rule-based tokenization approach is employed using the punctuation
           as an indication of token boundaries.
        2. A large-coverage lexicon is used to merge over-tokenized units (e.g.
           fixed contractions such as *aujourd'hui* are considered as one token)

:History:
    - 0.21 (21 nov. 2011), bug fixes, adding the french city lexicon
    - 0.2 (26 oct. 2011), adding a large lexicon constructed from the lefff.
    - 0.1 (20 oct. 2011), first released version.

:Usage:
    A typical usage of this module is sample:
    
        >>> import kea
        >>> sentence = "Le Kea est le seul perroquet alpin au monde."
        >>> keatokenizer = kea.tokenizer()
        >>> tokens = keatokenizer.tokenize(sentence)
        ['Le', 'Kea', 'est', 'le', 'seul', 'perroquet', 'alpin', 'au', 'monde', 
        '.']
"""

import os
import re
import codecs

#~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# [ tokenizer
#~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
class tokenizer:
    """ The Kea Tokenizer is a rule-based tokenizer for french. """

    #-T-----------------------------------------------------------------------T-
    def __init__(self):
        """ Constructs a new tokenizer. """
        
        self.resources = os.path.dirname(__file__) + '/resources/'
        """ The path of the resources folder. """
        
        self.lexicon = {}
        """ The dictionary containing the lexicon. """

        self.regexp = re.compile(r"""(?xumsi)
          (?:[lcdjmnts]|qu)'                            # Contractions
        | http:[^\s]+\.\w{2,3}                          # Adresses web
        | \d+[.,]\d+                                    # Les réels en/fr
        | [.-]+                                         # Les ponctuations
        | \w+                                           # Les mots pleins
        | [^\w\s]                                       # -
        """)
        
        self.loadlist(self.resources+'abbrs.list')
        """ Loads the default lexicon (path is /resources/abbrs.list). """
        
        self.loadlist(self.resources+'villes.list')
        """ Loads the city lexicon (path is /resources/villes.list). """
    #-B-----------------------------------------------------------------------B-


    #-T-----------------------------------------------------------------------T-
    def tokenize(self, text):
        """
        Tokenize the sentence given in parameter and return a list of tokens. 
        This is a two-steps process: 1. tokenize text using punctuation marks,
        2. merge over-tokenized units using the lexicon.
        """
        
        #=======================================================================
        # STEP 1 : tokenize with punctuation
        #=======================================================================
        tokens = self.regexp.findall(text)
        
        #=======================================================================
        # STEP 2 : merge over-tokenized units using the lexicons
        #=======================================================================
        
        # A temporary list used for merging tokens
        tmp_list = []
        # First counter
        i = 0
        # Second counter
        j = 0
        
        # Loop and search for mis-tokenized tokens
        while i < len(tokens):
            # The second counter indicates the ending character
            j = i
            # While the second counter does not exceed the last word
            while j <= len(tokens):
                # The candidate container
                candidate = ''
                # Construct the candidate token from i to j
                for k in range(i, j):
                    candidate += tokens[k]
                # If the candidate word must be tokenized
                if self.lexicon.has_key(candidate.lower()):
                    # Place first counter on the last word
                    i = j-1
                    # Replace the i-th token by the candidate
                    tokens[i] = candidate
                    # Stop the candidate construction
                    break
                # Increment second counter
                j += 1
            # Add the token to the temporary list
            tmp_list.append(tokens[i])
            # Increment First counter
            i += 1
        # Return the tokenized text
        return tmp_list
    #-B-----------------------------------------------------------------------B-    
    
    
    #-T-----------------------------------------------------------------------T-
    def loadlist(self, path):
        """ Load a resource list and generate the corresponding regexp part. """

        # Reading the input file sequentially
        for line in codecs.open(path, 'r', 'utf-8'):
            # Get the word
            word = line.strip().lower()
            # Add the word to the lexicon
            self.lexicon[word] = 1
    #-B-----------------------------------------------------------------------B-

#~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# ]
#~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~








