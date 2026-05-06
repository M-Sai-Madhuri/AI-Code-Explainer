def get_prompt(code, mode):
    if mode == "Beginner":
        return f"""
Explain this code in simple terms:
- Use easy language
- Give real-life analogy
- Explain line-by-line

Code:
{code}
"""

    elif mode == "Advanced":
        return f"""
Explain this code in depth:
- Step-by-step logic
- Time & space complexity
- Best practices

Code:
{code}
"""

    elif mode == "Debug":
        return f"""
Analyze this code:
- Find bugs
- Suggest fixes
- Optimize performance

Code:
{code}
"""