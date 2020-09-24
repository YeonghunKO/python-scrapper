import csv

def save_to_file(jobs):
    file = open("C:\python scraper\jobs.csv", mode="w" ,encoding = "utf-8-sig") # 파일 이름이 없으면 자동으로 파일 생성. 그리고 일본어,중국어 때문에 파일이 깨진다면 -sig를 encoding에 추가!
    writer = csv.writer(file) # 만든 파일안애 데이터 입력
    writer.writerow(["title", "company", "location", "link"]) # 요런 식으로
    for job in jobs:
        writer.writerow(list(job.values())) 
        #그리고 우리가 가져오려는 값이 "company" : "full stack python devloper" 라고 되어있다 
        # 이때 key,value 중 value 만 가져오려면 ~~.value 이런식으로 코드를 적으면 된다.    
    return


#
