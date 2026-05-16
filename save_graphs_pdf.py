from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

images = [
    "runtime_comparison.png",
    "memory_comparison.png",
    "conflicts_comparison.png"
]

with PdfPages("graphs.pdf") as pdf:
    for img_path in images:
        img = mpimg.imread(img_path)
        plt.figure(figsize=(10, 7))
        plt.imshow(img)
        plt.axis("off")
        pdf.savefig(bbox_inches="tight")
        plt.close()

print("graphs.pdf created successfully")