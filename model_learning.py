from mindsdb import Predictor

Predictor(name='Happiness_predictor_py').learn(
    from_data="./cleansed_data/tup_seminarska_happiness_schema_happiness.csv",
    to_predict='happiness_score',
)

mdb = mindsdb.Predictor(name='Happiness_predictor_py')

result = Predictor(name='Happiness_predictor_py').predict(when_data={'economy': 0.5, 'health': 0.5, 'government_trust': 0.5})

print('The predicted price is between ${happiness_score} with {conf} confidence'.format(price=result[0].explanation['happiness_score']['confidence_interval'], conf=result[0].explanation['happiness_score']['confidence']))

## not working :(