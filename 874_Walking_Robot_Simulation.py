class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        STEPS = len(commands)
        Dir = 0
        ans = 0
        x = 0
        y = 0
        for STEP in range(STEPS):
            if commands[STEP] < 0:
                if commands[STEP] == -2:
                    Dir = (Dir + 3) % 4
                elif commands[STEP] == -1:
                    Dir = (Dir + 1) % 4
            else:
                i, j = DIR[Dir]
                if i != 0:
                    ostacle = [ostacle[0] for ostacle in obstacles if ostacle[1] == y and (ostacle[0] - x) / i > 0]
                    ostacle.append(x + i * commands[STEP] + i)
                    if i > 0:
                        x = min(ostacle) - 1
                    else:
                        x = max(ostacle) + 1
                elif j != 0:
                    ostacle = [ostacle[1] for ostacle in obstacles if ostacle[0] == x and (ostacle[1] - y) / j > 0]
                    ostacle.append(y + j * commands[STEP] + j)
                    if j > 0:
                        y = min(ostacle) - 1
                    else:
                        y = max(ostacle) + 1

                ans = max(ans, pow(x, 2) + pow(y, 2))
        
        return ans
