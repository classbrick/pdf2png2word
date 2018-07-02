import os

def pdf2jpg(pdf_path, tool_path= 'tool\\mutool.exe', pic_path = 'PIC_OUT\\out%d.png'):
    os.system(tool_path + ' draw -o ' + pic_path + ' '+ pdf_path)


if __name__ == '__main__':
    pdf_path = 'D:/Users/zhengnan.luo/PycharmProjects/pdf2png2word/pdf2png2word/PDF_FILE_NAME/1.pdf'
    pdf2jpg(pdf_path)

