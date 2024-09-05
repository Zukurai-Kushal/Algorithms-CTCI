def printM(M):
    for slice in M:
        print(slice)

def turn90Deg(M):
    n = len(M)
    for layer in range (0,n//2):
        for index in range(layer,n-layer-1):
            temp = M[index][-layer-1]
            M[index][-layer-1] = M[layer][index]
            M[layer][index] = M[-index-1][layer]
            M[-index-1][layer] = M[-layer-1][-index-1]
            M[-layer-1][-index-1] = temp
            # print("\n(layer, index): ",layer,',',index)
            # print("4 Points: ",M[index][-layer-1],M[layer][index],M[-index-1][layer],M[-layer-1][-index-1])
            # printM(M)
    return M

matrixInput = [['A','B','C','D'],
         ['E','F','G','H'],
         ['I','J','K','L'],
         ['M','N','O','P']]

# printM(matrixInput)
# print(" ")
# printM(turn90Deg(matrixInput))

def isSubString(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    for i in range(len(s2)):
        if(s1_length > s2_length-i):
            break
        if(s2[i] == s1[0]):
            for j in range(len(s1)):
                if(s1[j] != s2[i+j]):
                    break
                if(j == len(s1)-1):
                    return True
    return False
# O(M*N)

def stringRotate_1(s1, s2):
    for i in range(len(s2)):
        if(s1[0] == s2[i] and isSubString(s2[0:i], s1)):
            for j in range(i, len(s2)):
                if(s1[j-i] != s2[j]):
                    break
                if(j == len(s2)-1):
                    return True
    return False
# O(M*(O(isSubString()))*M)

def stringRotate_2(s1, s2): # xyxy (s1+s1) -> yx (s2)
    if(len(s1) != len(s2)):
        return False
    if(isSubString(s2, s1+s1)):
        return True
    else:
        return False
# O(O(isSubString)) -> best implementation: O(n)

#print(stringRotate_2("waterbottle","erbottlewat"))
    