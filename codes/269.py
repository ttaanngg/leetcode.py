class Solution(object):
    def alienOrder(self, words):
        relations = {}
        alphas = set()
        next_turn = range(1, len(words))
        count = 0
        while next_turn:
            tmp = []
            if len(words[next_turn[0]]) > count + 1:
                tmp.append(next_turn[0])
            for i in range(len(next_turn)):
                a = words[next_turn[i - 1]][count]
                b = words[next_turn[i]][count]
                alphas.add(a)
                alphas.add(b)
                if len(words[next_turn[i]]) > count + 1:
                    tmp.append(next_turn[i])
                if a == b:
                    continue
                if a in relations and b in relations[a] and next_turn[i - 1] + 1 != next_turn[i]:
                    continue
                relations.setdefault(b, set()).add(a)
            count += 1
            next_turn = tmp
        print alphas
        print relations
        result = []
        while alphas:
            for a in alphas:
                if a not in relations:
                    result.append(a)
                    break
            else:
                return ""

            alphas.remove(a)
            length_before_done = len(relations)
            for k in relations.keys():
                r = relations[k]
                r.discard(a)
                if not r:
                    relations.pop(k)
                else:
                    relations[k] = r
            if length_before_done and length_before_done == len(relations):
                return ""

        return ''.join(result)


solution = Solution()
print solution.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
print solution.alienOrder(['z', 'x', 'z'])
print solution.alienOrder(["a", "b", "ca", "cc"])
print solution.alienOrder(["zy", "zx"])
