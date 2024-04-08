import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

def merge_pdfs(input_files, output_file):
    merger = PyPDF2.PdfMerger()

    for file in input_files:
        try:
            merger.append(file)
        except PyPDF2.utils.PdfReadError as e:
            print(f"Error reading {file}: {e}")

    output_dir = "./combined"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, output_file)
    with open(output_path, 'wb') as output:
        merger.write(output)

def select_files():
    root = tk.Tk()
    root.withdraw()  

    input_files = filedialog.askopenfilenames(title="Select PDF files to merge", filetypes=[("PDF files", "*.pdf")])

    if not input_files:
        print("No files selected. Exiting...")
        return None, None

    initial_dir = "./combined"
    if not os.path.exists(initial_dir):
        initial_dir = "./"
    
    output_file = filedialog.asksaveasfilename(title="Save merged PDF as", initialdir=initial_dir, initialfile="combined.pdf", filetypes=[("PDF files", "*.pdf")])

    return input_files, output_file

def main():
    input_files, output_file = select_files()
    if not input_files or not output_file:
        return

    merge_pdfs(input_files, output_file)
    print("PDF files merged successfully!")

if __name__ == "__main__":
    main()
