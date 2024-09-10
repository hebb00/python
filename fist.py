class Solution(object):
    def isCircularSentence(self, sentence):
        check = 0
        space = 0
        if sentence[0] == sentence[len(sentence)-1]:
            check+=1
        
        for i in range(len(sentence)):
            if sentence[i] == " ":
                space+=1
                if sentence[i-1] == sentence[i+1]:
                    check+=1


        if check-1 == space:
            return True
        else: 
            return False