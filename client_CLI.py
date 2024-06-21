import pdf_swissknife

def get_options():
    try:
        print("Options:")
        print("1. split pdf")
        print("2. merge pdf")
        print("3. convert image to pdf")
        print("4. Exit")
        return int(input("Enter your choice: "))
    except ValueError:
        return -1

def preforme_split():
    input_pdf_path = input("Enter the path of the pdf file: ")
    output_folder = input("Enter the path of the output folder: ")
    pdf_swissknife.pdf_split(input_pdf_path, output_folder)

def preforme_merge():
    input_files = input("Enter the path of the pdf files separated by comma: ").split(",")
    output_file = input("Enter the path of the output pdf file: ")
    pdf_swissknife.pdf_merge(input_files, output_file)

def preforme_convert():
    input_image_path = input("Enter the path of the output image file: ")
    output_file = input("Enter the path of the output pdf file: ")
    if not input_image_path.endswith(".jpg") and not input_image_path.endswith(".jpeg") and not input_image_path.endswith(".png"):
        print("Invalid image file. Please try again.")
        return
    
    if not output_file.endswith(".pdf"):
        output_file += ".pdf"
    
    pdf_swissknife.convert_image_to_pdf(input_image_path, output_file)

def main():
    while True:
        choice = get_options()
        if choice == 1:
            preforme_split()
        elif choice == 2:
            preforme_merge()
        elif choice == 3:
            preforme_convert()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()