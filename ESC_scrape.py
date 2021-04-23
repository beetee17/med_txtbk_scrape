from bs4 import BeautifulSoup as bs

def get_urls():
    
    with open('ESC.html', 'r') as f:
        soup = bs(f, 'html.parser')
        urls = []
        for li in soup.find_all('li', class_=['notcurrent', 'chapterType', 'level3']):
        
            try:
                urls.append("https://oxfordmedicine-com.libproxy1.nus.edu.sg{}?print=pdf".format(li.a['href']))
                # print(li.a['href'][-3:])
            except:
                continue
    return urls
def get_chpts():
    with open('ESC.html', 'r') as f:
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
def get_fns():
    
    with open('ESC.html', 'r') as f:
        soup = bs(f, 'html.parser')
        fns = []
        for li in soup.find_all('li', class_=['notcurrent', 'chapterType', 'level3']):
        
            try:
                fn = li.a['href']
                fn = fn[fn.find('/view/10.1093/')+14:]
                fn = fn[:fn.find('.001.0001')] + fn[fn.find('.001.0001')+9:]
                fn = fn.replace('/9780198784906/', '--')
                # fn = fn.replace('/', '-')
                fn = fn.replace('med--', '')
                fn = '/Users/brandonthio/Downloads/' + fn +'.pdf'
                
                fns.append(fn)

                # print(li.a['href'][-3:])
            except:
                continue
    return fns

    # https://oxfordmedicine-com.libproxy1.nus.edu.sg/view/10.1093/med/9780198784906.001.0001/med-9780198784906-chapter-1?print=pdf
if __name__ == '__main__':
    fns = get_fns()
    chpts = get_chpts()
    print(len(chpts))
    for i in range(50):
        if i% 50==0:
            print(i)
        print(chpts[i])