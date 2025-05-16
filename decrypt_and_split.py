# decrypt_and_split.py
# This module provides two utilities:
# 1. decrypt_pdf: Decrypts an encrypted PDF using a known password.
# 2. split_pdf_by_pages: Splits a PDF into smaller chapters by specifying page ranges.

import pikepdf 
from PyPDF2 import PdfReader, PdfWriter 


def decrypt_pdf(input_path: str, output_path: str, password: str) -> None:
    """
    Decrypts a PDF file that is encrypted with a password and writes the decrypted version to disk.

    Parameters:
    - input_path: Path to the encrypted PDF.
    - output_path: Path where the decrypted PDF will be saved.
    - password: Password used to open the encrypted PDF.

    Example:
    decrypt_pdf(
        "/path/to/encrypted.pdf",
        "/path/to/decrypted.pdf",
        "yourPassword"
    )
    """
    # Open the encrypted PDF using the provided password
    with pikepdf.open(input_path, password=password) as pdf:
        # Save the decrypted copy to the specified output path
        pdf.save(output_path)
    print(f"Decryption complete. Saved decrypted PDF to: {output_path}")


def split_pdf_by_pages(input_pdf: str, output_prefix: str, start_page: int, end_page: int) -> None:
    """
    Splits a PDF into a new file containing only the pages from start_page to end_page (inclusive).

    Parameters:
    - input_pdf: Path to the source PDF (typically decrypted first).
    - output_prefix: Prefix for the output filename; the function appends "_start_to_end.pdf".
    - start_page: First page number to include (1-based index).
    - end_page: Last page number to include (1-based index).

    Example:
    split_pdf_by_pages(
        "decrypted.pdf",
        "chapter1",
        1,
        12
    )  # creates chapter1_1_to_12.pdf
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Loop over pages (convert 1-based to 0-based indices)
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])

    # Build the output filename
    output_pdf = f"{output_prefix}_{start_page}_to_{end_page}.pdf"
    # Write the new PDF containing only the specified range
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"Created split PDF: {output_pdf}")


if __name__ == "__main__":
    # Example usage:
    encrypted_path = "path of encrypted document" # Replace with actual paths
    decrypted_path = "path of decrypted document" # Replace with actual paths
    pdf_password = "password" # Replace with the actual password

    # Step 1: Decrypt the PDF
    decrypt_pdf(encrypted_path, decrypted_path, pdf_password)

    # Step 2: Split decrypted PDF into chapters by page ranges
    # Adjust the page ranges according to your needs
    split_pdf_by_pages(decrypted_path, "chapter1", 1, 12)
    split_pdf_by_pages(decrypted_path, "chapter2", 13, 32)
    split_pdf_by_pages(decrypted_path, "chapter3", 33, 52)
    split_pdf_by_pages(decrypted_path, "chapter4", 53, 58)
    split_pdf_by_pages(decrypted_path, "chapter5", 59, 76)
    split_pdf_by_pages(decrypted_path, "chapter6", 77, 81)
    split_pdf_by_pages(decrypted_path, "chapter7", 82, 95)
    split_pdf_by_pages(decrypted_path, "chapter8", 96, 112)
