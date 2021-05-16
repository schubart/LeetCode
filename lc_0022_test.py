from lc_0022 import Solution


def test_examples():
    s = Solution()

    assert s.generateParenthesis(1) == ["()"]
    assert set(s.generateParenthesis(2)) == {"(())", "()()"}
    assert set(s.generateParenthesis(3)) == {
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    }
    assert set(s.generateParenthesis(4)) == {
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()",
    }
    assert len(s.generateParenthesis(5)) == 42
    assert len(s.generateParenthesis(6)) == 132
    assert len(s.generateParenthesis(7)) == 429
    assert len(s.generateParenthesis(8)) == 1430
