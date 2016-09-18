__author__ = 'selenacardona'
import sys
import json
import string
import collections

def freq_each_comment(comment_file):
  freq = collections.defaultdict(int)
  with open(comment_file) as cf:
    for line in cf:
      comment = json.loads(line , 'utf=8')
      if 'text' in comment.keys():
        words = unicode(comment['text']).split()
        for word in words:
          word = clean_word(word)
          freq[word] += 1
#          print word, freq[word]
  all_term_sum = sum(freq.itervalues())
  sorted_freq = collections.OrderedDict(sorted(freq.items()))
  for key,value in sorted_freq.items():
    print(key, value/all_term_sum)


def clean_word(word):
  word = word.lower()
  # remove the punctuations in the words
  exclude = set(string.punctuation)
  word = ''.join(ch for ch in word if ch not in exclude)
  return word


def main():
    comment_file = sys.argv[1]
    freq_each_comment(comment_file)

if __name__ == '__main__':
    main()
