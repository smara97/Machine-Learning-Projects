# Resume Parser


Resume parser analyze a resume, extract the desired information, and insert the information into a database with a unique entry for each candidate. Once the resume has been analyzed, a recruiter can search the database for keywords and phrases and get a list of relevant candidates

extract information like : 	Name , college , designation , graduation , email , mobile ,links , achievements, number ,skills ,…..etc .


Using 2 Model in training :


### first model – base cased Bert with spacy nlp and tokenizer of base cased bert 

- Have 30 epochs of training take ~4 hours in training , have about 14 tags (achievements, address, Certifications, College, Companies, degree, Designation
email, state, training, projects, location, university and graduation).

- Training jupyter notebook file resume_spacy.ipynb


### second model have 2 models of sapcy (Custom training of spacy in NER ) and English spacy model in nlp for NER 

- Have about 11 tags (name, designation, college, email, mobile_number, experience, no_of_pages
total_experience, skills, companies and location). 

- Have 60 epochs of training take about ~5 hours .
- Get Accuracy 92%


- Training jupyter notebook file resume_parser_bert.ipynb



- After trained 2 models merge them to one file : resume_parser.ipynb



Datasets:

collecting about 701 annotation Cvs : https://drive.google.com/open?id=1TCsi-VF4OW4H5XNCTfhsaX5g9FJD60Rg








input file : 

<object data="https://github.com/smara97/Machine-Learning-Projects/blob/master/Resume%20Parsing/Ahmed%20Muhammad.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/smara97/Machine-Learning-Projects/blob/master/Resume%20Parsing/Ahmed%20Muhammad.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/smara97/Machine-Learning-Projects/blob/master/Resume%20Parsing/Ahmed%20Muhammad.pdf">Download PDF</a>.</p>
    </embed>
</object>

![alt text](https://github.com/smara97/Machine-Learning-Projects/blob/master/Resume%20Parsing/Ahmed%20Muhammad.pdf)

output : 

{'achievements': [{'name': 'in Contests'}],
 'address': [],
 'certifications': [],
 'college': [{'name': 'Assiut University'}, {'name': 'Assiut'}],
 'companies': [{'name': 'iNetworks'}],
 'degree': [],
 'designation': [{'name': 'Computer Science Student'},
  {'name': 'Data Scientist'}],
 'email': 'ahmedsmara33@gmail.com',
 'experience': ['Computers and Information, Assiut University — Bachelor’s degree',
  'Undergraduate (Aug 2016 –Aug 2020)',
  'Intern Data Scientist at Wakeb  — Egypt',
  '- Learned and deployed machine learning models and algorithms.',
  '- Worked on chat-bots and the dialects in Arabic language.',
  '- Implemented sentiment analysis model on Arabic sentences.',
  '- Analysis of the content of social networks into negative and positive impressions.',
  '(Jan 2020– Mar 2020)',
  'Intern Data Scientist at iNetworks — Egypt',
  '- Learned and deployed machine learning models and algorithms.',
  '- Implemented text classification model, recognition system and Sentiment analysis model in English sentences.',
  '(Jan 2020– Mar 2020)',
  'Remotely Data Scientist – NLP  at m06 — Netherlands                                                (Apr 2020– Jun 2020)',
  '- Worked on automated machine learning (AutoML) models.',
  '- Implemented text classification model and sentiment analysis model.',
  '- Used English movies reviews data-set and BERT model.',
  '- Worked on resume parsing, resume parser analyzes a resume, extract the desired information and insert the information',
  'into a database with a unique entry for each candidate.',
  '- Used BERT and NLP spacy models.'],
 'graduation': [],
 'links': None,
 'location': [{'name': 'Cairo'}],
 'mobile_number': [{'name': '1003524082'}],
 'name': [{'name': 'Ahmed Muhammad Sayed'}],
 'no_of_pages': 2,
 'projects': [],
 'skills': [{'name': 'Spacy'},
  {'name': 'Machine learning'},
  {'name': 'Github'},
  {'name': 'Database'},
  {'name': 'Pytorch'},
  {'name': 'Keras'},
  {'name': 'Java'},
  {'name': 'Analysis'},
  {'name': 'Programming'},
  {'name': 'Email'},
  {'name': 'Statistics'},
  {'name': 'Visual'},
  {'name': 'R'},
  {'name': 'Content'},
  {'name': 'English'},
  {'name': 'Tensorflow'},
  {'name': 'System'},
  {'name': 'Facebook'},
  {'name': 'Parser'},
  {'name': 'Mathematics'},
  {'name': 'Python'},
  {'name': 'Cloud'},
  {'name': 'C++'},
  {'name': 'Algorithms'}],
 'total_experience': 4.5}

