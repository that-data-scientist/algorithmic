import unittest


def levenshteinDistance(str1, str2):
    dp = [[-1 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    dp[0][0] = 0

    for j in range(1, len(str1) + 1):
        dp[0][j] = j

    for i in range(1, len(str2) + 1):
        dp[i][0] = i

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i - 1][j - 1],
                    dp[i][j - 1]
                )
    return dp[len(str2)][len(str1)]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(levenshteinDistance("abc", "yabd"), 2)
