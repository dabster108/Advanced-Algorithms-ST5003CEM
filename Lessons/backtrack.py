class Permutation:
    def permutation(self, s, perm):
        if len(s) == 0:
            print(perm)
            return
        for i in range(len(s)):
            ch = s[i]
            newstr = s[:i] + s[i+1:]
            self.permutation(newstr, perm + ch)

 
new_Perm = Permutation()
new_Perm.permutation("ABC", "")

