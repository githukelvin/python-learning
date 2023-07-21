# student_scores = input("input a list of student Scres").split(",")
# for n in range(0,len(student_scores)):
#     student_scores[n]=int(student_scores[n])
# print(student_scores)
#
# numOfStudents=len(student_scores)
# highestScore=0
# # currentScore=0
# # nextScore  = 0
# # for i in range(0,numOfStudents):
# #     currentScore=student_scores[i]
# #     if (i+1) > (numOfStudents-1):
# #         nextScore=student_scores[i]
# #     elif i < numOfStudents:
# #         nextScore= student_scores[i+1]
# #
# #         if highestScore >= currentScore:
# #             if nextScore >= highestScore:
# #                 highestScore = nextScore
# #         else:
# #             if currentScore >= nextScore:
# #                 highestScore = currentScore
# for score in student_scores:
#     if score >highestScore:
#         highestScore=score
# print(f"The highest score is {highestScore}")


total =0

for number in range(2,101,2):
    total +=number

print(total)





