# django_web

djangoによるWebページ

## 展開方法

```bash
git clone -b devlop https://github.com/naritomo08/django_docker
cd django_docker
cp .env.example .env
git clone git@github.com:naritomo08/django_web.git src
docker-compose build
docker-compose up -d

以下のサイトを参照
http://localhost:8000/
```

## 各種ブランチ

* master 初期状態
* devlop 開発サイト
* helloapp helloサイト作成(/hello/)
* helloapp2 helloサイト作成2(/hello/)
* dbmigrate mysqlへのmigrate設定

```bash
以下のコマンドを入力する。
docker-compose exec django /bin/bash
python3 manage.py makemigrations hello
python3 manage.py migrate
```

