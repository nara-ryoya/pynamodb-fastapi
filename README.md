# FastAPI + DynamoDBのローカル開発環境

## このレポジトリについて

DynamoDBのPython APIであるPynamoDBを用いて、Dockerで簡単にFastAPI + DynamoDBのローカル開発環境を行える。このレポジトリはその一例として、本の購入履歴を管理するアプリケーションを実装している。

[wip] フロントエンドの実装

## 使い方

### アプリケーションの立ち上げ

```
docker compose build # ビルド
docker compose up -d # アプリ立ち上げ
```

### テーブルにランダムな値を入れて初期化する

```
docker compose backend exec python db/create_db.py # テーブルの初期化
docker compose backend exec python db/insert_random_record.py # テーブルにランダムな値を入れる
```

### DBテーブルの確認

[http://localhost:8001](http://localhost:8001)をブラウザで開くことで、テーブルを確認することができる。


### エンドポイントの確認

[http://localhost:8000/docs](http://localhost:8000/docs)から、各エンドポイントの動作確認をすることができる。


## AWS本番環境で使うには

`backend/.aws`以下に正しい設定をするか、適切にコンテナにマウントの設定をすることで、AWS本番環境のDynamoDBに対するテーブルの作成・レコードの挿入・CRUD操作ができる。

## CI

mainブランチに対するPRに対して、frontend, backendでそれぞれgithub actionsによってCIを実行している。