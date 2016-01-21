def ReversePolish(exp):
    print repr(exp)
    
    if len(exp) == 1 and isinstance(exp[0], basestring):
#       print exp[0]
       return exp
    elif len(exp) == 1:
#       print exp[0]
       return ReversePolish(exp[0])
    elif len(exp) == 3:
        if exp[0] == "(" and exp[2] == ")":
            return ReversePolish(exp[1])
        else:
            return ' '.join([ReversePolish(exp[0]), ReversePolish(exp[2]), exp[1]])
    else:       
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
           print "to reverse", exp[:posini] + exp[posini+1:posend] + exp[posend+1:]
           #print exp[:posini] + ReversePolish(exp[posini+1:posend]) + exp[posend+1:]
           return ReversePolish(exp[:posini] + [exp[posini+1:posend]] + exp[posend+1:])

expressions = ["a".split(),
               "a + b".split(),
               "( a )".split(),
               "( ( a ) )".split(),
               "( ( ( a ) ) )".split(),
               "( a + b ) + c".split(),
               "a + ( b + c )".split()
                ]

for exp in expressions:
    print ReversePolish(exp)
