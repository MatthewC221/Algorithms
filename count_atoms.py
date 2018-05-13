# Leetcode: https://leetcode.com/problems/implement-magic-dictionary/description/
# This question is good but there are annoying components to it, the possibility of "M", "Mg", "Mg3", "Mg321", etc.
# Surprised that this runs fast (beats 98%), there are definitely ways to optimise/clean it up but I cbb

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        
        levels = [[]]        
        in_level = 0
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                in_level += 1
                levels.append([])
            elif 65 <= ord(formula[i]) <= 90:
                multiplier = 0
                cur_elem = formula[i]
                # Lowercase character combinations: "Mg"
                if i + 1 < len(formula) and 97 <= ord(formula[i+1]) < 122:
                    cur_elem = formula[i:i+2]
                    i += 1
                
                j = i + 1
                # Multipler: "Mg32"
                while j < len(formula) and 48 <= ord(formula[j]) <= 57:
                    multiplier = multiplier * 10 + int(formula[j])
                    j += 1
                
                if multiplier != 0: 
                    i = j - 1
                levels[in_level].append((cur_elem, max(multiplier, 1)))
            else:   
                multiplier = 0
                while i + 1 < len(formula) and 48 <= ord(formula[i+1]) <= 57:
                    multiplier = multiplier * 10 + int(formula[i+1])
                    i += 1
                i -= 1
                # Append the current level to the previous level with the multiplier
                while levels[in_level]:
                    elem, freq = levels[in_level].pop()
                    levels[in_level-1].append((elem, freq*int(multiplier)))
                in_level -= 1
                i += 1
            i += 1
        
        # Analyse and sort the 0th level
        freq = {}
        for k, v in levels[0]:
            if k in freq:
                freq[k] += v
            else:
                freq[k] = v
        
        ret = ""
        for key in sorted(freq):
            if freq[key] == 1:
                ret += key
            else:
                ret += key + str(freq[key])
        
        return ret
        
