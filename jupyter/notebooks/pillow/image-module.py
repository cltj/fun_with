from PIL import Image
with Image.open(r"/mnt/c/dev/fun_with/jupyter/notebooks/pillow/cl.png") as im:
    im.rotate(45).show()

