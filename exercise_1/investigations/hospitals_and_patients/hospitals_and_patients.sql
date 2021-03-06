--Joining scores for hospital general comparison measures with survey ratings
DROP TABLE IF EXISTS hospital_ratings_survey_joined;
CREATE TABLE hospital_ratings_survey_joined AS
SELECT
	a.provider_id,
	a.hospital_rating,
	b.communication_with_nurses_performance_rate,
	b.communication_with_doctors_performance_rate,
	b.responsiveness_of_hospital_staff_performance_rate,
	b.pain_management_performance_rate,
	b.communication_about_medicines_performance_rate,
	b.cleanliness_and_quietness_of_hospital_environment_performance_rate,   
	b.discharge_information_performance_rate,
	b.overall_rating_of_hospital_performance_rate,
	b.total_performance_score,
	b.overall_rating_of_hospital_threshold_met
FROM hospital_general_ratings a
JOIN survey_response_data b
	ON a.provider_id = b.provider_id 
;

--finding correlations between hospital general comparison ratings with survey ratings
DROP TABLE IF EXISTS hospital_ratings_survey_correlations;
CREATE TABLE hospital_ratings_survey_correlations AS
SELECT
	CORR(hospital_rating,total_performance_score) AS hospital_rating_total_performance_score_corr,
	CORR(hospital_rating,overall_rating_of_hospital_threshold_met) AS hospital_rating_overall_rating_of_hospital_threshold_met_corr,
	CORR(hospital_rating,overall_rating_of_hospital_performance_rate) AS hospital_rating_overall_rating_of_hospital_performance_rate_corr,
	CORR(hospital_rating,communication_with_nurses_performance_rate) AS hospital_rating_communication_with_nurses_performance_rate_corr,
	CORR(hospital_rating,communication_with_doctors_performance_rate) AS hospital_rating_communication_with_doctors_performance_rate_corr,
	CORR(hospital_rating,responsiveness_of_hospital_staff_performance_rate) AS hospital_rating_responsiveness_of_hospital_staff_performance_rate_corr,
	CORR(hospital_rating,pain_management_performance_rate) AS hospital_rating_pain_management_performance_rate_corr,
	CORR(hospital_rating,communication_about_medicines_performance_rate) AS hospital_rating_communication_about_medicines_performance_rate_corr,
	CORR(hospital_rating,cleanliness_and_quietness_of_hospital_environment_performance_rate) AS hospital_rating_cleanliness_and_quietness_performance_rate_corr,
	CORR(hospital_rating,discharge_information_performance_rate) AS hospital_rating_discharge_information_performance_rate_corr
FROM hospital_ratings_survey_joined
;