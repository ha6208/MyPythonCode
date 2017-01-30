import Epic

adj = Epic.userString('Enter an adjective: '),
adj2 = Epic.userString('Enter another adjective: '),
pluralnoun = Epic.userString('Enter a plural noun: '),
pluralnoun2 = Epic.userString('Enter another plural noun: '),
celeb = Epic.userString('Enter a celebrity: '),
noun = Epic.userString('Enter a noun: '),

sentence = ('In the shadowy world of spies, a/an ADJ organization like the US govt uses spies to infiltrate ADJ2 groups'
            'for the purpose of obtaining top secret PLURALNOUN. A teacher, CELEB or even the little old NOUN with a cane and'
            'fifteen pet PLURALNOUN2 could be a spy.')

print

sentence = sentence.replace('ADJ', adj)
sentence = sentence.replace('ADJ2', adj2)
sentence = sentence.replace('PLURALNOUN', pluralnoun)
sentence = sentence.replace('PLURALNOUN2', pluralnoun2)
sentence = sentence.replace('CELEB', celeb)
sentence = sentence.replace('NOUN', noun)

print sentence