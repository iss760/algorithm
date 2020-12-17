import re


def is_valid_palindrome(s):
    # 전처리: 문자만 추출, 소문자로 변환(대소문자 구분 x 이므로)
    s = [_s.lower() for _s in s if _s.isalnum()]

    # 회문 판별
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True


def is_valid_palindrome2(s):
    # 전처리
    s = s.lower()    # 소문자로 변환(대소문자 구분 x 이므로)
    s = re.sub('[^a-z0-9]', '', s)    # 정규표현식으로 영문자 숫자만 남김

    return s == s[::-1]


print(is_valid_palindrome("man :aba,n : am"))
print(is_valid_palindrome2("man :aba,n : am"))
