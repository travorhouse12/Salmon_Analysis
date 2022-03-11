# Salmon_Analysis

## Dashboard

Click below to check out our Salmon Anlaysis final presentation!

[Click Me to Go To Our Google Slides Presentation](https://docs.google.com/presentation/d/1_tHgs23qMZGwq0RtyLZu3yQ7rGeU5Wllu7NAGIvpXs4/edit#slide=id.g118c62022ce_0_177)

Click below to get a hold of our final Tableau Dashboard where you are able to filter by brood year on select pages and use the interactive "Click Me to Move On!" to keep you on the right path!

[DASHBOARD LINK. CLICK ME](https://public.tableau.com/views/Salmon_Analysis_Dashboard/Story9?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
If you see the snapshot below when you click the Dashboard link, then congrats you made it there properly!

<img width="1285" alt="Screen Shot 2022-03-10 at 8 29 38 PM" src="https://user-images.githubusercontent.com/91299616/157802428-c814991d-7537-455b-b71c-9401e7ab52fb.png">

KEY INFORMATION WITH TABLEAU

• We connected our Tableau Desktop with postgres inorder to retrevie the ML model tables. In order to publish this Tableau story/dashboard I needed to extract from the live server to then use Tableau public just for the display of the story/dashboard.

• There are interactive buttons at the top of each story to get you to the next visualization.

• Interactive sliders to filter the brood year on a few of the charts to give you a smaller chart to analyze.

## Outline of the Project

The purpose of this project was to aid salmon hatcheries in identifying the future need of hatchery raised salmon by providing predictive population numbers of wild salmon. To do this, we will find a data set that has the salmon data we will need. We will perform some exploratory analysis. Then, we upload the data to a Postgres database. We leveraged an AWS RDS server for our Postgres database to make it publicly accesible.

Then, we cleaned the data using a mixture of SQL and Pandas until we got the data to a state that was usable, while dropping unnecesary columns.

Next, we built our machine learning model that helped us predict salmon population for 2012 in the Imnaha river. Finally, we connected our Tableau to interact and pull data from our Postgres to analyze the salmon data as well as teh predicted salmon data to create visualizations.

### ROLES
**Square:** Travor – His job is to manage the repository and make sure everything is up to date, and clean for our project.

**Triangle:** Matt – Will be working on creating a mockup of a machine learning model.

**Circle:** Adam – His job is to create a mockup of a database with a set of sample data. Mainly, so that we can ensure our database

**X:** Nora – This member will oversee which technologies to use for each step of the project.

We have decided on these roles for one another but are not limited to role in any way. We will all be working through each role and helping one another with ideas and feedback which is important for the project to run smoothly!

## Progress Made to the Machine Learning Model as of 3/8
### Completed changes to primary data preprocessing and renamed file salmon_preprocessing_ws
   - Dropped "Unamed: 0", "Start Year", "End Year" and "Effective Catch" since they have no impact on our more focused feature approach
   - Found additional duplicate data that was not dropped due to variance in the "Start Year" and "End Year" Columns despite all the remaining data being duplicate values. 
   - Dropped all values from our variables that were below 0 (There were a lot of '-99' values instead of 'NaN'
   - Multiplied the "Number of Spawners" by "Fracwild" to create Wild Spawners, which will be our target for the model. 
   - Created arrays to hold our Previous Year, Two Years Prior, and Three Years Prior Wild Spawners data
   - Added arrays in a staggered fashion to the dataframe 
   - Renamed columns to remove spaces
   - Created salmon_preprocessed_ws.csv
   - Set up our connection with Postgres on our AWS server
### Completed secondary data preprocessing in salmon_ml_model (feature selection)
   - Set up our dependencies
   - Connected our Postgres database and loaded tabled data into notebook
   - Isolated target stream
   - Deleted first three lines since it holds the incorrect data for this targetted stream.
### Completed determining target and the features   
   - Created variables to hold our features and our target 
   - Our biggest change to our model was determining that our features should just be the Wild Spawners data from the three previous years.  
   - Our features are: 'Wild_Spawners_Prev_Yr', 'Wild_Spawners_Two_Yrs_Prior' and 'Wild_Spawners_Two_Yrs_Prior'
### Split our testing and training sets
   - We adjusted our training rations to 80/20
### Initiated a Multiple Linear Regression Model
   - We chose this model because it seemed ideal for our continuos data type of our target
   - We tried using different models such as the ridge model but our data was not diverse enough for it to be effective.
   - We ultimately decided to change our features and target to create a better performing model.
### Accuracy and Performance
   - Our model's performance is not ideal but we have achieved an r-squared value of .61 and a mean squared error of 673.
   - We will continue to adjust our model or train different streams to achieve a higher score.
   - Our data has been hard to predict due to the nature of salmon spawning. Salmon could return to spawn in as soon as two years or up to 5-6 years which makes the predictability difficult.     	

## Database Mockup
Database being leveraged:

- PostegreSQL
- AWS RDS

Selected Topic: 

Population Change in Chinook Salmon in the Imnaha River.

Reason Why We Selected This Data:

We chose this topic because the population of Chinook Salmon are very local to the Pacific Northwest. It is very important to understand what is going on within the local watersheds to help prevent disaster. This project will help us really understand what has happened over so many years with the spawning and reproduction of this species, and what may have caused an increase or a decrease in this population!


Description Of The Data Source: 

Our data source is coming from NOAA.Gov. This link will bring you directly to the data source. This dataset has more than 30 + columns and 60,000+ rows so there is plenty of data to work with. We will not need all of this data for the main portion of the project but may need to go back and use it for a comparison later on. You can see where we filtered this very large dataset to contain only the chinook salmon populations in the Filter_Fish_Data.ipynb. 

Link to our data source:

https://www.webapps.nwfsc.noaa.gov/apex/parrdata/inventory/tables/table/population_data_and_references_for_the_salmon_population_summary_sps_database 

Questions We Are Looking To Answer: 

Can salmon populations be predicted? Are salmon populations stable? Is the work being done to restore salmon habitat currently effective?
