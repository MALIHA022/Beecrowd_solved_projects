# sentence = input()
# even = []
# odd = []
# new = ""
# for alp in sentence:
#     if alp != " ":
#         new+=alp
#
# for alp_e in range(0,len(sentence),2):
#         even.append(sentence[alp_e])
# for alp_o in range(1,len(sentence),2):
#         odd.append((sentence[alp_o]))
#
# dancing_sentence = ""
# even_index = 0
# odd_index = 0
# for i in sentence:
#     if i == " ":
#         dancing_sentence += ""
#     else:
#         if even_index < len(even):
#             dancing_sentence += even[even_index].upper()
#             even_index += 1
#
#         if odd_index < len(odd):
#             dancing_sentence += odd[odd_index].lower()
#             odd_index += 1
#
# print(dancing_sentence)

while True:
    try:
        sentence = input()
        result = ""
        flag = True
        for ch in sentence:
            if ch != " ":
                if flag:
                    result += ch.upper()
                    flag = False
                else:
                    result += ch.lower()
                    flag = True
            else:
                result += " "
        print(result)
    except:
        break

