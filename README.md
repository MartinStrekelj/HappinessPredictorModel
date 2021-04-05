# HappinessPredictorModel
Predicting happiness with MindsDB

MindsDB, python3, PostgreSQL

## Getting started

run `ddl.sql` in ./sql/ to create table in PostgreSQL

Make sure you install all pip modules.

run `python3 input_reader.py`
run `python3 data_correction.sql`

Alternatively or just use ./cleansed_data/tup_seminarska_happiness_schema_happiness.csv

Run `MindsDB scout`

Import data from PostgreSQL to MindsDB or ./cleansed_data/tup_seminarska_happiness_schema_happiness.csv

Create model / Predictor

Run prediction query 
