"""Lay out supplied, uncropped illustrations on textures for ThreeUI's original curl.

Run after changing story.json: python3 scripts/prepare_spreads.py
Requires Pillow and fonttools[woff]. No illustrations are generated or retouched.
"""
from pathlib import Path
import json
import math
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'public/landing-pages/meng-to-sketchbook'
MEDIA = ROOT / 'public/landing-pages/shelby-media'
OUT = MEDIA / 'spreads'
OUT.mkdir(exist_ok=True)
FONT_CACHE = ROOT / '.sites-runtime/story-fonts'
FONT_CACHE.mkdir(parents=True, exist_ok=True)

def font(name, size):
    path = FONT_CACHE / (name + '.ttf')
    if not path.exists():
        tt = TTFont(ASSETS / (name + '.woff2'))
        tt.flavor = None
        tt.save(path)
    return ImageFont.truetype(str(path), size)

def wrap(draw, text, face, width):
    lines = []
    for paragraph in text.split('\n'):
        current = ''
        for word in paragraph.split():
            candidate = current + (' ' if current else '') + word
            if current and draw.textlength(candidate, font=face) > width:
                lines.append(current)
                current = word
            else:
                current = candidate
        lines.append(current)
    return lines

pages = json.loads((ROOT / 'story.json').read_text())
for i, page in enumerate(pages):
    # Exactly the canonical 1760 × 1240 spread coordinate system and .449 span.
    spread = Image.new('RGBA', (1760, 1240))
    draw = ImageDraw.Draw(spread)
    for offset, tone in [(10, '#cdc3b0'), (7, '#e0d6c5'), (4, '#eee4d3')]:
        draw.rounded_rectangle((90-offset//2, 276+offset, 1670+offset//2, 968+offset), radius=22, fill=tone)
    draw.rounded_rectangle((90, 272, 1670, 968), radius=20, fill='#f8f2e7')
    # Use the author's existing painted wash as a very faint paper surface.
    texture = Image.open(ASSETS / 'bg-wash.jpg').convert('RGBA').resize((1580, 696))
    texture.putalpha(15)
    mask = Image.new('L', (1580, 696))
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 1579, 695), radius=20, fill=15)
    texture.putalpha(mask)
    spread.alpha_composite(texture, (90, 272))
    draw = ImageDraw.Draw(spread)
    ink = '#39302a'
    muted = '#806957'
    draw.text((174, 314), 'CHAPTER ONE  ·  WINDWORKS', font=font('newsreader', 25), fill=muted)
    y = 365
    for line in page['heading']:
        draw.text((174, y), line, font=font('instrument-serif', 72), fill=ink)
        y += 79
    y += 28
    face = font('newsreader', 39)
    lines = [wrap(draw, paragraph, face, 625) for paragraph in page['paragraphs']]
    block_height = sum(len(group)*48 for group in lines) + (len(lines)-1)*20
    if y + block_height > 882:
        face = font('newsreader', 36)
        lines = [wrap(draw, paragraph, face, 625) for paragraph in page['paragraphs']]
    for group in lines:
        for line in group:
            draw.text((174, y), line, font=face, fill=ink)
            y += 48
        y += 20
    if y > 930:
        raise ValueError('Text needs a shorter excerpt: '+page['id'])
    picture = Image.open(MEDIA / page['image']).convert('RGBA')
    # Contain the entire supplied frame, including its caption and taped border.
    ratio = min(684 / picture.width, 532 / picture.height)
    w, h = round(picture.width*ratio), round(picture.height*ratio)
    x, py = 927 + (684-w)//2, 338 + (532-h)//2
    picture = picture.resize((w, h), Image.Resampling.LANCZOS)
    spread.alpha_composite(picture, (x, py))
    page['mediaRect'] = [x/1760, py/1240, w/1760, h/1240]
    # The gutter belongs to the page surface, so it moves with the original leaf.
    gutter = Image.new('RGBA', spread.size)
    gd = ImageDraw.Draw(gutter)
    for gx in range(842, 907):
        alpha = round(43*math.exp(-abs(gx-880)/14))
        gd.line((gx, 276, gx, 965), fill=(70, 49, 26, alpha))
    gd.line((882, 277, 882, 965), fill=(255, 253, 245, 100), width=2)
    spread.alpha_composite(gutter)
    draw = ImageDraw.Draw(spread)
    draw.text((174, 916), 'SHELBY & THE CUDDLE WARRIORS', font=font('newsreader', 20), fill=muted)
    draw.text((1587, 916), str(i+1).zfill(2), font=font('newsreader', 24), fill=muted)
    spread.save(OUT / (page['id']+'.webp'), 'WEBP', quality=96, method=6)
    page['url'] = 'shelby-media/spreads/'+page['id']+'.webp'
    page['poster'] = 'shelby-media/'+page['image']
    print(page['id'], 'body bottom', y, 'picture', (x, py, w, h))

(ROOT/'public/landing-pages/story-data.js').write_text(
    '// Generated from story.json by scripts/prepare_spreads.py\n'
    'window.SHELBY_STORY = '+json.dumps(pages, ensure_ascii=False, indent=2)+';\n'
)
