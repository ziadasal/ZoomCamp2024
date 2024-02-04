if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


@transformer
def transform(data, *args, **kwargs):
    data.lpep_pickup_date = pd.to_datetime(data.lpep_pickup_datetime)
    data.lpep_pickup_date = pd.to_datetime(data.lpep_dropoff_datetime)
    data.drop(['lpep_pickup_datetime','lpep_dropoff_datetime'],axis='columns',inplace=True)
    return(data)

