from ESC_scrape import get_chpts, get_fns
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
        

if __name__ == '__main__':
    import ESC_scrape
    fns = get_fns()
    chpts = get_chpts()
    merger = PdfFileMerger()
    # split into chunks and append to completed file
    for i in range(len(fns)):
        
        # pdf_name = "/Users/brandonthio/Python/Get_Oxford_Textbook/Oxford_Medical_Approach_to_Medical Decision_Making/med-9780190862800-chapter-{}.pdf".format(i)
        
        try:
            fn = fns[i]
    
            pdf_file = open(fn, 'rb')
            merger.append(pdf_file, bookmark=chpts[i])
            print("MERGING {} {}".format(fn, chpts[i]))

        except Exception as e:

            print(e, fn)

    print("SAVING MERGED PDF")

    with open("/Users/brandonthio/Python/Get_Oxford_Textbook/completed_file3.pdf", "ab+") as save_file:
    
        merger.write(save_file)
        merger.close()

    print("SUCCESS")
