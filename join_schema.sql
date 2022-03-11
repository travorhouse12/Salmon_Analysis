SELECT
	"Brood_Year",
	"Nwr_Population_Name",
	"Wild_Spawners",
	"Predicted_Wild_Spawners",
	"wen_year",
	"wen",
	"wen_wild",
	"wen_pred"
FROM
	wenatchee_predict_prod
INNER JOIN salmon_predict_prod ON "Brood_Year" = "wen_year";

