class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1

        count = 0
        visited.add("0000")
        d = deque(["0000"])

        while d:
            for i in range(len(d)):
                s = d.popleft()
                if s == target:
                    return count

                for i in range(4):
                    for delta in (1, -1):
                        digit = (int(s[i]) + delta) % 10
                        nxt = s[:i] + str(digit) + s[i + 1:]
                        if nxt not in visited:
                            d.append(nxt)
                            visited.add(nxt)
            count += 1
        return -1