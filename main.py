def pwr(base, pw=5):
    ans = 1
    for i in range(pw):
        ans *= base
    return ans


if __name__ == "__main__":
    print(pwr(2, 3))