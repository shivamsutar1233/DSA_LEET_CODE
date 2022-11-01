######################################
######## SHIVAM ASHOK SUTAR ##########
######################################

def zigzag_convert(s,numRows):
    strings = ['']*numRows
    factor = numRows-1
    isTrue = True
    strings[0] += s[0]
    for i in range(1,len(s)):
        idx = i%factor
        if isTrue:
            #From up to down
            if idx==0:
                strings[factor] += s[i]
                isTrue = False
            else:
                strings[idx] += s[i]
        else:
            #form down to up
            if idx==0:
                strings[0] += s[i]
                isTrue = True
            else:
                strings[numRows-idx-1] += s[i]
        print(strings)
    return ''.join(strings)



if __name__== "__main__":
    
    ###### INPUT: 'PAYPALISHIRING'
    ###### OUTPUT: 'PAHNAPLSIIGYIR'
    zigzag_convert('PAHNAPLSIIGYIR',3)
 
    ###### INPUT: 'PAYPALISHIRING'
    ###### OUTPUT: 'PINALSIGYAHRPI'
    zigzag_convert('PAHNAPLSIIGYIR',4)
