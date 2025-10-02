# DOCX to HTML Converter

This project provides a simple Python script to convert `.docx` files to
HTML using the [Mammoth](https://github.com/mwilliamson/python-mammoth)
library.

## Features

-   Converts `.docx` files to clean and semantic HTML.
-   Easy-to-use script with minimal dependencies.
-   Handles errors gracefully.

## Requirements

-   Python 3.7+
-   [mammoth](https://pypi.org/project/mammoth/)

Install requirements with:

``` bash
pip install mammoth
```

## Usage

1.  Place your `.docx` file in the desired location.
2.  Update the `input_file` variable in `convert_docx_to_html.py` with
    your `.docx` file path.
3.  Run the script:

``` bash
python convert_docx_to_html.py
```

4.  The converted HTML will be saved as `output.html` (or the file name
    you specify).

## Example

``` python
input_file = 'c:\Users\A1\Desktop\SLA 2.docx'
output_file = 'output.html'
convert_docx_to_html(input_file, output_file)
```

## Output

-   The script will generate an HTML file that can be opened in any web
    browser.

## License

This project is licensed under the MIT License.
