import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sqlalchemy.orm import Session

from database import engine
from models import Base, Exchanger


def init_database():
    Base.metadata.create_all(bind=engine)

    df = pd.read_csv("data/bestchange_top.csv")

    with Session(engine) as session:
        session.query(Exchanger).delete()

        for _, row in df.iterrows():
            exchanger = Exchanger(
                name=row['name'],
                rate=float(row['rate']),
                reserve=float(row['reserve']),
                reviews=int(row['reviews']),
                min_btc=float(row['min_btc']),
                max_btc=float(row['max_btc'])
            )
            session.add(exchanger)

        session.commit()

    print(f"База данных успешно инициализирована. Загружено {len(df)} записей.")


if __name__ == "__main__":
    init_database()