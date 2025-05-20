from PIL import Image
import os
import sys


def image_to_hex_grid():
    if getattr(sys, 'frozen', False):
        exe_dir = os.path.dirname(sys.executable)
    else:
        exe_dir = os.path.dirname(os.path.abspath(__file__))

    input_path = os.path.join(exe_dir, 'input.png')
    output_path = os.path.join(exe_dir, 'output.txt')

    if not os.path.exists(input_path):
        print(f"错误：请将图片重命名为 'input.png' 并放在EXE同级目录：\n{exe_dir}")
        return

    try:
        img = Image.open(input_path).convert('RGBA')
        img = img.resize((64, 64))
        pixels = img.load()

        all_hex = []
        for y in range(64):
            for x in range(64):
                r, g, b, a = pixels[x, y]
                all_hex.append(f"{r:02x}{g:02x}{b:02x}{a:02x}")

        # 每16个一组合并成一个字符串
        hex_blocks = [''.join(all_hex[i:i + 16]) for i in range(0, len(all_hex), 16)]

        with open(output_path, 'w', encoding='utf-8') as f:
            for idx, block in enumerate(hex_blocks):
                end_char = '),\n' if idx != len(hex_blocks) - 1 else ')'
                f.write(f'自定义字符串(\n\t\t"{block}"{end_char}\n')
                print(f'自定义字符串(\n\t\t"{block}"{end_char}\n')

    except Exception as e:
        print("发生错误:", str(e))


# 调用函数
image_to_hex_grid()
