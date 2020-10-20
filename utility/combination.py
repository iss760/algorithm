

class Combination:
    def combination(self, candidates, r):
        for i in range(len(candidates)):
            if r == 1:
                yield [candidates[i]]
            else:
                for nex in self.combination_with_repetition(candidates[i+1:], r - 1):
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
                for nex in self.combination_sum(candidates[i:], target-candidates[i]):
                    yield [candidates[i]] + nex


if __name__ == '__main__':
    cmb = Combination()
    for i in cmb.combination([2, 3, 5, 6], 2):
        print(i)

    res = cmb.combination_with_repetition([2, 3, 5, 6], 2)
    print(res)
    print('a')