import binascii
import os


def convert_file(filepath):
    filename_parts = filepath.split('\\')[-1].split('.')
    filename = '.'.join(filename_parts[:-1])

    with open(filepath, 'rb') as input_file:
        word = input_file.read(1)
        output_filename = filename + '.js'
        with open(output_filename, 'w') as output_file:
            output_file.write(f"const {filename} = new Uint8Array([")
            while word:
                output = binascii.hexlify(word)
                output_file.write("0x%s," % output.decode('utf-8'))
                word = input_file.read(1)
            output_file.write("]);")

    print(f"转换完成，输出文件位于：{os.path.abspath(output_filename)}")

    folder_path = os.path.dirname(os.path.abspath(output_filename))
    os.startfile(folder_path)


while True:
    filepath = input("请输入要转换的文件的绝对路径，或输入 N 退出程序：")
    if filepath.lower() == 'n':
        break

    try:
        convert_file(filepath)
    except Exception as e:
        print(f"出现错误：{e}")
