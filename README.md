# Louis George
## Capstone Project for the BrainStation Data Science Diploma Program
## [goodscriptbadscript.ca](www.goodscriptbadscript.ca)

The goal of this project is to determine if it is possible to predict whether or not a movie will be successful based solely upon its script.    

Although writing quality is undoubetly a subjective measure, if you have targets upon which to base something as good or bad, you can do some statistics and hope to pick something out of the noise. I wasn't expecting to make any breakthroughs in the understanding of human subjectivity, and the focus of this project was on the process, improving my code, and becoming familiar with the tools at my disposal. As a result of this, I was more intereseted in comparing and contrasting the most important features selected by the models used, in order to gain some insight as to how they work. The models which I chose to compare were: Logistic Regression, Random Forest, ADA Boost, and XG Boost.      

This is a Natural Language Processing (NLP) project, where I analysed around a thousand movie scripts in search of relationships between them which could be used to make predictions on a given target. My target variables are: IMDb score, Rotten Tomatoes score, and Profitability (measured by total worldwide revenue / budget). NLP is the act of transforming human language into numbers, so that you can put those numbers into conventional models like you would with numeric data. The first way to do this, and the method which I used, is called vectorization. This process invovles creating vectors out of all of your documents according to certain rules, resulting in one really big table. Another way to do this, called word embeding, is how you turn your words into numbers if you're going to use a neural network, and results in a matrix of tables.

My project is split into three components:
 - Data Collection
 - Data Science
 - Data Visualization
 
### Data Collection:

I scraped my data from three sources:
 - imsdb.com
 - imdb.com
 - omdbapi.com

I used selenium for all three of the scrapers, and had to parse through html and json to extract the necessary data. Lots of cleaning was required, as there was problems with formatting, and a variety nan related compromises. All cleaning was done with Pandas.    

All of the code for the scrapers can be found in the web_scrapers folder, and the cleaning was done in the EDA notebook.

### Data Science

The analysis was composed of:
 - Feature engineering
 - Target engineering
 - Modeling

Engineering the features involved:
 - Dummying the genres with Pandas.
 - Vectorizing the scripts using tf-idf from sklearn and a custom preprocessor and tokenizer which used SpaCy's library.
 - Counting the parts of speech with a function built using SpaCy's library.

Engineering the targets involved:
 - Creating the profitability target (Revenue/Budget).
 - Reclassifying the targets according to the selected thresholds as outlined in the Feature Engineering notebook.

Modeling
 - I began by investigating the possibility of using Latent Dirichlet Allocation (LDA) with the hypothesis that they would group into topics representative of the various genres. This was then visualized as described below.
 - Optimization of hyper parameters for the models was performed using sklearns grid search. Scores, and precision metrics were also recorded.
  - The Logistic Regression model was optimized for penalty type, and C value.
  - The Random Forest model was optimized for max depth, and number of estimators.
  - The ADA Boost model was optimized for learning rate, and number of estimators.
  - The XG Boost model was optimized for max depth, learning rate, and the number of estimators.
  
All work done here can be found in the Feature Engineering, and Modeling notebooks.

### Data Visualization

The visualization was composed of:
 - Plotting the results.
 - Creating a web application and deploying the models.

Plotting the results:
 - The LDA topics were further decomposed using t-SNE in an attempt to visualize the topics, and were plotted as a 3D scatter plot.
 - The distribution of the target as a histogram, as well as the most important features (highest coeffients for Logistic Regression, and highest gain for XG Boost) as bar plots were plotted.
 - All exploratory graphs were made with matplotlib, and final copies were made using Plotly.

