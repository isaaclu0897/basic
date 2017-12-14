#文件讀寫接上
text = "ggwp\nhi\nheollo python\ni am pythoner \n"

with open("filelink3.txt", "w") as f:
    f.write(text)

with open("filelink3.txt", "r") as f:
    print(f.read())
