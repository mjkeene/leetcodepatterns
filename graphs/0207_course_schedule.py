class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency list to represent the dependencies (prereqs) for each course
        prereq_map = {course: [] for course in range(num_courses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # This represents the nodes visited in the current dfs traversal
        visit_set = set()

        def dfs(course):
            # This means there is a cycle in the dependency graph, not possible to complete courses
            if course in visit_set:
                return False
            # No prereqs means the course is a base case and can be completed
            if prereq_map[course] == []:
                return True

            # Add course to current dfs traversal visited set for cycle detection
            visit_set.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            # Set prereqs to empty list to avoid duplicate traversal later, and remove from visit_set
            prereq_map[course] = []
            visit_set.remove(course)
            return True

        # Traverse all nodes since there can be nodes that are not connected
        # e.g., 1 -> 2, 3 -> 4
        for course in range(num_courses):
            if not dfs(course):
                return False

        return True
