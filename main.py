from asyncore import write
from bs4 import BeautifulSoup
import requests
import time



print("Tell Us Your Skills : ")
unfamiliar_skill = input('> ')
print(f"Filtering Out {unfamiliar_skill}")



def find_jobs():

    

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')




    for index, job in enumerate(jobs):

        job_published_date = job.find('span',class_ = 'sim-posted').span.text
        if('few' in job_published_date):


            
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if(unfamiliar_skill not in skills):

                with open(f'posts/{index}.txt','w') as f:

                    f.write(f"Company Name : {company_name.strip()}")
                    f.write('\n')
                    f.write(f"Skills Required : {skills.strip()} ")
                    f.write('\n')
                    f.write(f"Job Info : {more_info}")
                    f.write('\n')
                    f.write(f"Date Published : {job_published_date.strip()}")
                    f.write('\n')
                print(f'File Saved : {index}')


if __name__=='__main__':

    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes ...")
        time.sleep(time_wait*60)
        print()