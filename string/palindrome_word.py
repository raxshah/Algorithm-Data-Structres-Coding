#recursive solution for if given string is palindrome or not

def isPalindrome(st):
    def helper(st, s, e) : 
        # If there is only one character 
        if (s > e): 
            return True
        if (st[s] != st[e]): 
            return False
        return helper(st, s + 1, e - 1)
    
    n = len(st)
    if not n:
        return True
    return helper(st,0,n-1)

# Driver Code 
st = "abccba"
if (isPalindrome(st)) : 
	print("Yes")
else : 
	print("No")
