def reverse(word: str) -> str:
    """reverse given word"""
    revers = word[::-1]
    return revers

if __name__ == "__main__":
    result = reverse('linas')
    print(result)