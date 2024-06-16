var5 = list("aaa")
var3 = list("aaa")
var4 = list("aaa")
var2 = list("aaa")

var5[0] = chr(ord(var5[0]) + 4)
var5[1] = chr(ord(var5[1]) + 19)
var5[2] = chr(ord(var5[2]) + 18)

var3[0] = chr(ord(var3[0]) + 7)
var3[1] = chr(ord(var3[1]) + 0)
var3[2] = chr(ord(var3[2]) + 1)

var4[0] = chr(ord(var4[0]) + 0)
var4[1] = chr(ord(var4[1]) + 11)
var4[2] = chr(ord(var4[2]) + 15)

var2[0] = chr(ord(var2[0]) + 14)
var2[1] = chr(ord(var2[1]) + 20)
var2[2] = chr(ord(var2[2]) + 15)

res = "".join(var4 + var3 + var5 + var2)
print(res)