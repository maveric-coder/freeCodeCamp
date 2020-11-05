def arithmetic_arranger(problems,flag=False):
  
    if len(problems) > 5:
        return "Error: Too many problems."

    line1: str = ""
    line2: str = ""
    line3: str = ""
    line4: str = ""
    for i, problem in enumerate(problems):
        op1, operation, op2 = problem.split(" ")
        if operation not in ['+','-']:
          return "Error: Operator must be '+' or '-'."
        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not op1.isdigit() or not op2.isdigit():
            return "Error: Numbers must only contain digits."
        result = int(op1)+int(op2) if operation=='+' else int(op1)-int(op2)
        l1,l2 = len(op1),len(op2)
        space = max(l1,l2)
        line1 += op1.rjust(space+2)
        line2 += operation + op2.rjust(space+1)
        line3 += ''.rjust(space+2,'-')
        line4 += str(result).rjust(space+2)
        if i<len(problems)-1:
          line1 += '    '
          line2 += '    '
          line3 += '    '
          line4 += '    '
    
    if flag:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        return line1 + '\n' + line2 + '\n' + line3
