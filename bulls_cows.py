# Leetcode: https://leetcode.com/problems/matchsticks-to-square/description/
# It's been a while I must admit, straight forward leetcode medium. Not too sure why it's disliked, maybe unconventional
# O(n) time and O(n) space.

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        # The trick is the second or third 
        # Should do a frequency iterate and then a positional iterate
        
        _secret = {}
        _guess = {}
        
        bull = 0
        cow = 0
        
        # Can only be bull or cow
        for i in xrange(len(secret)):
            if (secret[i] == guess[i]):
                bull += 1
            else:
                _guess[guess[i]] = _guess.get(guess[i], 0) + 1
                _secret[secret[i]] = _secret.get(secret[i], 0) + 1
        
        for i in xrange(10):
            if (_secret.get(str(i), 0) > 0 and _guess.get(str(i), 0) > 0):
                cow += min(_secret.get(str(i), 0), _guess.get(str(i), 0))
        
        return (str(bull) + "A" + str(cow) + "B")
