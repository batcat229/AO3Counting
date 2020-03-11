from get_request import simple_get
from bs4 import BeautifulSoup
#
def get_counts(url):
    raw_html=simple_get(url)
    html=BeautifulSoup(raw_html, 'html.parser')
    result=html.find_all('h3', attrs={"class":"heading"})
    return result
        

def find_between(r,first,last):
    try:
        start=r.index(first)+len(first)
        end = r.index(last,start)
        true_r=r[start:end]
        return true_r
    except ValueError:
        return

def counts(language,date,rate):
    url='https://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D=&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D='+date+'&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D='+language+'&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D='+rate+'&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc&commit=Search'
    try:
        n=get_counts(url)
        t=str(n[1])
        r=find_between(t,">","F")
        return r
    except:
        print("No Result")
        return

#test#
date='%3E+7+days'
no_rated='9'
rate=no_rated
zh='zh'
en=''
zh7=counts(zh,date,no_rated)
en7=counts(en,date,no_rated)
print(zh7)
print(en7)