def arithmetic_arranger(problems, show_answers=False):

    # define variables
    lines=['','','','']


    if len(problems)>5:  # check if the number of problems is greater than 5
        arranged_math = 'Error: Too many problems.'
        return arranged_math
    for problem in problems:
        parts = problem.split(' ')
        if not parts[0].isdigit() or not parts[2].isdigit(): # check if the numbers are digits
            arranged_math = 'Error: Numbers must only contain digits.'
            return arranged_math
        if parts[1].find('+') == -1 and parts[1].find('-') == -1: # check if the operator is + or -
            arranged_math = "Error: Operator must be '+' or '-'."
            return arranged_math
        parts  = problem.split(' ')
        if len(parts[0])>4 or len(parts[2])>4: # check if the numbers are more than 4 digits
            arranged_math = 'Error: Numbers cannot be more than four digits.'
            return arranged_math
        if parts[1] == '+': # check if the operator is addition or subtraction
            math = str( int( parts[0] ) + int( parts[2] ) )
        else:
            math = str( int( parts[0] ) - int( parts[2] ) )
        
        len_first  = len(parts[0]) # get the length of the first number

        len_second = len(parts[2]) # get the length of the second number

        len_math = len(math) # get the length of the answer
        

        size = len(parts[1] + ' ' + '-' * (max(len_first,len_second) )) # get the size of the number

        lines[0] += ' ' * (size - len( parts[0] ) ) + parts[0]+ 4*' ' # add the first number to the first line
        
        lines[1] += parts[1] + ' ' * (size - len(parts[2])-1) + parts[2]+ 4*' ' # add the operator and the second number to the second line

        lines[2] +=  '-' * (size)+ 4*' ' # add the dashes to the third line

        lines[3] +=  ' '*(size-len(math))+   math + 4*' ' # add the answer to the fourth line

    for i in range(3 + int(show_answers)):
        lines[i] = lines[i].rstrip(' ')# remove trailing whitespace

    
    arranged_math =  "\n".join(lines[i] for i in range(3 + int(show_answers))) #  join the lines together

    return arranged_math # return the arranged math

