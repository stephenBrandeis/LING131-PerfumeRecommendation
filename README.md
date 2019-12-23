# LING131-PerfumeRecommendation
By Jingya Cao, Shixuan Wan, Siyuan Chen, Xin Shen,

1.Background Information
For the people who want to buy the perfume, you will often find yourself overwhelmed by different kinds of perfumes when you search online.
Even you search them based on certain filters, you still have to select one from several web pages by reading the long, unusual and highly 
descriptive introductions. Those poetic introductions describe the feelings emotionally. Those introductions even use a scene to describe 
the moment someone smells the perfume, which takes some time to understand. Picking the perfume by reading introductions is absolutely 
time-consuming. As a perfume customer who is confused by the introductions and want to find the right perfume in a short time, our perfume
recommendation system is a good choice for them.
2. Goals of the system
The aim of this system is to give 5 recommendations based on the description input, which increases the choosing efficiency. The special 
corpus of the perfume is good for NLP. It contains the emotion, the feeling and the personality description. When the people input a 
descriptive text, the model can return the perfume that matches the input text. What’s more, our system includes sentiment analysis. 
The system can detect your likes and dislikes. 
3. How to run
 Module Requirement: 
    Scipy >=  1.3.0 
    Numpy >=1.16.0 
    Matplotlib >= 3.1.0 
    Skimage > 0.15.0 
    Nltk >=3.4.0 
    Genism >=3.8.0 
    Sklearn > 0.21.0 
 File Description
  get_data.py: A web scraping script to get the data frame of perfume source data. we have already scrape the data we need and store it 
  in the ‘perfume_data.pkl’ file so you do not have to scrape the data again. Simply load the data using ‘pickle.load’ function is fine.
  
  model_training.ipynb: Include text pre-processing and two model training(TF-IDF and Doc2Vec).  We have vectorized the raw data and 
  persist them into several pickle files so as to be used directly. 
  
  run_model.ipynb: Show the query results in the interface. 
  
  information_retrieval_model.py: Run the model we have trained We have scraped the raw data, trained the model and persist them into 
  files so simply run the ‘run_model.ipynb’ file and input the sentence into the box, you would get perfume recommendation. 
  
  
