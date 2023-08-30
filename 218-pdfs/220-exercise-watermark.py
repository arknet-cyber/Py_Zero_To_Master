from pypdf import PdfWriter, PdfReader
import sys

stamp = PdfReader('dummy.pdf').pages[0]
write = PdfWriter(clone_from='wtr.pdf')
for page in write.pages:
    page.merge_page(stamp, over=False)

write.write('out.pdf')


# The course solution

import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileMerger

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)