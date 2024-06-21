from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from img2pdf import convert as img2pdf_convert
class pdf_swissknife:

    @staticmethod
    def pdf_merge(input_files, output_file):
        pdf_merger = PdfMerger()
        for input_file in input_files:
            pdf_merger.append(input_file)
        with open(output_file, 'wb') as output_pdf:
            pdf_merger.write(output_pdf)
    
    @staticmethod
    def pdf_split(input_pdf_path, output_folder):
        with open(input_pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            
            for page_number in range(len(pdf_reader.pages)):
                pdf_writer = PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[page_number])
                
                output_pdf_path = f"{output_folder}/page_{page_number + 1}.pdf"
                
                with open(output_pdf_path, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
                
                print(f"Page {page_number + 1} saved as {output_pdf_path}")
   
if __name__ == "__main__":
    input_pdf_path = "C:/temp/case.pdf"
    output_folder = "C:/temp"
    
    pdf_swissknife.pdf_split(input_pdf_path, output_folder)
