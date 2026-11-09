f = open("nhat_ky.txt", "w", encoding="utf-8")
f.write("Giao dịch thành công")

f.close()



# with open(r"E:\Code\Python\Learn\Code\test\test.txt", "a", encoding="utf-8") as f:
#     f.write("\nTôi không thể bị thay thế")
#     print(f.read())

# with open("nhat_ky_he_thong.txt", "x", encoding="utf-8" ) as f:
#     print(f.read())

# f = open("nhat_ky_he_thong.txt", "x")

with open(r"E:\Code\Python\Learn\Code\test\test.txt", "r", encoding="utf-8") as f:
    print(f.readline())