Creating the web application:
 - Web app was created using Flask.
 - Deployed on a Linux server hosted by Linode.
 - The struggle was real with this part of the project, and I documented some of it with [a blog post](https://towardsdatascience.com/deploying-an-nlp-web-app-with-heroku-the-pickle-problem-f50113ed2367) published to Towards Data Science.
 
All work done here can be found in the Visualization notebook, and the web_app folder.

### Plots

<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~lougeo/52.embed"></iframe>
<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~lougeo/16.embed"></iframe>
<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~lougeo/18.embed"></iframe>
<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~lougeo/20.embed"></iframe>

### Results

<div align='center'>Logistic Regression Accuracy Scores</div>

|        |    train |     test | baseline |
|:-------|---------:|---------:|---------:|
| IMDb   | 0.671491 | 0.632035 |     0.57 |
| RT     | 0.68741  | 0.558442 |     0.43 |
| Profit | 0.59479  | 0.627706 |     0.61 |

    
<div align='center'>Logistic Regression Precision Metrics</div>

|    | target   |   class |   precision |   recall |   f1-score |   support |
|---:|:---------|--------:|------------:|---------:|-----------:|----------:|
|  0 | IMDb     |       0 |    0.576923 | 0.463918 |   0.514286 |        97 |
|  1 | IMDb     |       1 |    0.660131 | 0.753731 |   0.703833 |       134 |
|  2 | RT       |       0 |    0.603896 | 0.69403  |   0.645833 |       134 |
|  3 | RT       |       1 |    0.467532 | 0.371134 |   0.413793 |        97 |
|  4 | Profit   |       0 |    0.347826 | 0.101266 |   0.156863 |        79 |
|  5 | Profit   |       1 |    0.658654 | 0.901316 |   0.761111 |       152 |

     
<div align='center'>XG Boost Accuracy Scores</div>

|        |   train |     test | baseline |
|:-------|--------:|---------:|---------:|
| IMDb   |       1 | 0.601732 |     0.57 |
| RT     |       1 | 0.580087 |     0.43 |
| Profit |       1 | 0.588745 |     0.61 |
     
    
<div align='center'>XG Boost Precision Metrics</div>

|    | target   |   class |   precision |   recall |   f1-score |   support |
|---:|:---------|--------:|------------:|---------:|-----------:|----------:|
|  0 | IMDb     |       0 |    0.53012  | 0.453608 |   0.488889 |        97 |
|  1 | IMDb     |       1 |    0.641892 | 0.708955 |   0.673759 |       134 |
|  2 | RT       |       0 |    0.610778 | 0.761194 |   0.677741 |       134 |
|  3 | RT       |       1 |    0.5      | 0.329897 |   0.397516 |        97 |
|  4 | Profit   |       0 |    0.357143 | 0.253165 |   0.296296 |        79 |
|  5 | Profit   |       1 |    0.662857 | 0.763158 |   0.70948  |       152 |

    
<div align='center'>Random Forest Accuracy Scores</div>

|        |    train |     test | baseline |
|:-------|---------:|---------:|---------:|
| IMDb   | 0.892909 | 0.61039  |     0.57 |
| RT     | 1        | 0.623377 |     0.43 |
| Profit | 1        | 0.649351 |     0.61 |
    
    
<div align='center'>Random Forest Precision Metrics</div>

|    | target   |   class |   precision |   recall |   f1-score |   support |
|---:|:---------|--------:|------------:|---------:|-----------:|----------:|
|  0 | IMDb     |       0 |    0.6      | 0.216495 |   0.318182 |        97 |
|  1 | IMDb     |       1 |    0.612245 | 0.895522 |   0.727273 |       134 |
|  2 | RT       |       0 |    0.625668 | 0.873134 |   0.728972 |       134 |
|  3 | RT       |       1 |    0.613636 | 0.278351 |   0.382979 |        97 |
|  4 | Profit   |       0 |    0.444444 | 0.101266 |   0.164948 |        79 |
|  5 | Profit   |       1 |    0.666667 | 0.934211 |   0.778082 |       152 |
    
    
<div align='center'>ADA Boost Accuracy Scores</div>

|        |    train |     test | baseline |
|:-------|---------:|---------:|---------:|
| IMDb   | 0.9233   | 0.601732 |     0.57 |
| RT     | 1        | 0.575758 |     0.43 |
| Profit | 0.723589 | 0.640693 |     0.61 |
    
    
<div align='center'>ADA Boost Precision Metrics</div>

|    | target   |   class |   precision |   recall |   f1-score |   support |
|---:|:---------|--------:|------------:|---------:|-----------:|----------:|
|  0 | IMDb     |       0 |    0.537313 | 0.371134 |   0.439024 |        97 |
|  1 | IMDb     |       1 |    0.628049 | 0.768657 |   0.691275 |       134 |
|  2 | RT       |       0 |    0.621622 | 0.686567 |   0.652482 |       134 |
|  3 | RT       |       1 |    0.493976 | 0.42268  |   0.455556 |        97 |
|  4 | Profit   |       0 |    0.433333 | 0.164557 |   0.238532 |        79 |
|  5 | Profit   |       1 |    0.671642 | 0.888158 |   0.764873 |       152 |


### Interpretation of Results

The main focus with regards to the interpretation of the results is, for me, the somewhat humerous comparison of the most important features, as displayed in the graphs. I have also included some tables above with accuracy, precision, recall, and other such metrics. These metrics were made using the hyper parameters of the best performing model in the 5 fold cross validated grid search. The precision and recall were relatively consistent between the two models, and there are only a few additional points I would like to make in regards to these metrics:    
 - With regards to the accuracy score:
   - Logistic Regression performs the best targeting the IMDb score.
   - Random Forest performs the best on both Rotten Tomatoes score, and Profitability.
   - With only slight exception, the decision tree based models are overfitting.
 - With regards to the other metrics:
   - When looking at the IMDb, and Profitability scores, all models are significantly better at predicting whether a script will result in good scores, rather then bad scores. 
   - When looking at the Rotten Tomatoes scores, the opposite is true, and the models are better at detecting scripts which will result in bad movies rather than good ones. 

### Considerations, and next steps

There are without a doubt, a plethora of confounding factors when looking at what makes a movie successful or not. These factors range from the obvious, such as who's directing the movie, all the way to who's making decisions on the marketing. It is also important to note that there is selection bias in the data I collected, as I only used scripts which were made into movies.    

Having said that, there most certainly is opportunity for this kind of analysis to be commercialized. The most obvious example would be to aid in the decision making process which production companies undertake when considering spending large quantities of money to produce a movie, or tv show. Tools such as this are simply that - tools, but having any kind of qualitative metric upon which to base decisions is generally helpful.     

Moving forward here is a short bucket list of things which would improve this project:
 - Modeling
   - Further optimize the models, to try to get better accuracy rather then interpretability.
   - Build out a neural network.
 - Web App
   - Improve the design, and functionality of the website.
All of the above would of course be made significantly more interesting with the availablilty of a more extensive, and complete data source.    

Thanks for reading!
Louis