# Leetcode https://leetcode.com/problems/fraction-addition-and-subtraction/description/
# This one was quite annoying.. working with strings. I didn't realise there were multi-digit nums

import fractions

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        starting_val = 0
        i = 0
        cur_denom = 0
        cur_numerat = 0   
        

        while (len(expression) > i):
            cur = expression[i]
            if (i == 0): 
                if (expression[i] == '-'):
                    cur_numerat, move = self.getInt(expression, i + 1)
                    cur_numerat *= -1
                    i += (move + 2)
                    cur_denom, move = self.getInt(expression, i)
                else:
                    cur_numerat, move = self.getInt(expression, i)
                    i += (move + 1)
                    cur_denom, move = self.getInt(expression, i)
                    
            if (expression[i] == '-' or expression[i] == '+'):
                tmp_numerat, move = self.getInt(expression, i + 1)
                i += (move + 2)
                tmp_denom, move = self.getInt(expression, i)               
                new_denom = self.LCM(cur_denom, tmp_denom)
                cur_numerat *= new_denom / cur_denom
                tmp_numerat *= new_denom / tmp_denom
                cur_denom = new_denom
                if (cur == '-'):
                    cur_numerat -= tmp_numerat
                else:
                    cur_numerat += tmp_numerat   
            i += 1
        
        divisor = fractions.gcd(cur_numerat, cur_denom)
        if (divisor > 1 and cur_numerat != 0):
            cur_numerat /= divisor
            cur_denom /= divisor
        elif (cur_numerat == 0):
            cur_denom = 1
        
        return str(cur_numerat) + "/" + str(cur_denom)

    # Return a tuple, the int and how many spaces to move
    def getInt(self, expr, i):    
        for j in range(i, len(expr)):
            if (expr[j] == '+' or expr[j] == '-' or expr[j] == '/' or j == len(expr) - 1):
                if (j == len(expr) - 1):
                    j += 1
                print expr[i:j]
                return (int(expr[i:j]), j - i)
            
        return None
    
    def LCM(self, num1, num2):
        return num1 * num2 /  fractions.gcd ( num1 , num2 )
