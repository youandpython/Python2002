import datetime
import os
import fitz  # fitz就是pip install PyMuPDF


def py_mu_pdf_fitz(pdf_path, image_path):
    start_time_pdf2img = datetime.datetime.now()  # 开始时间

    print("image_path=" + image_path)
    pdf_doc = fitz.open(pdf_path)
    for pg in range(pdf_doc.pageCount):
        page = pdf_doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(image_path):  # 判断存放图片的文件夹是否存在
            os.makedirs(image_path)  # 若图片文件夹不存在就创建

        pix.writePNG(image_path + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内

    end_time_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (end_time_pdf2img - start_time_pdf2img).seconds)


if __name__ == "__main__":
    # 1、PDF地址
    local_pdf_path = 'science.pdf'
    # 2、需要储存图片的目录
    local_image_path = '/python/imgs'
    py_mu_pdf_fitz(local_pdf_path, local_image_path)
