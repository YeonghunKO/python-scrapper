import requests
from bs4 import BeautifulSoup

LIMIT = 50

URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def last_page():
    result = requests.get(URL) #'URL' 이라고 해서 NO SCHEMA SUPPLIED 라고 ERROR 떴었음..;; 
    soup = BeautifulSoup(result.text, "html.parser")
    pagi = soup.find("div", {"class" : "pagination"})
    link = pagi.find_all('a')

    spans = []
    for span in link[:-1]:         
        spans.append(int(span.string))
     # 마지막 원소 빼고 다 출력

    max_page = spans[-1]
    return max_page # 이 함수를 통해서 maxpage 데이터 value 저장함. return 으로 저장안하고 그냥 print 만 하면 나중에 값을 불러올때 none 이라고 뜰것임.


# sp = link.find("span", {"class":"pn"})

# print(sp)
# 위에건 왜 안될까? 리스트라서 싱글 원소로 취급하지 말라고 하던데.(You're probably treating a list of elements like a single element.)
# 답변: link 안에 a 가 여러개 있다. find("a") 이 함수 는 결과값중에 젤 앞에 있는 것만 찾아내는 함수이다. 페이지 안에 있는 모든 링크태그중에 제일 위에있는것만. 
# find_all("a")은 페이지 안에 있는 모든 링크를 찾아내는거고. 그래서 find_all로 찾아낸건 find_all로 끝내거나 for 문을 통해 하나하나 훑어야한다.



#page url 을 보면 1페이지일때(1페이지에 50개의 결과물이 출력된다고 봤을때) url 끝에 start=0, 2페이지일때 start=50 이런식으로 나감.
#나중에 url 을 추출할때 끝에 이런식으로 덧붙여서 각페이지의 url을 추출할 생각이다.


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"] 
    # chaining 이라고 한다. title=~~ + anchor = title.find("a")["title"]를 한 문장으로 묶었다.
    # 따라서 말로 풀면은 "h2(class:title) 태그 안에 a<title=~~> 태그가 있는데 ~~를 뽑아내라"는 뜻이다.
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is None:
        company = str(company.string)
    else:
        company = str(company_anchor.string)
    company = company.strip()    
    # 이번에는 회사 이름을 scrap 해볼거다. 검사를 통해 알아봤는데 <span class=company> 라고 되어있고 
    # child 로 링크안에 회사이름이 기재되어있는것도 있고 span 태그안에 바로 기재되어있는 것도 있어서 if/else 문법을 써주었다.
    # 그리고 span태그 a 태그를 나누어서 변수에 담고 사용하였다. 그리고 str 함수로 글자변환한다음에 space 를 없애주려고 strip() 함수도 사용해주었다.
    # 이로써 깔끔하게 company 까지 출력이 된다.
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    link = f"https://www.indeed.com/viewjob?jk={job_id}"    
    return {'Title': title , 
            'Company': company , 
            'location': location, 
            'link':link
            }
    # 중요한건 장소, 링크를 뽑아낼때, 검사를 통해 해당 장소코드가 어디에 위치하는지, 그리고 링크의 url 은 어떻게 생성되는지 알아내야한다.
    # 장소는 location 에서 div class=recjobloc 안에 attribute 로 data-rc-loc에 명시되어있었고 링크는 클릭해서 url을 보고 구성하였다.
    # 그리고 함수를 따로 만든다음 대입해서 코드를 작성하는게 깔끔하다. extract_job(result) 처럼.



def extractor_indeed_jobs(last_page):
    jobs = []    
    for page in range(last_page)[:10]:
        print(f"scrapping INDEED Page: {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}") 
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)        
    return jobs

# 다시 한 번더 requests, Beautifulsoup 함수를 써준다. 그리고 for 문을 통해 scrap 해온 모든 문장을 훑으면서 원하는 것을 찾아낸다.
# return jobs 를 for 문안에 쓰는 경우: page 0 에서 끝남. 왜냐? return은 함수를 끝내기도 하니깐.
# return jobs 를 안쓰는 경우: jobs = [] 안에 저장만 되고 출력은 안됨.

def get_jobs():
    max_indeed_pages = last_page()
    indeed_jobs = extractor_indeed_jobs(max_indeed_pages)
    return indeed_jobs
# return 하는 거 잊지말자!

