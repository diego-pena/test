def operate(exp, n):
    #Obtain first and last indexes of part evaluated
    i_f = (n-1)*5
    i_l = (n-1)*5 + 9

    #Evaluate part
    new_numb = str(eval(exp[i_f:i_l]))

    #Add blanc spaces so it has 3 char
    new_numb = normalize(new_numb)

    #Generate new string of operations
    if i_f > 0:
        new_exp = exp[0:i_f]+new_numb
    else:
        new_exp = new_numb

    if i_l < len(exp):
        new_exp = new_exp + exp[i_l:len(exp)]
    else:
        new_exp = new_exp

    return new_exp

def normalize(numb):
    while len(numb)<4:
        numb = ' ' + numb

    return numb

def recursive_operation(exp,sequence):
    for i in range(0, 7):
        # print(exp)
        exp = operate(exp, sequence[i])
    return exp

exp = '   7-   2*   5-   3*   3+   5*   3' #three spaces per number
#exp  = '   5-   2*   2*  12-   3*   3+  15-   4'
num = 31
print(recursive_operation(exp,[1, 1, 2, 3, 1, 1, 1]))
#for i_1 in range(1, 7):
for i_2 in range(1, 7):
    for i_3 in range(1, 6):
        for i_4 in range(1, 5):
            for i_5 in range(1, 4):
                for i_6 in range(1, 3):
                    #print([i_2,i_3,i_4,i_5,i_6,1,1])
                    #print(recursive_operation(exp,[i_1,i_2,i_3,i_4,i_5,i_6,1,1]))
                    if num == int(recursive_operation(exp,[i_2,i_3,i_4,i_5,i_6,1,1])):
                        seq = [i_2,i_3,i_4,i_5,i_6,1,1]
                        print(str(seq))