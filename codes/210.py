class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        result = []
        courses = set(range(numCourses))
        prerequisite_courses = set()
        advanced_courses = {}

        for prerequisite in prerequisites:
            advanced_courses.setdefault(prerequisite[0], set()).add(prerequisite[1])
            prerequisite_courses.add(prerequisite[1])

        result.extend(courses - set(advanced_courses.keys()) - prerequisite_courses)
        while prerequisite_courses:
            for prerequisite_course in prerequisite_courses:
                if prerequisite_course not in advanced_courses:
                    learned = prerequisite_course
                    # print 'learned', learned
                    break
            else:
                return []

            prerequisite_courses.remove(learned)
            result.append(learned)

            for course in advanced_courses.keys():
                courses = advanced_courses[course]
                courses.discard(learned)
                if len(courses) == 0:
                    advanced_courses.pop(course)
                    if course not in prerequisite_courses:
                        result.append(course)
        result.extend(advanced_courses.keys())
        return result


solution = Solution()
print solution.findOrder(2, [[1, 0]])
print solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
