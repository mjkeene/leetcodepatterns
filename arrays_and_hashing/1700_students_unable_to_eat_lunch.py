from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # order of students doesn't really matter; they will come back and repeat
        # order of sandwiches does matter; they must be served in specific order

        # create mapping of sandwich preference to number of students, decremenet
        # when a sandwich is taken, return remaining amount
        student_mapping = Counter(students)
        res = len(students)

        for s in sandwiches:
            if student_mapping[s] > 0:
                res -= 1
                student_mapping[s] -= 1
            else:
                # no student can eat sandwich
                return res
        return 0