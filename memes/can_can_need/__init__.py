from pathlib import Path
from typing import List

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def can_can_need(images: List[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.jpg")
    frame.paste(
        images[0].convert("RGBA").circle().resize((340, 340)), (120, 21), alpha=True
    ).paste(
        images[1].convert("RGBA").circle().resize((300, 300)), (611, 718), alpha=True
    )
    return frame.save_jpg()


add_meme("can_can_need", can_can_need, min_images=2, max_images=2, keywords=["看看你的"])
