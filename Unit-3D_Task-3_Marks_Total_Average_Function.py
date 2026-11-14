def total_and_average(subject_1_marks, subject_2_marks, subject_3_marks):
    tot = subject_1_marks + subject_2_marks + subject_3_marks
    avg = tot / 3
    return tot, avg

m1, m2, m3 = 60, 70, 80
total, average = total_and_average(m1, m2, m3)
print("Total marks:", total)
print("Average marks:", average)
