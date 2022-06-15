
expression = ["0", "+", "1", "=" , "1"]
onetoten = ["0", "1", "2", 
            "3", "4", "5",
            "6", "7", "8"
            "9", "10"]
ops = ["-", "=", "+", "/"]
mapdigit = {"0" : 0, "1" : 1 , "2" : 2
            "3" : 3, "4" : 4, "5" : 5, "6" : 6
            "7" : 7, "8" : 8, "9" : 9, "10" : 10}
def checkdigit(expression, position):
    item = expression[position]
    if( item in onetoten):
        return item
    else:
        return ""
def getPlus(expression):
    scan = 0 
    for scan in range(len(expression)):
        if(expression[scan] == "+"): 
            if(checkdigit(expression, scan - 1) != ""):
                left = expression[scan - 1]
            if(checkdigit(expression, scan + 1) != ""):
                right = expression[scan + 1]
                tree = ["+", [left, right]]
                return tree
            else:
                return ""
tree = getPlus(expression)
root = tree[0] 
left = tree[1][0]
right = tree[1][1]
print(getPlus(expression))
         

        
        
