def check_parentheses(a_lsit):
    stack = []
    for i in a_lsit:
        if i == "(":
            stack.append(i)
        elif i ==")":
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True

print(check_parentheses("()()()"))  #True
print(check_parentheses("()())"))   #False
print(check_parentheses("()()"))    #True
print(check_parentheses("))"))      #False

