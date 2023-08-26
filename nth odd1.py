class a:
    
    def nth(self,n):

        #create a function
        def isdigi(nu):
            for i in str(nu):
                if int(i)%2 != 0:
                    return False
            return True
        
        
        num  = 2*n - 1
        if isdigi(num):
            return num
        else:
            return self.nth(n+1)     #failed due to recursion times exceeds
t = a()

print(t.nth(int(input("enter the number"))))
