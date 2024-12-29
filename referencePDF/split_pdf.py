import PyPDF2

input_path = "/home/v-zhifeng/HPE/CombinatoricsProj/combinatorics.pdf"
output_path = "/home/v-zhifeng/HPE/CombinatoricsProj/combinatorics_first1pages.pdf"

# Open the PDF file in read-binary mode
with open(input_path, "rb") as infile:
    reader = PyPDF2.PdfReader(infile)
    writer = PyPDF2.PdfWriter()

    # Add the first 10 pages to the writer
    for page_number in range(1):  # pages are 0-indexed
        writer.add_page(reader.pages[page_number])

    # Write out the new PDF
    with open(output_path, "wb") as outfile:
        writer.write(outfile)

print("Successfully created first 10 pages:", output_path)
