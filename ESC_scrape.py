from bs4 import BeautifulSoup as bs

def get_urls(html_file, verbose=False):
    
    with open('html/{}'.format(html_file), 'r') as f:
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
        for i in range(min(50, len(urls))):
            print(i, urls[i])

    return urls

def get_chpts(html_file, verbose=False):
    with open('html/{}'.format(html_file), 'r') as f:
        soup = bs(f, 'html.parser')
        chpts = []
        for li in soup.find_all('li', class_=['notcurrent', 'chapterType', 'level3']):
        
            try:
                if not 'expand' in li.a.text:
                    chpts.append(' '.join(li.a.text.split()))
                # print(li.a['href'][-3:])
            except:
                continue
    if verbose:
        for i in range(min(50, len(chpts))):
            print(i, chpts[i])
    return chpts

def get_fns(html_file, folder):
    
    with open('html/{}'.format(html_file), 'r') as f:
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

    chpts = get_chpts(html_file)
    fns = get_fns(html_file, folder)
    
    for i in range(len(fns)):
        
        new_fn = os.path.join(os.path.dirname(fns[i]), chpts[i] + '.pdf')
        new_fn = new_fn.replace("/", ", ").replace(":", " - ")
        
        try:
            os.rename(fns[i], new_fn)

            if verbose:
                print('RENAMING', os.path.basename(fns[i]), 'TO', chpts[i])

        except Exception as e:
            print(e)

    
        


if __name__ == '__main__':
    # html_file = input('HTML Filename:\n')
    # folder = input('DOWNLOAD FOLDER NAME:\n')
    
    import os
    html_fns = [fn for fn in os.listdir("html") if fn.endswith(".html")]
    folder_names = [fn.replace(".html", "") for fn in os.listdir("html") if fn.endswith(".html")]

    for item in zip(html_fns, folder_names):

        chpts = get_chpts(item[0], verbose=True)
        # urls = get_urls(item[0], verbose=True)
        # print(urls)
        print(get_fns(item[0], item[1]))
        rename_files(item[0], item[1], verbose=True)

    
