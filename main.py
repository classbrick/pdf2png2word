import pdf2png2word.pdf2png as pdf2png
import pdf2png2word.pic2word as pic2word


pdf_path = 'PDF_FILE_NAME/1.pdf'
tool_path= 'tool\\mutool.exe'
pic_path = 'PIC_OUT\\out%d.png'
word_path = 'WORD_OUT/'


def pdf2word(pdf_path, pic_path, tool_path, word_path):
    pdf2png.pdf2jpg(pdf_path, pic_path, tool_path)


if __name__ == '__main__':
    pdf2word(pdf_path, pic_path, tool_path, word_path)
