##############################
#  Module: reviewExtractor.py
#  Author: Shravan Kuchkula
#  Editor: Homayoun Sohrabpour (homayoun.srp@gmail.com)
#  Release Date: 07/13/2019
#  Edit Date: 05/22/2020
##############################
import re

import requests
from bs4 import BeautifulSoup


def getSoup(url):
    """
    Utility function which takes a url and returns a Soup object.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup




def getReviews(soup):
    '''Function returns a negative and positive review for each movie.'''

    # return the negative and positive review link
    link_list=[]
    review_link = soup.find_all('a', {'class': 'title', 'href': True})
    for links in review_link:
        # what to do if it's a list and not empty
        full_link = "https://www.imdb.com" + links['href']
        link_list = full_link



    return link_list

def getReviewerId(review_url):
    '''Returns the user review text given the review url.'''
    soup = getSoup(review_url)
    # return the negative and positive review link
    reviewer_id = soup.find('div', {'class': 'parent'}).find('a')['href']


    return reviewer_id

def getReviewerName(review_url):
    '''Returns the user review text given the review url.'''
    soup = getSoup(review_url)
    # return the negative and positive review link
    reviewer_name = soup.find('div', {'class': 'parent'}).find('a').getText()
    return reviewer_name


def getReviewText(review_url):
    '''Returns the user review text given the review url.'''

    # get the review_url's soup
    soup = getSoup(review_url)

    # find div tags with class text show-more__control
    tag = soup.find('div', attrs={'class': 'text show-more__control'})

    return tag.getText()


def getMovieTitle(review_url):
    '''Returns the movie title from the review url.'''

    # get the review_url's soup
    soup = getSoup(review_url)

    # find h1 tag
    tag = soup.find('h1')

    return list(tag.children)[1].getText()

def getReviewsTitle(soup):
    '''Function returns a negative and positive review for each movie.'''

    # return the negative and positive review link
    review_titles=[]
    review_link = soup.find_all('a', {'class': 'title', 'href': True})
    for links in review_link:
        # what to do if it's a list and not empty

        review_titles=links.getText()



    return review_titles