from collections import deque

class Solution:
    def canMeasureWater(self, x, y, z):
        if z == 0:
            return True
        if x + y < z:
            return False

        fringe = deque()
        fringe.append((0, 0))
        visited = set()
        visited.add((0, 0))

        while fringe:
            a, b = fringe.popleft()

            if a == z or b == z or a + b == z:
                return True

            states = [
                (x, b),
                (a, y),
                (0, b),
                (a, 0),
            ]

            t = min(a, y - b)
            states.append((a - t, b + t))

            t = min(b, x - a)
            states.append((a + t, b - t))

            for s in states:
                if s not in visited:
                    visited.add(s)
                    fringe.append(s)

        return False


        