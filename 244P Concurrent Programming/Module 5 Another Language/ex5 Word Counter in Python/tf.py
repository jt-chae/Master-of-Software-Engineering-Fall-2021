import re, sys, collections

stopwords = set(open('stop_words').read().split(','))
words = re.findall('\w{3,}', open(sys.argv[1]).read().lower())
counts = collections.Counter(w for w in words if w not in stopwords)
for (w, c) in counts.most_common(25):
    print w, '-', c
