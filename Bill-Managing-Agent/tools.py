
import pytesseract
from PIL import Image

def extract_text_from_image(image_bytes: bytes) -> str:
    """Extract plain text from image using OCR."""
    try:
        img = Image.open(image_bytes)
        return pytesseract.image_to_string(img)
    except Exception:
        return ""

def parse_and_categorize(text: str) -> dict:
    """
    Simulate categorizing expenses.
    Returns a dict {"category": amount, ...}
    """
    categories = {}
    total = 0.0
    for line in text.splitlines():
        parts = line.rsplit(" ", 1)
        if len(parts) != 2: continue
        item, value = parts
        try:
            price = float(value.replace("$", ""))
        except Exception:
            continue
        category = "uncategorized"
        if any(x in item.lower() for x in ["grocery","supermarket"]):
            category = "Groceries"
        elif any(x in item.lower() for x in ["cafe","coffee","restaurant"]):
            category = "Dining"
        categories[category] = categories.get(category, 0.0) + price
        total += price
    categories["__total__"] = total
    return categories
