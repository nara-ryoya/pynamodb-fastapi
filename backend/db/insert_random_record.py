from argparse import ArgumentParser
from datetime import datetime
from random import choice, randint

from dateutil.relativedelta import relativedelta

from api import models, schemas

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "record_num", default=10, type=int, help="number of random records to insert"
    )
    args = parser.parse_args()
    models.History.set_meta()
    for _ in range(args.record_num):
        record = models.History(
            **schemas.History(
                user_id=str(randint(0, 90000)).zfill(5),
                timestamp=datetime.now() + relativedelta(days=randint(-1000, 1000)),
                book=schemas.Book(
                    author=choice(
                        ["Ryunosuke Akutagawa", "Yasunari Kawabata", "Yukio Mishima"]
                    ),
                    category="novel",
                    title=choice(["Rashomon", "Yukiguni", "Kinkakuji"]),
                    thoughts="interesting, I like this book",
                    price=randint(1000, 2000),
                    link=None,
                ),
            ).dict()
        )
        record.save()
