import mammoth

def convert_docx_to_html(input_file, output_file):
    try:
        with open(input_file, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_content = result.value

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print(f"Conversion successful! HTML file saved as '{output_file}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = 'c:\\Users\\A1\\Desktop\\SLA 2.docx'
  # Replace with your input file name
    output_file = 'output.html'   # Replace with your desired output file name
    convert_docx_to_html(input_file, output_file)
