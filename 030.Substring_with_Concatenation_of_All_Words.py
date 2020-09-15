# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once,
# in any order, and without any intervening characters.
# You can return the answer in any order.

# Example 1:
#   Input: s = "barfoothefoobarman", words = ["foo","bar"]
#   Output: [0,9]
#   Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
#   The output order does not matter, returning [9,0] is fine too.
# Example 2:
#   Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
#   Output: [8]
# Example 3:
#   Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
#   Output: [6,9,12]

from itertools import permutations


class Solution:
    def findSubstring(self, s, words):
        """
        :param s: str
        :param words: list[str]
        :return: list[int]
        """
        word_len = len(words[0])
        res = []
        # 입력 문장 순환
        for i in range(len(s)):
            temp = words.copy()     # 깊은복사
            # 단어 순환 탐색
            for j in range(i, len(s), word_len):
                string = s[j:j+word_len]
                # 단어장에 없을 경우
                if string not in temp:
                    break
                temp.remove(string)     # 찾은 단어 단어장에서 제거
            # 모든 단어 사용 했을 경우
            if not temp:
                res.append(i)

        return res



sol = Solution()
#print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(sol.findSubstring2("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
#print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
print(sol.findSubstring2("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]))