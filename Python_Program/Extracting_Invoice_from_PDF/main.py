import os
import PyPDF2
import re
import fitz
import pandas as pd


# Function to extract invoice number from a PDF page
def extract_invoice_number_from_page(text):
  # Use regular expression to find the invoice number (Assuming a pattern like 'INVOICE # 123456')
  match = re.search(r'INVOICE\n\s*#\s*\d+', text)
  if match:
    return match.group()
  return None


# Function to extract invoice numbers from a PDF file
def extract_invoice_numbers(pdf_path):
  invoice_numbers = []
  # Open the PDF file
  with fitz.open(pdf_path) as pdf_document:
    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
      page = pdf_document.load_page(page_num)
      text = page.get_text()
      invoice_number = extract_invoice_number_from_page(text)
      if invoice_number:
        invoice_number = (invoice_number.split("#")[1]).lstrip()
        print(invoice_number)
        invoice_numbers.append(invoice_number)
  return invoice_numbers


def open_pdf():
  # Directory containing the PDF files
  pdf_dir = 'Inputfiles'

  # List to hold all extracted invoice numbers
  all_invoices = []

  # Iterate through each PDF file in the directory
  for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
      pdf_path = os.path.join(pdf_dir, filename)
      invoices = extract_invoice_numbers(pdf_path)
      all_invoices.append(invoices)
  print(all_invoices)


if __name__ == "__main__":
  open_pdf()
