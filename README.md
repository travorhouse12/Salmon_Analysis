# Salmon_Analysis

# Dashboard

Follow this link to get in touch with our google slides presentation for segment 2! You'll be able to see the mockup of our presentation and answering questions for our segment 2 requirements. 

https://docs.google.com/presentation/d/10R9gvxBUOt1RNUjTFMUJGDPdhrtOrSDcN_3XxHq1TQQ/edit?usp=sharing

The storyboard for the Dashboard can be located on the Google Slides draft as well as in the SB folder on the main branch. 

Extra Information on the Dashboard Section

- The blue print for the storyboard is just a mockup. There may be more on the storyboard then really will be completed for the dashboard. The more ideas the easier the process will be to complete it.

- There will be a seperate storyboard/presentation created through Tableau as well as the app.

- A JSON file was created from the preprocess CSV which you can find the code and the JSON file in the JSON folder above. Another JSON file will be created now that the ML is finished. 

## Description of Communication Protocols

The salmon team makes use of various forms of communication, including:
- Slack for basic back-and-forth communication about the project and questions.
- Zoom for video calls during class and office hours. Our video calls are when we get most of our communication done.

## Outline of the Project

How many salmon do we need to spawn for streams X, X, and X to meet the benchmark?

The goal of this project is to find out how many Salmon that we will have to harvest for years to come. To find this number, we will take the average number of spawners for X amount of years for X, X, and X streams. This average will define the benchmark that each stream will need to meet each year.

We will then build a machine learning model to predict the number of salmon for the next year. We will also build a machine learning model to predict the fraction of wild salmon for the next year. Based on the predicted number of spawners, we will take the predicted fraction of wild salmon to determine the remaining number of fish we will need to spawn the following year.

If we notice any fluctuations in population, we will pull in other datasets to determine possible reasons why the salmon population might’ve dipped or risen in the specific time period.

Notes:
X is being used as a placeholder until we decide on the streams and amount of years that we will use.

### ROLES
**Square:** Travor – His job is to manage the repository and make sure everything is up to date, and clean for our project.
**Triangle:** Matt – Will be working on creating a mockup of a machine learning model.
**Circle:** Adam – His job is to create a mockup of a database with a set of sample data. Mainly, so that we can ensure our database
**X:** Nora – This member will oversee which technologies to use for each step of the project.

We have decided on these roles for one another but are not limited to role in any way. We will all be working through each role and helping one another with ideas and feedback which is important for the project to run smoothly!


## VISUALIZATION OUTLINE

This is a small mockup of potential visualization tools we can possibly use for our project:

-	Line Plots
-	Histograms
-	Scatter Plots
-	Matplotlib figures/diagrams
-	Bootstrap
-	HTML
-	Javascript/HTML for our website creation (i.e UFO / Mapping Earthquakes projects)
-	Heatmaps
-	Tableau Maps

## Progress Made to the Machine Learning Model as of 2/27
- Completed primary data preprocessing in salmon_ml_preprocessing
   - Deleted "Unnamed: 0" Column
   - We had a substantial amount of duplicate rows so we dropped all duplicates
   - Dropped all values from our variables that were below 0 (There were a lot of '-99' values instead of 'NaN'
   - Created arrays to hold our Previous Year and Two Years Prior independendent values
   - Deleted first row and added our Previous Year variables to the DataFrame
   - Deleted first row of augmented DataFrame and assed our Two Years Prior arrays to the DataFrame
   - Renamed columns to remove spaces
   - Created salmon_preprocessed.csv
- Completed secondary data preprocessing in salmon_ml_model (feature selection)
   - Set up our dependencies
   - Added a placeholder to connect to our pgAdmin Database
   - loaded in salmon_preprocessed.csv
   - Isolated target stream
   - Delete thhe first two lines of data since it would hold the Previous Year and Two Years Prior values from the previous stream in the dataset
   - Set up a scaler for our Previous Year and Two Years Prior columns
   - Created a dataframe with the scaled data and then merged it with the original data frame with the unscaled columns removed
   - Created variables to hold our features and our target 
   - We decided that for our model to be forcasting, it was important that we use the Previous Year and Two Years Prior columns for our independent values as well as the Brood_Year
   - Our features are: 'Brood_Year', 'Spawners_Prev_Yr_Sc', 'Eff_Catch_Prev_Yr_Sc', 'Fracwild_Prev_Yr_Sc', 'Spawners_Two_Yrs_Prior_Sc', 'Eff_Catch_Two_Yrs_Prior_Sc' and 'Fracwild_Two_Yrs_Prior_Sc'
- Split our testing and training sets
   - We have initially used the default testing and training ratios
- Initiated a Multiple Linear Regression Model
   - We chose this model because it seemed ideal for our continuos data type of our target
   - We understand that our number of features and the nature of our data is not ideal for a linear regression model
   - We will continue to adjust our features, use different data sets to train our model, adjust our scaling and we may need to pick a better model for our data set    	

## Database Mockup
Database being leveraged:

- PostegreSQL
- AWS RDS

Selected Topic: 

Population Change in Chinook Salmon

Reason Why We Selected This Data:

We chose this topic because the population of Chinook Salmon are very local to the Pacific Northwest. It is very important to understand what is going on within the local watersheds to help prevent disaster. This project will help us really understand what has happened over so many years with the spawning and reproduction of this species, and what may have caused an increase or a decrease in this population!


Description Of The Data Source: 

Our data source is coming from NOAA.Gov. This link will bring you directly to the data source. This dataset has more than 30 + columns and 60,000+ rows so there is plenty of data to work with. We will not need all of this data for the main portion of the project but may need to go back and use it for a comparison later on. You can see where we filtered this very large dataset to contain only the chinook salmon populations in the Filter_Fish_Data.ipynb. 

Link to our data source:

https://www.webapps.nwfsc.noaa.gov/apex/parrdata/inventory/tables/table/population_data_and_references_for_the_salmon_population_summary_sps_database 

Questions We Are Looking To Answer: 

Can salmon populations be predicted? Are salmon populations stable? Is the work being done to restore salmon habitat currently effective?
