def roundGrade(grades):
   grade_groups = [-3,0,2,4,7,10,12]
   gradesRounded = [min(grade_groups,key=lambda x:abs(grade-x)) for grade in     grades]
   return gradesRounded
print(roundGrade([2,1,8,-2,9.2,3]))
