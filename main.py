def pwr(base, pw=5):
    ans = 1
    for i in range(abs(pw)):
        ans = ans*base if (pw>0) else ans/base
        
    return ans


if __name__ == "__main__":
    print(pwr(2, 3))