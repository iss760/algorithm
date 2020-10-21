

class Combination:
    def combination(self, candidates, r):
        for i in range(len(candidates)):
            if r == 1:
                yield [candidates[i]]
            else:
                for nex in self.combination(candidates[i+1:], r - 1):
                    yield [candidates[i]] + nex

    def combination_with_repetition(self, candidates, r):
        for i in range(len(candidates)):
            if r == 1:
                yield [candidates[i]]
            else:
                for nex in self.combination_with_repetition(candidates[i:], r - 1):
                    yield [candidates[i]] + nex

    def combination_sum(self, candidates: list, target: int):
        for i in range(len(candidates)):
            if candidates[i] == target:
                yield [candidates[i]]
            elif candidates[i] < target:
                for nex in self.combination_sum(candidates[i+1:], target-candidates[i]):
                    yield [candidates[i]] + nex

    def combination_with_repetition_sum(self, candidates: list, target: int):
        for i in range(len(candidates)):
            if candidates[i] == target:
                yield [candidates[i]]
            elif candidates[i] < target:
                for nex in self.combination_with_repetition_sum(candidates[i:], target-candidates[i]):
                    yield [candidates[i]] + nex


if __name__ == '__main__':
    cmb = Combination()
    res = cmb.combination_sum([10, 1, 2, 7, 6, 1, 5], 8)
    for i in res:
        print(i)

