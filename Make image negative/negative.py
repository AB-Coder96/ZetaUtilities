from PIL import Image, ImageOps
img_path = "/mnt/data/photo_5994795990780676870_y.jpg"
img = Image.open(img_path).convert("RGB")
neg = ImageOps.invert(img)
out_path = "/mnt/data/lateral_flow_assay_negative.png"
neg.save(out_path)
out_path