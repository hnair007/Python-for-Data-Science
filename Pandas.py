import pandas as pd
#Salaries.csv Datasets is in the same folder or can be downloaded from (https://www.kaggle.com/kaggle/sf-salaries)
salary = pd.read_csv('Salaries.csv')
#Average BasePay
salary['BasePay'].mean()
#highest amount of OvertimePay in the dataset
salary['OvertimePay'].max()
#Job title of CHRISTOPHER CHONG ?
salary[salary['EmployeeName']=='CHRISTOPHER CHONG']['JobTitle']
# How much does JOSEPH DRISCOLL make
salary[salary['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']
#What is the name of highest paid person (including benefits)?
salary[salary['TotalPayBenefits']== salary['TotalPayBenefits'].max()]
#What is the name of lowest paid person (including benefits)?
salary[salary['TotalPayBenefits']== salary['TotalPayBenefits'].min()]
#What was the average BasePay of all employees per year?
salary.groupby('Year').mean()['BasePay']
#How many unique job titles are there?
salary['JobTitle'].nunique()
#What are the top 5 most common jobs?
salary['JobTitle'].value_counts().head(5)
#How many Job Titles were represented by only one person in 2013? 
sum(salary[salary['Year']==2013]['JobTitle'].value_counts() == 1)
#How many people have the word Chief in their job title?
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
   sum(salary['JobTitle'].apply(lambda x: chief_string(x)))
