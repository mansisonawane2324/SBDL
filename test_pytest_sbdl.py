import pytest
from lib.Utils import get_spark_session

@pytest.fixture(scope='session')
def spark():
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    spark_session.stop()

def test_blank_test(spark):
    print("Spark Version:", spark.version)
    assert spark.version.startswith("4.")  # Passes for 4.x versions
