print("为了你和他人的安全，严禁酒后开车！")

proof = input("请输入每100毫升血液中的酒精含量：")

if int(proof) < 20:
    print("您还不构成饮酒行为，可以开车，但要注意安全！")
else:
    if 80 > int(proof) >= 20:
        print("已经达到酒后驾驶标准，请不要开车！")
    else:
        print("已经达到醉酒驾驶标准，千万不要开车！！！")

pass
