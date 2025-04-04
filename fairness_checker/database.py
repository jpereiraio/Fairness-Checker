import pandas as pd
from sqlalchemy import create_engine

class Database:
    def __init__(self, config):
        self.engine = create_engine(
            f"postgresql://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
        )

    def load_customer_data(self, customer):
        return pd.read_sql_table(customer, con=self.engine)
