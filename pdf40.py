from PyPDF2 import PdfReader, PdfWriter

# Load the uploaded PDF file
file_path = '73-两次杠杆做到5000万股灾被强平的投机之路-南侠1987.pdf'
reader = PdfReader(file_path)

# Calculate how many pages should be in each of the 40 files
total_pages = len(reader.pages)
pages_per_file = total_pages // 40

# Split the PDF into 40 separate files
output_files = []
for i in range(40):
    writer = PdfWriter()
    start_page = i * pages_per_file
    end_page = (i + 1) * pages_per_file if i < 39 else total_pages  # Make sure last file gets the remaining pages
    
    # Add pages to each new PDF
    for page_num in range(start_page, end_page):
        writer.add_page(reader.pages[page_num])
    
    output_file_path = f'part_{i+1}_of_40.pdf'
    with open(output_file_path, 'wb') as output_file:
        writer.write(output_file)
    
    output_files.append(output_file_path)

output_files

