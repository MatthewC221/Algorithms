# Leetcode: https://leetcode.com/problems/word-ladder/description/
# Beats 0.07% of test cases. I made a pre-defined dict as well. NOT SURE MAN
# TLE's sometimes, I think you need to construct a graph for this sigh

from string import ascii_lowercase

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # BFS
        
        all_words = {}
        step = {}
        wordList.append(beginWord)
        for word in wordList:
            all_words[word] = 1
            step[word] = []
            
        all_words[beginWord] = 1
        
        # Step is a dict that shows what the current word can step to
        for i in xrange(len(wordList)):
            for j in xrange(len(wordList[i])):
                tmp = list(wordList[i])
                for c in ascii_lowercase:
                    tmp[j] = c
                    new_word = ''.join(tmp)
                    if (new_word in all_words and new_word != wordList[i]):
                        step[wordList[i]].append(new_word)
        
        queue = [(beginWord, 1)]
        H = {}
        # Start with the first step
        
        while queue:
            new = []
            for j in xrange(len(queue)):
                cur_word, dist = queue[j][0], queue[j][1]
                H[cur_word] = 1         
                
                possible = step.get(cur_word, [])
                for i in xrange(len(possible)):
                    if (possible[i] == endWord): return dist + 1
                    if (possible[i] not in H):
                        new.append((possible[i], dist+1))                  
            queue = new
        
        return 0
