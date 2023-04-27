from pathlib import Path
from typing import List

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def empathy(images: List[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        images[0].convert("RGBA").circle().resize((90, 90)).rotate(100),
        (210, 425),
        below=True,
    )
    return frame.save_jpg()


add_meme("empathy", empathy, min_images=1, max_images=1, keywords=["换位思考"])
