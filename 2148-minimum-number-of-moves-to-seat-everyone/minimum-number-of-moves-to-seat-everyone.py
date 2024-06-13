class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        c = 0
        for i in range(len(seats)):
            while seats[i] != students[i]:
                c += 1
                if students[i] > seats[i]:
                    students[i] -= 1
                else:
                    students[i] += 1

        return c