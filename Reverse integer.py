class Solution(object):
    def reverse(self, x):
        x = str(x)[::-1]
        stringLength = len(x)-1
        counter = 0
        if (len(x)>1):
            for char in x:
                if (char != '0'):
                    break
                x = x[:counter] + x[(counter + 1):]
            stringLength = len(x) - 1
        if (x[-1:]=="-"):
            x = x[:-1]
            x = int(x) * -1
            x = str(x)
            
        if (abs(int(x))>=2**31):
            return 0
        return x
