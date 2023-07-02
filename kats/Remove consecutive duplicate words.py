# def remove_consecutive_duplicates(s):
#     new_str = s.split()
#     lis = []
#     for i in new_str:
#         if len(lis) != 0:
#             if i == lis[-1]:
#                 continue
#             else:
#                 lis.append(i)
#         else:
#             lis.append(i)
#     string1 = ''
#     for ind in range(len(lis)):
#         string1 += " " + lis[ind]
#     new_string1 = string1.strip(" ")
#     return new_string1
#print( remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))




# def remove_consecutive_duplicates(s):
#     lis = []
#     for i in s.split():
#         if len(lis) != 0:
#             if i == lis[-1]:
#                 continue
#             else:
#                 lis.append(i)
#         else:
#             lis.append(i)
#     return " ".join(lis)
# print( remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))








