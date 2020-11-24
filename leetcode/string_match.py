
def func(s, dict):

    def helper(word, path, ans):
        if not word:
            ans.append(path)
            return
        for end in range(1, len(word) + 1):
            if word[:end] in dict:
                helper(word[end:], path + ' ' + word[:end], ans)

    ans = []
    helper(s, '', ans)
    return ans


print(func("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
