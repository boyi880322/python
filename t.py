name = input("姓名：")
while name != "":
    h = float(input("身高（公尺）："))
    w = int(input("體重（公斤）："))
    BMI = w / h ** 2
    print("{}的BMI是：{}".format(name, BMI))
    name = input("姓名：")