import os
import csv
from backend.shapes import parse_geometry

def read_order(path):
    stickers = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = row["sticker_id"].strip()
            shape = row["shape"].strip()
            geom = row["geometry"]
            qty = int(row["quantity"])
            d = parse_geometry(shape, geom)
            d["sticker_id"] = sid
            d["quantity"] = qty
            stickers.append(d)
    order_id = os.path.splitext(os.path.basename(path))[0]
    return {"order_id": order_id, "stickers": stickers}
