def ReversePolish(exp):
    if len(exp) == 1:
       return exp[0]
    if len(exp) == 3:
        if exp[0] == "(" and exp[2] == ")":
            return [exp[1]]
        else:
            return [exp[0], exp[2], exp[1]]
    else:
       #bl = [i for i, s in enumerate(exp) if s == "("]
       #br = [i for i, s in enumerate(exp) if s == ")"]
       
       if "(" in exp:
           numbrac = -1
           posini = exp.index("(")
           for i, s in enumerate(exp):
               if s == "(":
                   numbrac += 1
               elif s == ")":
                   if numbrac == 0:
                       posend = i
                       break
                   numbrac -= 1
       return [exp[:posini], ReversePolish(exp[posini+1:posend]), exp[posend+1:]]

expressions = [["(", "a", ")", "+", "(", "b", "*", "c", ")"],
               ["a", "+", "b"],
               ["(", "a", ")"],
               "( a + b ) + c".split(),
               "( ( a ) )".split() ]

for exp in expressions:
    print exp
    print ReversePolish(exp)
