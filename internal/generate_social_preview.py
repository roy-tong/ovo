from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "social-preview.png"
CN = "/System/Library/Fonts/STHeiti Medium.ttc"
EN = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REG = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

image = Image.new("RGB", (1200, 630), "#0D1B2A")
draw = ImageDraw.Draw(image)
teal = "#74D7C1"
white = "#F5F8FA"
muted = "#A9BBC6"
draw.rectangle((64, 58, 156, 64), fill=teal)
draw.text((64, 108), "OVO", font=ImageFont.truetype(EN, 72), fill=white)
draw.text((64, 236), "让 Agent 把真实业务做成", font=ImageFont.truetype(CN, 40), fill=white)
draw.text((64, 322), "真实研究 · 持续增长运营 · 独立经济度量", font=ImageFont.truetype(CN, 27), fill=teal)
draw.text((64, 388), "三个产品，一套 AI Native 业务交付体验", font=ImageFont.truetype(CN, 25), fill=muted)
draw.text((64, 490), "ASKOVO 2.25.1rc1   GROWOVO 0.23.1rc2   VEROVO 0.20.1rc1", font=ImageFont.truetype(REG, 21), fill=muted)
draw.text((1136, 570), "roy-tong.github.io/ovo", font=ImageFont.truetype(REG, 19), fill=muted, anchor="rs")
image.save(OUT)
print(OUT)
