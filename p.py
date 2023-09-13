def issubstr(str1,str2):
    strsiz1=len(str1)
    strsiz2=len(str2)
    if strsiz1==0:
        return False
    if strsiz2==0:
        return True
    if str1[0]==str2[0]:
        return isexact(str1,str2)
    else:
        return issubstr(str1[1:],str2)
    
def isexact(str1,str2):
    strsiz1=len(str1)
    strsiz2=len(str2)
    if strsiz1==0:
        return False
    if strsiz2==0:
        return True
    if str1[0]==str2[0]:
        return isexact(str1[1:],str2[1:])

str1=input('enter string1 : ')
str2=input('enter string2 : ')
print(issubstr(str1,str2))

    
    