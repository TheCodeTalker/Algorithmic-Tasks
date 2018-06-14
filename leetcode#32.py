
'''
# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#

'''
def longestValidParentheses(s):
    longest, last, indices = 0, -1, []
    for i in range(len(s)):
        if s[i] == "(":
            indices.append(i)
        elif not indices:
            last = i
        else:
            indices.pop()
            if not indices:
                longest = max(longest,i - last)
            else:
                longest = max(longest, i - indices[-1])
    return longest




print(longestValidParentheses("(()"))
