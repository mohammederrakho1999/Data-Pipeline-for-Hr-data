candidates_table_create = ("""
CREATE TABLE IF NOT EXISTS candidates(
  candidate_id INT PRIMARY KEY NOT NULL,
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
  practice_name VARCHAR,
  salary_hike_percent INT, 
  social_adv INT
  );
""")

offer_table_create = ("""
CREATE TABLE IF NOT EXISTS offers(
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

demographics_table_create = ("""
CREATE TABLE IF NOT EXISTS demographics(
  passeport_number VARCHAR PRIMARY KEY NOT NULL,
  gender VARCHAR,
  country VARCHAR, 
  age INT, 
  postal_code INT, 
  email VARCHAR,
  phone INT, 
  address VARCHAR
  );
""")
