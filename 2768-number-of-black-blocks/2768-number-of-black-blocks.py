class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        coord_set = set([tuple(coords) for coords in coordinates])
        seen = set()

        ans = [0] * 5

        for x, y in coordinates:
            for i in range(x - 1, x - 1 + 2):
                for j in range(y - 1, y - 1 + 2):
                    count = 0
                    valid = True
                    for possible_x in range(2):
                        for possible_y in range(2):
                            if i + possible_x >= m or i + possible_x < 0 or j + possible_y >= n or j + possible_y < 0 or (i + possible_x, j + possible_y) in seen:
                                valid = False
                                break
                            if (i + possible_x, j + possible_y) in coord_set:
                                count += 1
                    if valid:
                        ans[count] += 1
            seen.add((x, y))

        ans[0] = (m - 1) * (n - 1) - sum(ans[1:])

        return ans

    