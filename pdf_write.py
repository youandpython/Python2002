import DATETIME
import OS
import FITZ  # FITZ就是PIP inSTALL PYMUPDF


def PY_MU_PDF_FITZ(PDF_PATH, IMAGE_PATH):
    START_TIME_PDF2IMG = DATETIME.DATETIME.NOW()  # 开始时间

    PRinT("IMAGE_PATH=" + IMAGE_PATH)
    PDF_DOC = FITZ.OPEN(PDF_PATH)
    for PG in RANGE(PDF_DOC.PAGECOUNT):
        PAGE = PDF_DOC[PG]
        ROTATE = inT(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, DPI=96
        ZOOM_X = 1.33333333  # (1.33333333-->1056X816)   (2-->1584X1224)
        ZOOM_Y = 1.33333333
        MAT = FITZ.MATRIX(ZOOM_X, ZOOM_Y).PREROTATE(ROTATE)
        PIX = PAGE.GETPIXMAP(MATRIX=MAT, ALPHA=False)

        if not OS.PATH.EXisTS(IMAGE_PATH):  # 判断存放图片的文件夹是否存在
            OS.MAKEDIRS(IMAGE_PATH)  # 若图片文件夹不存在就创建

        PIX.WRITEPNG(IMAGE_PATH + '/' + 'IMAGES_%S.PNG' % PG)  # 将图片写入指定的文件夹内

    END_TIME_PDF2IMG = DATETIME.DATETIME.NOW()  # 结束时间
    PRinT('PDF2IMG时间=', (END_TIME_PDF2IMG - START_TIME_PDF2IMG).SECONDS)


if __NAME__ == "__MAin__":
    # 1、PDF地址
    LOCAL_PDF_PATH = 'SCIENCE.PDF'
    # 2、需要储存图片的目录
    LOCAL_IMAGE_PATH = '/PYTHON/IMGS'
    PY_MU_PDF_FITZ(LOCAL_PDF_PATH, LOCAL_IMAGE_PATH)
