-- Create table for Salmon Analysis
CREATE TABLE filtered_salmon_data (
	Nwr_Population_Name VARCHAR(40) NOT NULL,
	Stream_Name VARCHAR(40) NOT NULL,
	Brood_Year INT NOT NULL,
	Start_Year INT NOT NULL,
	End_Year INT NOT NULL,
	Number_of_Spawners INT NOT NULL
);
