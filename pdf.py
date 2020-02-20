import datetime
import os
import fitz  # fitz����pip install PyMuPDF


def py_mu_pdf_fitz(pdf_path, image_path):
    start_time_pdf2img = datetime.datetime.now()  # ��ʼʱ��

    print("image_path=" + image_path)
    pdf_doc = fitz.open(pdf_path)
    for pg in range(pdf_doc.pageCount):
        page = pdf_doc[pg]
        rotate = int(0)
        # ÿ���ߴ������ϵ��Ϊ1.3���⽫Ϊ�������ɷֱ������2.6��ͼ��
        # �˴����ǲ������ã�Ĭ��ͼƬ��СΪ��792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(image_path):  # �жϴ��ͼƬ���ļ����Ƿ����
            os.makedirs(image_path)  # ��ͼƬ�ļ��в����ھʹ���

        pix.writePNG(image_path + '/' + 'images_%s.png' % pg)  # ��ͼƬд��ָ�����ļ�����

    end_time_pdf2img = datetime.datetime.now()  # ����ʱ��
    print('pdf2imgʱ��=', (end_time_pdf2img - start_time_pdf2img).seconds)


if __name__ == "__main__":
    # 1��PDF��ַ
    local_pdf_path = 'science.pdf'
    # 2����Ҫ����ͼƬ��Ŀ¼
    local_image_path = '/python/imgs'
    py_mu_pdf_fitz(local_pdf_path, local_image_path)
