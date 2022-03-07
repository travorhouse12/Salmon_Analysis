# Salmon_Analysis

# Dashboard

Follow this link to get in touch with our google slides presentation for segment 2! You'll be able to see the mockup of our presentation and answering questions for our segment 2 requirements. 

https://docs.google.com/presentation/d/1_tHgs23qMZGwq0RtyLZu3yQ7rGeU5Wllu7NAGIvpXs4/edit#slide=id.g118c62022ce_0_177

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

## Progress Made to the Machine Learning Model as of 3/6
- Completed changes to primary data preprocessing and renamed file salmon_preprocessing_ws
   - Dropped "Unamed: 0", "Start Year", "End Year" and "Effective Catch" since they have no impact on our more focused feature approach
   - Found additional duplicate data that was not dropped due to variance in the "Start Year" and "End Year" Columns despite all the remaining data being duplicate values. 
   - Dropped all values from our variables that were below 0 (There were a lot of '-99' values instead of 'NaN'
   - Multiplied the "Number of Spawners" by "Fracwild" to create Wild Spawners, which will be our target for the model. 
   - Created arrays to hold our Previous Year, Two Years Prior, and Three Years Prior Wild Spawners data
   - Added arrays in a staggered fashion to the dataframe 
   - Renamed columns to remove spaces
   - Created salmon_preprocessed_ws.csv
   - Set up our connection with Postgres on our AWS server
- Completed secondary data preprocessing in salmon_ml_model (feature selection)
   - Set up our dependencies
   - Connected our Postgres database and loaded tabled data into notebook
   - Isolated target stream
   - Deleted first three lines since it holds the incorrect data for this targetted stream.
- Completed determining target and the features   
   - Created variables to hold our features and our target 
   - Our biggest change to our model was determining that our features should just be the Wild Spawners data from the three previous years.  
   - Our features are: 'Brood_Year', 'Wild_Spawners_Prev_Yr', 'Wild_Spawners_Two_Yrs_Prior' and 'Wild_Spawners_Two_Yrs_Prior'
- Split our testing and training sets
   - We adjusted our training rations to 80/20
- Initiated a Multiple Linear Regression Model
   - We chose this model because it seemed ideal for our continuos data type of our target
   - We tried using different models such as the ridge model but our data was not diverse enough for it to be effective.
   - We ultimately decided to change our features and target to create a better performing model.
- Accuracy and Performance
   - Our model's performance is not ideal but we have achieved an r-squared value of .64 and a mean squared error of 673.
   - We will continue to adjust our model or train different streams to achieve a higher score.
   - Our data has been hard to predict due to the nature of salmon spawning. Salmon could return to spawn in as soon as two years or up to 5-6 years which makes the predictability difficult.     	

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
