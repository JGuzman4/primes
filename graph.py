import math
from PIL import Image, ImageDraw

w = 600
img = Image.new("RGB", (w, w), "lightgoldenrodyellow")
draw = ImageDraw.Draw(img)
for n in range(1, w * w // 4):
    p = 1
    for s in range(2, int(math.sqrt(n))):
        if n % s == 0:
            p = 0
    if p == 1:
        r = math.sqrt(n)
        t = 2 * math.pi * r
        x = int(w * 0.5 + r * math.cos(t))
        y = int(w * 0.5 - r * math.sin(t))
        draw.ellipse([x, y, x + 4, y + 4], fill="black")
img.save("primes.png")
img.show()
