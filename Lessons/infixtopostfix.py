# Convert infix to postfix expression

from stacks import Stack
class InfxToPostfix:
    @staticmethod
    def precedence (ch):
        if (ch=='^'):
            return 3
        elif (ch=='*' or ch=='/'):
            return 2
        elif (ch=='+' or ch=='-'):
            return 1
        else:
            return -1 
        

    def convertPostfix (self, exp):
        stk = Stack ()
        result = []
        for ch in exp:
            if (self.precedence (ch) > 0):
                # case operator
                while (not stk.isEmpty () and self.precedence (ch) <= self.precedence (stk.peek()) ):
                    result.append (stk.pop ())
                stk.push (ch)
            else:
                # operand or bracket
                if (ch== '('):
                    stk.push (ch)
                elif (ch== ')'):
                    x= stk.pop()
                    while (x!= '('):
                        result.append (x)
                        x= stk.pop()
                else:
                    result.append (ch)