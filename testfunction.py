def fun(str1):
	str1.append( "hello")
	print str1, id(str1)

str1 = ["helloworld"]
print str1, id(str1)

fun(str1)

print str1, id(str1)


str2 = "1111"
print str2, id(str2)
str2 += "2222"
print str2, id(str2)
str2 += "3333"
print str2, id(str2)

