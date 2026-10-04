def partial_print(s):
    for ch in s[::2]:
        print(f"^{ch}^", end="")
    print()
