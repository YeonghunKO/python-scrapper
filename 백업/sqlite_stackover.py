import requests
import sqlite3
import json
import codecs
from bs4 import BeautifulSoup

URL ="https://stackoverflow.com/jobs?q=python&sort=i"

def so_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagi = soup.find("div", {"class":"s-pagination"}).find_all("a")           
    last = pagi[-2].get_text(strip=True) #pagi 안에 텍스트(페이지넘버)를 불러들이고 strip 해서 정리해줌.(이런식으로 strip=true를 인자로 사용가능)
    return int(last)
    # indeed 서 처럼 link에서 span을 다 뽑아서 리스트에 넣은다음 리스트 마지막 숫자만 뽑아내도 좋고
    # 여기서 처럼 아예 링크 마지막 부분을 애초부터 뽑아내도 괜찮다.

def extract_job(html):    
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company = html.find("h3", {"class":"fc-black-700"}).find("span").string.strip()
    location = html.find("span", {"class": "fc-black-500"}).string.strip()
    job_id = html["data-jobid"]
    link = f"https://stackoverflow.com/jobs?id={job_id}&q=python"
    
    return title,company,location,link
# 위의 모든 데이터를 리스트안에 넣고 for loop 을 돌리려면 return 뒤에 중괄호 없이 그냥 이름만 적을것!
           



def extract_so_jobs(last_page): 
    conn = sqlite3.connect("C:\\Bitnami\\wampstack-7.4.6-1\\apache2\\htdocs\\scrapper.sqlite") # Mention the full path to where SQLite is located.
    cur = conn.cursor()  
    cur.executescript('''
    DROP TABLE IF EXISTS scrapper;

    CREATE TABLE scrapper (title TEXT, company TEXT, location TEXT, link TEXT)
    ''') # 두줄을 적으려면 executescript 함수를 사용할 것.
    jobs = [] 
    for page in range(1):
        print(f"Scrapping SO Page:{page}")
        result = requests.get(f"{URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"} )
        for result in results:
            job = extract_job(result)
            jobs.append(job)     
       
    for data in jobs:
        title = data[0]
        company = data[1]
        location = data[2]
        link = data[3]
        cur.execute('''INSERT INTO scrapper (title, company, location, link)
            VALUES ( ?, ?, ?, ? )''', ( title, company, location, link ) )
        conn.commit()
    cur.close()
    return jobs
# 된다....된다...된다...드디어 진짜 된다ㅠㅠㅠㅠ 진짜 포기하려고 했었는데... 너무 뿌듯하고 자랑스럽고 벅차고 그렇다.. 
# 발상의 전환이 중요한 것 같다. 사실 jobs[] 안에 있는 값을 python coursera 처럼 js 파일로 따로 뽑아서 open 한 다음 for loop 돌릴려고 했는데
# js 파일안에 저장된 리스트가 다듬어지지 않아서 계속 에러 나고 심지어 파일을 찾을 수 없다는 에러까지 나서 멘붕왔다. 그래서 파일을 따로 만들지말고
# 여기 extract_so_job 함수안에서 jobs[] 안에 저장하고 for loop을 돌리자고 생각하니 그뒤로는 쉽게 술술 풀렸다. 생각의 폭을 넓히고 생각에 갇히지 말자! 
# 편하게 자유롭게!!

def get_jobs():
    last_page = so_last_page()
    so_jobs = extract_so_jobs(last_page)
    return so_jobs


# <난 사용안했지만, 니코는 사용한것>

# tuple unpacking(mutiple assignment)--알아보자!(밑에 계속)

# 장소와 회사변수를 각각 지정안해주고 한번에 지정할 수 있음
# company,location = html.find("div", {"class": "-company"}).find_all("span",recursive=False)
# 라고 하면 
# // recursive = false --안에 속해있는 모든 자손을 불러오지 말고 직계자손만, first level 만 불러옴!
# 예를 들어 아래와 같은 html 코드가 있다고 치고. 위에 코드를 쳤다고 치자.
# <div class = -company >
#   <span class = a>
#     KIA
#     <span class = b>LOL</span>
#   </span> 
#   <span class = a1>
#     KOREA
#   </span>
# </div>
# 그럼 직계자손 span 만 불러오므로 결과값은 company = KIA, location = KOREA 가 된다.