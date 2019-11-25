from PIL import Image
# argparse 库是用来管理命令行参数输入的
import argparse

# 构建命令行参数处理
parper = argparse.ArgumentParser()

# 定义输入文件，输出文件，字符画的宽和高
parper.add_argument('file') #输入文件
parper.add_argument('-o', '--output') #输出文件
parper.add_argument('--width', type=int, default=80) #输出字符画的宽
parper.add_argument('--height', type=int, default=80) #输出字符画的高
# 解析并获取参数
args = parper.parse_args()

# 输入图片的问价路径
IMG = args.file
# 输出字符画的宽度
WIDTH = args.width
# 输出字符画的高度
HEIGHT = args.height
# 输出字符画的路径
OUTPUT = args.output

# 字符画所使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r, g, b, alpha=256):
    # RGB转字符

    # 判断alpha
    if alpha == 0:
        return ' '
    # 获取字符串的长度
    length = len(ascii_char)
    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1)/length
    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]
if __name__ == '__main__':
    # 打开图片并调整图片的宽和高
    im = Image.open(IMG)
    width, height = im.size
    print(width, height)
    # WIDTH, HEIGHT = int(width), int(height)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    # 初始化输出的字符串
    txt = " "
    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历图片每一列
        for j in range(WIDTH):
            #  将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j, i)))
            # 遍历完一行后增加换行符
        txt += '\n'
    print(txt)
    # 字符串输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)


