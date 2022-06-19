import pandas as pd
import numpy as np

n_names = 500
data = {
    "job_title": [],
    "job_grade": [],
    "fte_category": [],
    "engineering_school": [],
    "line_of_business": [],
    "type_of_contact_prefered": [],
    "reason_for_rejection": [],
    "performance": [],
    "joined": []
}

job_titl = ["Data Engineer", "Data Analyst", "Data Scientist", "Sap Consultant", "BI engineer", "Software Engineer", "Data Gov Consultant",
            "Informatica Consultant", "Salesforce Consultant", "Talent Acquisition Specialist", "Cloud & Devops Engineer", "Test Engineer"]
job_grad = ["C2", "C1", "SC1", "M", "J", "SC2"]
#team_nam = ["AIM","SAP","HRT","RPA","SF"]
fte_categor = ["Full Time", "Freelance"]
#tenure_rang = []
engineering_schoo = ["INPT", "EMI", "ENSIAS",
                     "INSEA", "ENIM", "ENSA", "FST", "UIR", "EMSI", "Centrale Casablanca", "ENSET"]
line_of_busines = ["Retail", "Finance service", "Audit",
                   "Insurance", "Human Ressources Management", "Health", "Accounting", "Education", "Transportation", "Telecommunication", "Electronic Commerce", "Customer Relationship Management"]
type_of_contact_prefere = ["Email", "Phone"]
organizatio = ["Deloitte Casablanca",
               "Deloitte France", "Deloitte USA", "Deloitte UK"]
#main_skill =  ["python/SQL","machine learning","data science","aws/azure/gcp","terraform","pytest/jest","sap","salesforce","tableau/powerbi","informatica","postresql","mysql"]
reason_for_rejectio = ["Candidate_not_prepared",
                       "Skills_does_not_match", "Not_culturally_fit"]
#leave_take = []
#terminatio = []
#percent_hik = []
performanc = ["Good", "Low", "Medium"]
joine = ["Joined", "Not_joined"]

job_title = np.random.choice(job_titl, n_names)
job_grade = np.random.choice(job_grad, n_names)
fte_category = np.random.choice(fte_categor, n_names)
engineering_school = np.random.choice(engineering_schoo, n_names)
line_of_business = np.random.choice(line_of_busines, n_names)
type_of_contact_prefered = np.random.choice(type_of_contact_prefere, n_names)
reason_for_rejection = np.random.choice(reason_for_rejectio, n_names)
performance = np.random.choice(performanc, n_names)
joined_or_not = np.random.choice(joine, n_names)

data["job_title"].extend(job_title)
data["job_grade"].extend(job_grade)
data["fte_category"].extend(fte_category)
data["engineering_school"].extend(engineering_school)
data["line_of_business"].extend(line_of_business)
data["type_of_contact_prefered"].extend(type_of_contact_prefered)
data["reason_for_rejection"].extend(reason_for_rejection)
data["performance"].extend(performance)
data["joined"].extend(joined_or_not)


data_gen = pd.DataFrame(data)
data_gen.to_csv("C:/Users/info/Desktop/pfe deloitte/employees.csv")
