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