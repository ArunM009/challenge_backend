import PyPDF2
import tabula
import json

def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def extract_tables(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables

if __name__ == "__main__":
    pdf_path = input("Enter path to PDF file: ")
    
    # Extract text
    text = extract_text(pdf_path)
    
    # Extract tables
    tables = extract_tables(pdf_path)
    
    # Save results to JSON
    result = {
        'text': text,
        'tables': tables
    }
    
    with open('pdf_extraction_results.json', 'w') as f:
        json.dump(result, f, indent=4)
    
    print("Text and tables extracted and saved to pdf_extraction_results.json")