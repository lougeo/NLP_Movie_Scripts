# Louis George
## Capstone Project for the BrainStation Data Science Diploma Program
## [goodscriptbadscript.ca](www.goodscriptbadscript.ca)

The goal of this project is to determine if it is possible to predict whether or not a movie will be successful based solely upon its script.    

Although writing quality is undoubetly a subjective measure, if you have targets upon which to base something as good or bad, you can do some statistics and hope to pick something out of the noise. I wasn't expecting to make any breakthroughs in the understanding of human subjectivity, and the focus of this project was on the process, improving my code, and becoming familiar with the tools at my disposal. As a result of this, I was more intereseted in comparing and contrasting two different models used, in order to gain some insight as to how they work. The two models I chose to compare were a linear model, in the form of Logistic Regression, and a decision tree, in the form of Gradient Boosting.      

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
 - Optimization of hyper parameters for the Logisitic Regression, and XG Boost model was performed using sklearns grid search. Scores, and precision metrics were also recorded.
     - I didn't optimize for any models other than these two because I was only looking for interpretability and comparing and contrasting the decisions made by these two models, rather than chipping away at the accuracy score.
     - The Logistic Regression was tuned for penalty type, and C value.
     - The XG Boost model was tuned for max depth, learning rate, and the number of estimators.
  
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
<div align='center'>
    <div>
        <a href="https://plotly.com/~lougeo/52/?share_key=nYPNBdBaLZWJXo8iyBvZ9D" target="_blank" title="tSNE" style="display: block; text-align: center;"><img src="https://plotly.com/~lougeo/52.png?share_key=nYPNBdBaLZWJXo8iyBvZ9D" alt="tSNE" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plotly.com/404.png';" /></a>
    </div>
    <div>
        <a href="https://plotly.com/~lougeo/16/?share_key=jLpxuaGbc0dO8vu5pKf8q2" target="_blank" title="IMDb" style="display: block; text-align: center;"><img src="https://plotly.com/~lougeo/16.png?share_key=jLpxuaGbc0dO8vu5pKf8q2" alt="IMDb" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plotly.com/404.png';" /></a>
    </div>
    <div>
        <a href="https://plotly.com/~lougeo/18/?share_key=N324MXHqZ4LrTJd2uZsXMq" target="_blank" title="RT" style="display: block; text-align: center;"><img src="https://plotly.com/~lougeo/18.png?share_key=N324MXHqZ4LrTJd2uZsXMq" alt="RT" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plotly.com/404.png';" /></a>
    </div>
    <div>
        <a href="https://plotly.com/~lougeo/20/?share_key=dSI5wVoe7m9Yuz8CNEEiXB" target="_blank" title="Profit" style="display: block; text-align: center;"><img src="https://plotly.com/~lougeo/20.png?share_key=dSI5wVoe7m9Yuz8CNEEiXB" alt="Profit" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plotly.com/404.png';" /></a>
    </div>
</div>

### Results

<div>Logistic Regression Accuracy Scores</div>

|        |    train |     test | baseline |
|:-------|---------:|---------:|---------:|
| IMDb   | 0.671491 | 0.632035 |     0.57 |
| RT     | 0.68741  | 0.558442 |     0.43 |
| Profit | 0.59479  | 0.627706 |     0.61 |


<div>Logistic Regression Precision Metrics</div>

|    | target   |   class |   precision |   recall |   f1-score |   support |
|---:|:---------|--------:|------------:|---------:|-----------:|----------:|
|  0 | IMDb     |       0 |    0.576923 | 0.463918 |   0.514286 |        97 |
|  1 | IMDb     |       1 |    0.660131 | 0.753731 |   0.703833 |       134 |
|  2 | RT       |       0 |    0.603896 | 0.69403  |   0.645833 |       134 |
|  3 | RT       |       1 |    0.467532 | 0.371134 |   0.413793 |        97 |
|  4 | Profit   |       0 |    0.347826 | 0.101266 |   0.156863 |        79 |
|  5 | Profit   |       1 |    0.658654 | 0.901316 |   0.761111 |       152 |


<div>XG Boost Accuracy Scores</div>

|        |   train |     test | baseline |
|:-------|--------:|---------:|---------:|
| IMDb   |       1 | 0.601732 |     0.57 |
| RT     |       1 | 0.580087 |     0.43 |
| Profit |       1 | 0.588745 |     0.61 |
     

<div>XG Boost Precision Metrics</div>

|    | target   |   class |   precision |   recall |   f1-score |   support |
|---:|:---------|--------:|------------:|---------:|-----------:|----------:|
|  0 | IMDb     |       0 |    0.53012  | 0.453608 |   0.488889 |        97 |
|  1 | IMDb     |       1 |    0.641892 | 0.708955 |   0.673759 |       134 |
|  2 | RT       |       0 |    0.610778 | 0.761194 |   0.677741 |       134 |
|  3 | RT       |       1 |    0.5      | 0.329897 |   0.397516 |        97 |
|  4 | Profit   |       0 |    0.357143 | 0.253165 |   0.296296 |        79 |
|  5 | Profit   |       1 |    0.662857 | 0.763158 |   0.70948  |       152 |


### Interpretation of Results

The main focus with regards to the interpretation of the results is, for me, the somewhat humerous comparison of the most important features, as displayed in the graphs. I have also included some tables above with accuracy, precision, recall, and other such metrics. These metrics were made using the hyper parameters of the best performing model in the 5 fold cross validated grid search. The precision and recall were relatively consistent between the two models, and there are only a few additional points I would like to make in regards to these metrics:    
 - With regards to the accuracy scores, both models were able to make the best predictions for the Rotten Tomatoes score, followed by IMDb, and finally Profitiability, whose results likely aren't significantly different then random (statistical test would be required). 
 - When looking at the IMDb, and Profitability scores, both models are significantly better at predicting whether a script will result in good scores, rather then bad scores. 
 - When looking at the Rotten Tomatoes scores, the opposite is true, and the models are better at detecting scripts which will result in bad movies rather than good ones. 

### Considerations, and next steps

There are without a doubt, a plethora of confounding factors when looking at what makes a movie successful or not. These factors range from the obvious, such as who's directing the movie, all the way to who's making decisions on the marketing. It is also important to note that there is selection bias in the data I collected, as I only used scripts which were made into movies.    

Having said that, there most certainly is opportunity for this kind of analysis to be commercialized. The most obvious example would be to aid in the decision making process which production companies undertake when considering spending large quantities of money to produce a movie, or tv show. Tools such as this are simply that - tools, but having any kind of qualitative metric upon which to base decisions is generally helpful.     

Moving forward here is a short bucket list of things which would improve this project:
 - Modeling
     - Further optimize the models, potentially looking outside of the two used, to try to get better accuracy rather then interpretability.
     - Build out a convolutional neural network.
 - Web App
     - Improve the design, and functionality of the website.
All of the above would of course be made significantly more interesting with the availablilty of a more extensive, and complete data source.    

Thanks for reading!    
Louis