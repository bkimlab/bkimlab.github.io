"""Generate web-sized copies of the photos in ../photos/ into assets/images/.

    photos/lab_theme/*      -> assets/images/hero/    (home banner, max 1600 px wide)
    photos/group_photos/*   -> assets/images/group/   (members banner, max 1600 px wide)
    photos/<person>/*       -> assets/images/people/<person>/  (max 600 px tall)

Output is progressive JPEG with EXIF stripped (phone photos often embed GPS)
and orientation applied. Filenames are lower-cased and de-punctuated:
'DSC01303~2.jpg' -> 'dsc01303-2.jpg'. Run again after adding photos; existing
outputs are overwritten. Requires Pillow.
"""
import os
import re
import sys

from PIL import Image, ImageOps

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(os.path.dirname(SITE), 'photos')
OUT = os.path.join(SITE, 'assets', 'images')
BANNER_SETS = {'lab_theme': 'hero', 'group_photos': 'group'}
BANNER_WIDTH = 1600
PORTRAIT_HEIGHT = 600
QUALITY = 82


def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', os.path.splitext(name)[0].lower()).strip('-') + '.jpg'


def convert(src, dst, max_w=None, max_h=None):
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    im.thumbnail((max_w or im.width, max_h or im.height), Image.LANCZOS)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, 'JPEG', quality=QUALITY, optimize=True, progressive=True)  # no exif kwarg: metadata dropped
    return im.size, os.path.getsize(dst) // 1024


def main():
    if not os.path.isdir(SRC):
        sys.exit(f'no photos directory at {SRC}')
    for folder in sorted(os.listdir(SRC)):
        src_dir = os.path.join(SRC, folder)
        if not os.path.isdir(src_dir):
            continue
        for f in sorted(os.listdir(src_dir)):
            if not f.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
            if folder in BANNER_SETS:
                dst = os.path.join(OUT, BANNER_SETS[folder], slug(f))
                size, kb = convert(os.path.join(src_dir, f), dst, max_w=BANNER_WIDTH)
            else:
                dst = os.path.join(OUT, 'people', folder, slug(f))
                size, kb = convert(os.path.join(src_dir, f), dst, max_h=PORTRAIT_HEIGHT)
            print(f'{os.path.relpath(dst, SITE)}  {size[0]}x{size[1]}  {kb} KB')


if __name__ == '__main__':
    main()
