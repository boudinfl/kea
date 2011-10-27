#!/usr/bin/python
# -*- coding: utf-8 -*-

import kea
import codecs
import sys

################################################################################
sentence = u"Aujourd'hui, le Kea est le seul perroquet alpin au monde."
keatokenizer = kea.tokenizer()
tokens = keatokenizer.tokenize(sentence)
print tokens
################################################################################