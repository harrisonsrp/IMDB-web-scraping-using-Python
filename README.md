# python-review-scraping-imdb-movie-site-with-BeautifulSoup
With this Code you can have a data set from IMDB users with their reviews , user_id , username , movie_title , and review_id

# Lets start to learn how to use this code :

put reviewExtractor and imdb-scrap.py in a folder.(UserReviewIMDB folder is your output)

# install packages :
you need to install pandas , beautifulsoup4 , numpy :
<div class="highlight highlight-source-shell"><pre>pip install pandas</pre></div>
<div class="highlight highlight-source-shell"><pre>pip install numpy</pre></div>
<div class="highlight highlight-source-shell"><pre>pip install beautifulsoup4</pre></div>

# Download IMDB movie id data set:
For scraping IMDB movies we need movie id , you can downlaod movie id from the link below :
<div class="highlight highlight-source-shell"><a href="https://datasets.imdbws.com/title.akas.tsv.gz">https://datasets.imdbws.com/title.akas.tsv.gz</a></div>

# Load ids :
After downloading the data set you need to extract it and put it in your project folder and load it with pandas dataframe :
<div class="highlight highlight-source-shell"><pre>df = pd.read_table('yourFileName.tsv')</pre></div>

# Save your dataset :
For saving the data that you scraped , you need to create an empty csv file and then link it to your code :
<div class="highlight highlight-source-shell"><pre>df.to_csv('yourEmptyCsvFile.csv', index=False)</pre></div>


This codes has been written by Shravan Kuchkula and I upgraded it for a better performance
<hr>
If you had any issues just tell me : homayoun.srp@gmail.com
