import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver

driver = webdriver.Chrome(executable_path = r"C:\Users\sachin\Desktop\chromedriver.exe")
driver.get("https://www.monsterindia.com/search/walkin-jobs?searchId=ef8c61fa-cd57-4d07-9308-6778eafc3687")
source = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

#print(source)

csv_file = open('Monster_jobs_details_summary1.csv','w')
csv1 = csv.writer(csv_file) 
csv1.writerow(['Job Title','Company Name','Location','Experience','Salary','Job Description'])
soup_obj = BeautifulSoup(source,'lxml')


company_name=soup_obj.find_all('span' ,class_='exp col-xxs-12 col-sm-3 text-ellipsis')

job_description=soup_obj.find_all('p' ,class_='job-descrip')
job_skills=soup_obj.find_all('p' ,class_='descrip-skills')


div_entire = soup_obj.find_all('div' ,class_='card-apply-content')
for items in div_entire:
        
            job_title=items.find('div' ,class_='job-tittle')
            x=job_title.h3.text
            print (x)

            company_name=items.find('span' ,class_='company-name')
            company_names=company_name.a.text
            print(company_names)
            

            location_name=items.find('div' ,class_='searctag row')
            locations = location_name.find('div' ,class_='col-xxs-12 col-sm-5 text-ellipsis')
            location = locations.span.text.strip()
            print (location)
            try:
                experience_years= location_name.find('div' ,class_='exp col-xxs-12 col-sm-3 text-ellipsis')
                experience = experience_years.span.text.strip()
                print(experience)

            except Exception as e:
                experience=None

            Salary_all= location_name.find('div' ,class_='package col-xxs-12 col-sm-4 text-ellipsis')
            salary=Salary_all.span.text.strip()
            print (salary)

            job_descprition = items.find('p' ,class_='job-descrip')
            descp= job_descprition.text.replace('<br>','').strip()
            print (descp)

            print("====================================================================")
            myarr= [x,company_names,location,experience,salary,descp]
            df = [''.join(i for i in str(x) if (ord(i)<128) and type(x) is not None) for x in myarr]
            csv1.writerow(df)
csv_file.close()
        
    


#exp col-xxs-12 col-sm-3 text-ellipsis
    

    




