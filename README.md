# Wikipedia Scraping

The purpose of this project is to examine a corpus of Wikipedia
articles with both supervised and unsupervised learning techniques.
It combines retrieval of pages using the Wikipedia API, uploading and
downloading page info from a SQL database, searching for relevant
pages given an input phrase, and match pages to categories.

### download

./download [list of category names and/or .yml files from which to load category names]

The download script loops through a list of categories.  For each, it
queries the Wikipedia API for the list of pages associated with that
category, then downloads and cleans the text from each of those pages.
The category and individual page info is inserted into the SQL
database.

### search

./search [string of words]

The search script first loads the vectorized pages from the SQL
database.  It then vectorizes the input sting of words, and performs a
comparison (through dot-product) to the pages in the database.  The
five strongest correlations are then output.

### train-model

./train-model

The training script load the raw pages from the SQL database.  It
chooses all pages which correspond with a single category, and removes
any categories with less than 10 associated pages.  Each page's corpus
is vectorized using CountVectorizer from scikit-learn, removing stop
words and using a threshold for the minimum number of documents in
which pages appear of [30,100,300,1000].  A cross-validated grid
search is performed using K-Nearest Neighbors, Logistic Regression,
SVC, Decision Tree, Random Forest, Extra Trees.  The best model across
all models and thresholds is saved as a pickle, along with the trained
vectorizing transformer for the associated threshold.

### predict

./predict [page_id for a Wikipedia page]

The prediction script loads the existing vectorizing transformer and
most predictive model from pickles.  It then loads the cleaned text
from the input Wikipedia page, transforms it, and predicts the
category.