import DATETIME
import OS
import FITZ  # FITZ����PIP inSTALL PYMUPDF


def PY_MU_PDF_FITZ(PDF_PATH, IMAGE_PATH):
    START_TIME_PDF2IMG = DATETIME.DATETIME.NOW()  # ��ʼʱ��

    PRinT("IMAGE_PATH=" + IMAGE_PATH)
    PDF_DOC = FITZ.OPEN(PDF_PATH)
    for PG in RANGE(PDF_DOC.PAGECOUNT):
        PAGE = PDF_DOC[PG]
        ROTATE = inT(0)
        # ÿ���ߴ������ϵ��Ϊ1.3���⽫Ϊ�������ɷֱ������2.6��ͼ��
        # �˴����ǲ������ã�Ĭ��ͼƬ��СΪ��792X612, DPI=96
        ZOOM_X = 1.33333333  # (1.33333333-->1056X816)   (2-->1584X1224)
        ZOOM_Y = 1.33333333
        MAT = FITZ.MATRIX(ZOOM_X, ZOOM_Y).PREROTATE(ROTATE)
        PIX = PAGE.GETPIXMAP(MATRIX=MAT, ALPHA=False)

        if not OS.PATH.EXisTS(IMAGE_PATH):  # �жϴ��ͼƬ���ļ����Ƿ����
            OS.MAKEDIRS(IMAGE_PATH)  # ��ͼƬ�ļ��в����ھʹ���

        PIX.WRITEPNG(IMAGE_PATH + '/' + 'IMAGES_%S.PNG' % PG)  # ��ͼƬд��ָ�����ļ�����

    END_TIME_PDF2IMG = DATETIME.DATETIME.NOW()  # ����ʱ��
    PRinT('PDF2IMGʱ��=', (END_TIME_PDF2IMG - START_TIME_PDF2IMG).SECONDS)


if __NAME__ == "__MAin__":
    # 1��PDF��ַ
    LOCAL_PDF_PATH = 'SCIENCE.PDF'
    # 2����Ҫ����ͼƬ��Ŀ¼
    LOCAL_IMAGE_PATH = '/PYTHON/IMGS'
    PY_MU_PDF_FITZ(LOCAL_PDF_PATH, LOCAL_IMAGE_PATH)
