gradeList = [[89, 90, 86, 95, 95, 91],
			 [75, 77, 75, 81, 88, 65], 
			 [100, 90, 91, 94, 95, 93]]

student1 = sum(gradeList[0])/6
student2 = sum(gradeList[1])/6
student3 = sum(gradeList[2])/6
print("The average of student 1 is: {}".format(sum(gradeList[0])/6))
print("The average of student 2 is: {}".format(sum(gradeList[1])/6))
print("The average of student 3 is: {}".format(sum(gradeList[2])/6))
print("The class average is: {}".format((student1 + student2 + student3)/3))