# Leetcode: https://leetcode.com/problems/shortest-completing-word/description/
# It's been a while, this is pretty straight forward. Not sure why this is tagged medium.
# Lot's of fluff involved. I saw some nicer Python solutions using lambdas/counters

import copy
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        # Save dictionary of license plate letters
        plate = {}
        totalLetters = 0
        licensePlate = licensePlate.lower()
        
        for letter in licensePlate:
            letterVal = ord(letter)
            if (65 <= letterVal <= 122):
                if (letter in plate):
                    plate[letter] += 1
                else:
                    plate[letter] = 1
                totalLetters += 1
    
        ret = None
        minLetters = sys.maxint
        for word in words:
            currCopy = copy.deepcopy(plate)
            word = word.lower()
            charLeft = totalLetters 
            for letter in word:
                if (letter in currCopy and currCopy[letter] > 0):
                    currCopy[letter] -= 1
                    charLeft -= 1

                if (charLeft == 0):
                    if (len(word) < minLetters):
                        minLetters = len(word)
                        ret = word
                    
        return ret
                    
                    
                    
