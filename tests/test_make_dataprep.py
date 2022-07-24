# %%
import pandas as pd
import pytest

from src.data.make_dataprep import verify_data_type


@pytest.mark.parametrize(
    'data_type, expected', [
        ('discrete', 'discrete'),
        ('continuous', 'continuous')
    ]
)
def test_verify_data_type(data_type, expected):
    df = pd.DataFrame([['a', 1.25], ['b', 1.87], ['c', 3.87]], columns=['discrete', 'continuous'])
    result = verify_data_type(df=df, feature=data_type)
    assert expected == result


def test_load_dataprep_model():
    # load_dataprep_model(model_path='model')
    pass


def test_prepare_data():
    # prepare_data(input_data='df', model='model')
    pass
