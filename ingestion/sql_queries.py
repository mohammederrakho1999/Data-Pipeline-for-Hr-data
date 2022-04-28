candidate_table_drop = "DROP TABLE IF NOT EXISTS public.candidates"
offer_table_drop = "DROP TABLE IF NOT EXISTS public.offers"


candidates_table_create = ("""
CREATE TABLE IF NOT EXISTS public.candidates(
  candidate_id INT PRIMARY KEY NOT NULL,
  offer_id VARCHAR,
  job_title VARCHAR,
  job_grade VARCHAR,
  fte_category VARCHAR, 
  engineering_school VARCHAR, 
  line_of_business VARCHAR, 
  type_of_contact_prefered VARCHAR,
  reason_for_rejection VARCHAR, 
  performance INT,
  time_to_join INT, 
  joined VARCHAR, 
  years_of_ex INT,
  salary_hike_percentage INT, 
  social_adv INT
  );
""")

offers_table_create = ("""
CREATE TABLE IF NOT EXISTS public.offers(
  offer_id VARCHAR PRIMARY KEY NOT NULL,
  offer_designation VARCHAR,
  num_applicants INT, 
  num_rejections INT, 
  num_shortlisted INT, 
  num_offers_provided INT, 
  num_offers_accepted INT, 
  offer_date DATE
  );
""")

insert_candidate_table = (
    """INSERT INTO public.candidates VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""")
insert_offers_table = (
    """INSERT INTO public.offers VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""")
