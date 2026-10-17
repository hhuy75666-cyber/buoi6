#bai1
import random
ket_qua = random.randint(1, 6)
print(f"Kết quả gieo xúc xắc: {ket_qua}")

#bai2
kitu = random.choice(["NguyenVanA"])
print(f"Kết quả chọn ký tự: {kitu}")

#bai3
danhsachdongtu = ["Cool", "Fast", "Smart", "Happy"]
danhsachtinhtu = ["Tiger", "Eagle", "Panda", "Coder"]
tinhtu = random.choice(danhsachdongtu)
danhtu = random.choice(danhsachtinhtu)
username = tinhtu + danhtu
print(f"Username ngẫu nhiên của bạn là: {username}")

#bai4
ma_pin = ""
for _ in range(4):
    chu_so_ngau_nhien = str(random.randint(0, 9))
    ma_pin += chu_so_ngau_nhien
print(f"Mã PIN ngân hàng ngẫu nhiên của bạn là: {ma_pin}")

#bai5
cau = input("Nhập câu: ")
dsachtu= cau.split()
random.shuffle(dsachtu)
ketqua = " ".join(dsachtu)
print("Ket qua:", ketqua)