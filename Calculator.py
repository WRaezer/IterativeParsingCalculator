
expression = ["0", "+", "1", "=" , "1"]
onetoten = ["0", "1", "2", 
            "3", "4", "5",
            "6", "7", "8"
            "9", "10"]
ops = ["-", "=", "+", "/"]
def checkdigit(expression, position):
    item = expression[position]
    if( item is in onetoten):
        return item
    else:
        return ""
def checkop(expression, position):
    item = expression[position]
    if( item is in ops):
        return item
    else:
         return "" 
def getPlus(expression):
    scan = 0 
    for scan in range(len(expression)):
        if(checkop(expression[scan] == "+", scan)): 
            if(checkdigit(expression, expression[scan - 1]) != ""):
                left = expression[scan - 1]
            if(checkdigit(expression, expression[scan + 1]) != ""):
                right = expression[scan + 1]
                tree = ["+", [left, right]]
                return tree
            else:
                return ""

print(getPlus(expression))
         
        
        
