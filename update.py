student_score= {"Harry":81,"Kat":75,"Tina":45,"Priya":16,"Preety":95}

#need to update the number value to qualitative value

for keys,values in student_score.items():
    if 100>values>=91:
        student_score.update({keys:"Outstanding"})
    elif 90>values>=80:
        student_score.update({keys:"Exceeds Expectation"})
    elif 80>values>=71:
        student_score.update({keys:"Acceptable"})
    else:
        student_score.update({keys:"Fail"})

print(student_score)