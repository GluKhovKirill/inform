def pwr(base, pw=5):
    ans = 1
    
    for i in range(abs(pw)):
        ans = ans*base if (pw>0) else ans/base
        
    return ans


pwr_via_lambda = lambda base,power: base**power

if __name__ == "__main__":
    print(pwr(2, 3))
    print(pwr_via_lambda(2,5))