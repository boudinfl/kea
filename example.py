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

################################################################################
sentence = u"D’où le repli des penseurs républicains sur la forme nécessaire d’une « identité nationale », seul lieu possible d’une démocratie comme auto-détermination collective contre les périls du libéralisme et du communautarisme."
keatokenizer = kea.tokenizer()
tokens = keatokenizer.tokenize(sentence)
print tokens
################################################################################
