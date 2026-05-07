import pandas as pd
from sqlalchemy.orm import Session
from database import engine, Base
from models import Exchanger


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
    print("База данных успешно инициализирована")


if __name__ == "__main__":
    init_database()