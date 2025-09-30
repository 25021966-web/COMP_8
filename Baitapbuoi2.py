#W2A3
a, b = map(int, input("Nhập hai số nguyên a và b (cách nhau bằng khoảng trắng): ").split())

print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)
print("Phần nguyên:", a // b)
print("Phần dư:", a % b)
print("Chia thực: {:.2f}".format(a / b))

#W2A4
a1, b1, c1, a2, b2, a3 = map(float, input().split())
TB = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
print("{:.1f}".format(TB))

#W2A5
a, b = map(int, input("Nhập vào a, b:").split())
print("Kết quả: ", a ** b)

#W2A6
ch = input("Nhập một ký tự thường (a-z): ")
print("Mã Unicode:", ord(ch))
print("Ký tự hoa:", ch.upper())

#W2A7
A = ((13 ** 2) * 3) + 5
B = 13 ** 2 * 3 + 5
print("A =", A)
print("B =", B)

#W2A8
C = float(input("Nhập nhiệt độ C: "))
F = 9/5 * C + 32
print("Nhiệt độ F:", round(F, 2))

#W2A9
x = float(input("Nhập giá đồng hồ (USD): "))
shipping = 10
base_price = x + shipping
total = base_price * 1.4
print("Tổng số tiền phải trả (USD):", round(total, 2))

#W2A11
h, m = map(int, input("Nhập giờ và phút (cách nhau bằng khoảng trắng): ").split())
seconds = h * 3600 + m * 60
print(seconds)

#W2A12
n = int(input("Nhập cạnh Rubik: "))
stickers = 6 * n * n
print(stickers)

#W2A13
a, b = map(int, input("Nhập vào hai số nguyên dương a và b: ").split()) 
if a <= 0 or b <= 0:
    print("Nhập hai số nguyên dương!!!")
else:
    hang_don_vi = (a * b) % 10
    print("Hàng đơn vị của tích a * b là:", hang_don_vi)

#W2A14
a, b = map(int, input("Nhập a và b: ").split())
a, b = b, a
print(a, b)

#W2A15
n = int(input("Nhập n: "))
star_number = 3 * n * (n - 1) + 1
print(star_number)