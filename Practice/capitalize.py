# Task 06: Capitalization


# test_input = "('my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily.
# do you know my pet dog’s name? i love my pet very much.')"

def capitalize(s):

    newS = ""
    
    stops = ".?!"
    corner_case = " .?!'"
    for i in range(len(s)):
        if i == 0:
            newS += s[i].upper()

        # corner case for i
        elif (s[i] == 'i'):
            if s[i+1] in corner_case and s[i-1] == " ":
                newS += s[i].upper()
            else:
                newS +=s[i]
            
        # checks puncuation marks ".?!"
        elif i>2 and s[i-2] in stops and s[i-1]==" ":
                newS += s[i].upper()

        else:
            newS += s[i]
        
    print(newS)
        
    

capitalize("may i go there. my favourite animal is a dog. and i'll go there. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.")


