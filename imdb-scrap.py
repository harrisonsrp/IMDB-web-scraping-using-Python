import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import itertools
from reviewExtractor import *
import requests


df = pd.read_table('imdbRandomList/data.tsv')

# movie links
base_url = "https://www.imdb.com/title/"
#create url with unique title id
movie_links = [base_url + title_id + '/reviews?start=0' for title_id in df['titleId'].unique()]
print(movie_links[:10])
movie_soups = [getSoup(link) for link in movie_links[:10]]

# get all movie review
print("=====================================")
# get a list of soup links if link is not empty []
movie_review_list = [getReviews(movie_soup) for movie_soup in movie_soups if getReviews(movie_soup)]
# get review title from the review link
review_titles = [getReviewsTitle(movie_soup) for movie_soup in movie_soups if getReviews(movie_soup)]
# get reviewer_id  from the review link
reviewer_id = [getReviewerId(url) for url in movie_review_list]
# get reviewer name from the review link
reviewer_name = [getReviewerName(url) for url in movie_review_list]

print("There are a total of " + str(len(movie_review_list)) + " individual movie reviews")
print("Displaying 10 reviews")
print("=====================================")
# get review text from the review link
review_texts = [getReviewText(url) for url in movie_review_list if getReviewText(url)]
# get movie name from the review link
movie_titles = [getMovieTitle(url) for url in movie_review_list if getMovieTitle(url)]
# construct a dataframe
df = pd.DataFrame({'movie': movie_titles, 'reviewer_id': reviewer_id, 'reviewer_name' : reviewer_name, 'review_title': review_titles ,'user_review': review_texts})

# save the dataframe to a csv file.
df.to_csv('UserReviewIMDB/userReviews.csv', index=False)
print("Process Finished")