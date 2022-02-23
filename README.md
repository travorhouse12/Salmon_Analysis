# Salmon_Analysis
## ROLES
### Square: Travor – His job is to manage the repository and make sure everything is up to date, and clean for our project.
### Triangle: Matt – Will be working on creating a mockup of a machine learning model.
### Circle: Adam – His job is to create a mockup of a database with a set of sample data. Mainly, so that we can ensure our database
### X: Nora – This member will oversee which technologies to use for each step of the project.

We have decided on these roles for one another but are not limited to role in any way. We will all be working through each role and helping one another with ideas and feedback which is important for the project to run smoothly!

##OVERVIEW

How many salmon do we need to spawn for streams X, X, and X to meet the benchmark?

The goal of this project is to find out how many Salmon that we will have to harvest for years to come. To find this number, we will take the average number of spawners for X amount of years for X, X, and X streams. This average will define the benchmark that each stream will need to meet each year.

We will then build a machine learning model to predict the number of salmon for the next year. We will also build a machine learning model to predict the fraction of wild salmon for the next year. Based on the predicted number of spawners, we will take the predicted fraction of wild salmon to determine the remaining number of fish we will need to spawn the following year.

If we notice any fluctuations in population, we will pull in other datasets to determine possible reasons why the salmon population might’ve dipped or risen in the specific time period.


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

## Machine Learning Model

Models to consider:

- Supervised vs Unsupervised
	- We will first train and test a supervised model on select groups determined by nwr population name
	- We will then run this model against non-tested groups determined by nwr population name
	- Finally we will run an unsupervised model to create clusters and then test these custers with our unsupervided model/
- Linear Regression models?
  - Scikit-Learn?  
- Variables
- Dependent: Number of spawners
- Independent: Brood year, start year, end year, nwr population name, stream name, fracwild, effective catch
### Progress
- Preprocessed data
- Added a draft of model


## Database Mockup
Database systems to use:

- Microsoft Excel
- Postgres/pgAdmin
- Amazon AWS
- Mongo


Selected Topic: 

Population Change in Chinook Salmon

Reason Why We Selected This Data:

We chose this topic because the population of Chinook Salmon are very local to the Pacific Northwest. It is very important to understand what is going on within the local watersheds to help prevent disaster. This project will help us really understand what has happened over so many years with the spawning and reproduction of this species, and what may have caused an increase or a decrease in this population!


Description Of The Data Source: 

Our data source is coming from NOAA.Gov. This link will bring you directly to the data source. This dataset has more than 30 + columns and 60,000+ rows so there is plenty of data to work with. We will not need all of this data for the main portion of the project but may need to go back and use it for a comparison later on. You can see where we filtered this very large dataset to contain only the chinook salmon populations in the Filter_Fish_Data.ipynb. 

Link to our data source https://www.webapps.nwfsc.noaa.gov/apex/parrdata/inventory/tables/table/population_data_and_references_for_the_salmon_population_summary_sps_database 

Questions We Are Looking To Answer: 

Can salmon populations be predicted? Are salmon populations stable? Is the work being done to restore salmon habitat currently effective?
