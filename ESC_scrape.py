from bs4 import BeautifulSoup as bs

def get_urls(html_file, verbose=False):
    
    with open(html_file + '.html', 'r') as f:
        soup = bs(f, 'html.parser')
        urls = []
        for li in soup.find_all('li', class_=['notcurrent', 'chapterType', 'level3']):
        
            try:
                url = "https://oxfordmedicine-com.libproxy1.nus.edu.sg{}?print=pdf".format(li.a['href'])
                urls.append(url)
                print(url)
            except:
                continue
    if verbose:
        for i in range(50):
            print(i, urls[i])

    return urls

def get_chpts(html_file):
    with open(html_file + '.html', 'r') as f:
        soup = bs(f, 'html.parser')
        chpts = []
        for li in soup.find_all('li', class_=['notcurrent', 'chapterType', 'level3']):
        
            try:
                if not 'expand' in li.a.text:
                    chpts.append(' '.join(li.a.text.split()))
                # print(li.a['href'][-3:])
            except:
                continue
    return chpts

def get_fns(html_file, folder):
    
    with open(html_file + '.html', 'r') as f:
        soup = bs(f, 'html.parser')
        fns = []
        for li in soup.find_all('li', class_=['notcurrent', 'chapterType', 'level3']):
        
            try:
                fn = li.a['href']
                
                fn = fn[fn.find('/view/10.1093/')+14:]
                fn = fn[:fn.find('.001.0001')] + fn[fn.find('.001.0001')+9:]
                fn = fn[18:]
                fn = '/Users/brandonthio/Downloads/{}/'.format(folder) + fn +'.pdf'
                
                fns.append(fn)

            except:
                continue
    return fns

   

def rename_files(html_file, folder, verbose=False):
    import os

    chpts = get_chpts(html_file)
    fns = get_fns(html_file, folder)
    
    for i in range(len(fns)):
        
        new_fn = os.path.join(os.path.dirname(fns[i]), chpts[i] + '.pdf')

        try:
            os.rename(fns[i], new_fn)

            if verbose:
                print('RENAMING', os.path.basename(fns[i]), 'TO', chpts[i])

        except Exception as e:
            print(e)

    
        


if __name__ == '__main__':
    html_file = input('HTML Filename:\n')
    folder = input('DOWNLOAD FOLDER NAME:\n')
    rename_files(html_file, folder, verbose=True)

    
