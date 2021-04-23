from ESC_scrape import get_chpts, get_fns
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
        

if __name__ == '__main__':
    import ESC_scrape
    fns = get_fns()
    chpts = get_chpts()
    merger = PdfFileMerger()
    # split into chunks and append to completed file if # of pdf files > 150
    for i in range(1,9):
        
        # pdf_name = "/Users/brandonthio/Python/Get_Oxford_Textbook/Oxford_Medical_Approach_to_Medical Decision_Making/med-9780190862800-chapter-{}.pdf".format(i)
        
        try:
            fn = "C:/Users/Admin/med_txtbk_scrape/merged{}.pdf".format(i)
    
            f = open(fn, 'rb')
            merger.append(f)
            print("MERGING {}".format(fn))

        except Exception as e:

            print(e, fn)

    print("SAVING MERGED PDF")
    
    save_fn = "C:/Users/Admin/med_txtbk_scrape/merged.pdf" 
    with open(save_fn, 'wb+') as save:
        merger.write(save)
        merger.close()

    print("SUCCESS")
