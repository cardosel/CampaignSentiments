import sys


'''
Create dictionary of words in sentiments file: Word --> score
'''
def makeSentsDict(sentiments_fp):
    scores = {} 
    for line in sentiments_fp:
        term, score  = line.split("\t")  
        scores[term] = int(score)  
    
    return scores

'''
Create dictionary of comments: Comment --> calculated score
'''
def makeCommentsDict(comments_fp, sentsDict):
    commentsDict = {}
    
    for line in comments_fp:
        words = line.split()
        score = 0

        #Calculate sentiment of this comment
        for word in words:
            if word in sentsDict:
                score = score + sentsDict[word]

        #Add to dictionary
        commentsDict[line] = score
        
    return commentsDict

'''
Calculate sentiment for words not in sentiment file
'''
def calcNewSents(sents_fp, sents_dict, comments_dict):
    newSentsDict = {}
    
    for line in comments_dict.keys():
        words = line.split()
        score = 0
        
        for word in words:
            if word not in sents_dict:
                newSentsDict[word] = calcWordSentiment(comments_dict, word)
                print word + " " + str(newSentsDict[word])
                return word

                print sum(newSentsDict[word].values())


                # prints word and the score in string format.
                # new sents dict holds an array of  calc word sentiment scores.
                # get t








# Calculate aggregate the total score





'''
Aggregate sentiment for a term: 1/(# relevant comments) * [sum of sentiment scores for each of those relevant comments]
'''
def calcWordSentiment(commentsDict, word):
    count = 0
    sumSent = 0

    for comment in commentsDict:
        if word in comment:
            count = count + 1
            sumSent = sumSent + commentsDict[comment]
            
    score = (1.0/count)*(sumSent)

    return score



def main():
    # Read in files: sentiment words, list of comments
    #sent_file = open(sys.argv[1])
    sent_file = open( "./AFINN-111.txt" )
    #comment_file = open(sys.argv[2])
    comment_file = open( "./hillary1" )
    
    # Make dictionaries out of the two files
    sentsDict = makeSentsDict(sent_file)
    commentsDict = makeCommentsDict(comment_file, sentsDict)

    # Calculate sentiment of words not in dictionary
    calcNewSents(sent_file, sentsDict, commentsDict)



if __name__ == '__main__':
    main()

