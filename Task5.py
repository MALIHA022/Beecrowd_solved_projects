# Medium Task 2
while True:
    try:
        n = input()
        ch = [" ", ","]
        non_neg = ["0","1","2","3","4","5","6","7","8","9","o","O","l"]
        list1 = []
        newstr = ""
        for k in n:
            if k in ch:
                pass
            else:
                newstr += k

        output = ""
        new = newstr
        count = 0
        if new.isdigit():
            new1 = int(newstr)
            if new1 > 2147483647:
                print("error")
            else:
                print(new1)
        else:
            for chars in newstr:
                if chars not in non_neg:
                    count += 1
                else:
                    pass
            a = False
            for i in newstr:
                if i in non_neg:
                    a = True
                    break
                else:
                    a = False
            if count < 1:
                if a == True:
                    for l in newstr:
                        if l != "," or l != " ":
                            if l == "o" or l == "O":
                                output += '0'
                            elif l == "l":
                                output += "1"
                            elif l != 'o' or l != 'O' or l != 'l':
                                output += l
                        else:
                            pass
                    print(int(output))
                else:
                    print("error")
            else:
                print("error")
    except:
        break