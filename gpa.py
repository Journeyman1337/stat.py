# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

A = 0
B = 1
C = 2
D = 3
F = 4

def gpa(quality_points, credit_hours, grades):
    assert len(quality_points) == 5
    assert len(grades) == len(credit_hours)
    gpa = 0
    for course_i in range(0, len(grades)):
        gpa += quality_points[grades[course_i]] * credit_hours[course_i]
    gpa /= sum(credit_hours)
    return gpa