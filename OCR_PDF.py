import tkinter as tk
from tkinter import filedialog
import os
import ocrmypdf

root = tk.Tk()
root.withdraw()

# Select input PDF
input_pdf = filedialog.askopenfilename(
    title="Select PDF File",
    filetypes=[("PDF Files", "*.pdf")]
)

if not input_pdf:
    print("No PDF selected.")
    quit()

# Fixed output folder
output_folder = r"E:\Documents"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get original filename
pdf_name = os.path.splitext(
    os.path.basename(input_pdf)
)[0]

# Output file path
output_pdf = os.path.join(
    output_folder,
    f"{pdf_name}_searchable.pdf"
)

print(f"\nInput : {input_pdf}")
print(f"Output: {output_pdf}")

ocrmypdf.ocr(
    input_pdf,
    output_pdf,
    force_ocr=True
)

print(f"\nSearchable PDF created:")
print(output_pdf)

# Open output folder automatically
os.startfile(output_folder)

input("\nPress Enter to exit...")
