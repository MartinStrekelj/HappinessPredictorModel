import mindsdb
from mindsdb import Predictor

Predictor(name='Happiness_predictor_py').learn(
    from_data="./cleansed_data/tup_seminarska_happiness_schema_happiness.csv",
    to_predict='happiness_score',
)

mdb = mindsdb.Predictor(name='Happiness_predictor_py')

#enaki vnosni podatki kot v porocilu
result = Predictor(name='Happiness_predictor_py').predict(when_data={'country': "Slovenia",
                                                                     'year': 2021,
                                                                     'health': 0.2,
                                                                     'generosity': 0.6,
                                                                     'government_trust': 0.2,
                                                                     'freedom': 0.2,
                                                                     'region': "Western Europe",
                                                                     'economy': 0.4,
                                                                     'family': 0.8})

# result = Predictor(name='Happiness_predictor_py').predict(when_data={'country': "Slovenia",
#                                                                      'year': 2021})

print('The predicted happiness score is between {happiness_score} with {conf} confidence'.
      format(happiness_score=result[0].explanation['happiness_score']['confidence_interval'],
             conf=result[0].explanation['happiness_score']['confidence']))

