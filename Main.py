import os
from st_io.order_reader import read_order
from st_io.layout_writer import write_layout
from backend.packing import pack
from visualization.draw import visualize

ORDERS_DIR = r"\\path\\to\\orders"

def main():
    files = [f for f in os.listdir(ORDERS_DIR) if f.endswith(".csv") and not f.endswith("_layout.csv")]
    for fn in files:
        full = os.path.join(ORDERS_DIR, fn)
        order = read_order(full)
        sheets, oversized = pack(order)
        visualize(order, fn, sheets, oversized)
        out = full.replace(".csv", "_layout.csv")
        write_layout(order, sheets, oversized, out)
        total = sum(s["size"][0]*s["size"][1] - sum(p["area"] for p in s["placed"]) for s in sheets)
        print("Total waste:", int(total))
        if oversized:
            print("Too large:", ", ".join(oversized))

if __name__ == "__main__":
    main()
