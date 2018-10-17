try:
    from PIL import Image
    import pytesseract
except ImportError:
    raise SystemExit


def recImg(img):
    w = pytesseract.image_to_string(img, lang='chi_sim')
    return w
