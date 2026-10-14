"""
Number of Students Unable to Eat Lunch (NeetCode)
=================================================

The school cafeteria offers circular and square sandwiches at lunch break,
referred to by numbers 0 and 1 respectively. All students stand in a queue.
Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students.
The sandwiches are placed in a stack. At each step:
    - If the student at the front of the queue prefers the sandwich on the top
      of the stack, they will take it and leave the queue.
    - Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich
and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is
the type of the ith sandwich in the stack (i = 0 is the top of the stack) and
students[j] is the preference of the jth student in the initial queue (j = 0 is
the front of the queue). Return the number of students that are unable to eat.

Example 1:
    Input:  students = [1,1,0,0], sandwiches = [0,1,0,1]
    Output: 0

Example 2:
    Input:  students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
    Output: 3

Constraints:
    1 <= students.length, sandwiches.length <= 100
    students.length == sandwiches.length
    sandwiches[i] is 0 or 1.
    students[i] is 0 or 1.
"""

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # using hashmap
        # ORDER OF STUDENTS IS NOT IMPORTANT
        # ORDER OF SANDWICHES IS
        student_dict = {}

        for s in students:
            if s in student_dict:
                student_dict[s] += 1
            else:
                student_dict[s] = 1
        
        for sandwich in sandwiches:
            if sandwich in student_dict and student_dict[sandwich]>0:
                student_dict[sandwich] -= 1
            else:
                break
        
        sandwich_left = student_dict.get(0,0)+student_dict.get(1,0)
        return sandwich_left