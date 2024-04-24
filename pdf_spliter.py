import PyPDF2

def split_pdf(input_pdf_path, output_folder):
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for page_number in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])
            
            output_pdf_path = f"{output_folder}/page_{page_number + 1}.pdf"
            
            with open(output_pdf_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            
            print(f"Page {page_number + 1} saved as {output_pdf_path}")

if __name__ == "__main__":
    input_pdf_path = "C:/temp/case.pdf"
    output_folder = "C:/temp"
    
    split_pdf(input_pdf_path, output_folder)
