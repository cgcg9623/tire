def finding_GCD(a, b):
    # 12 18 / while로 1부터 시작 나눠서 소수점 안나올때까지 해당 숫자 divider
    while(b != 0):
        result = b  # 1) a= 12, b = 18 , result = 18 / 2) a = 18, b = 12, result = 12 / 3) a = 12, b=6 , result =6
        a, b = b, a % b # a= 18, b = 12 / 2) a= 12, b = 6 / 3) a= 6, b = 12 % 6 
    return result

def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_GCD(number1,number2) == 3)
    print("테스트통과")

if __name__ == "__main__":
    test_finding_gcd()