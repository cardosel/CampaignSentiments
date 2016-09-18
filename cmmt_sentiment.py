__author__ = 'selenacardona'
import sys
import json
from sentimentalgorithm import sentiment, sentiment_lib

# reads the whole comment log and parse it, calculates the sentiment of each comment
def score_each_comment(comment_file, sent_lib):
  with open(comment_file) as cf:
    for line in cf:
      comment = json.loads(line , 'utf=8')
      if 'text' in comment.keys():
        score = sentiment(comment['text'], sent_lib)
        print(score)

def main():
    sent_file = sys.argv[1]
    comment_file = sys.argv[2]
    sent_lib = sentiment_lib(sent_file)
    score_each_comment(comment_file, sent_lib)

if __name__ == '__main__':
    main()
