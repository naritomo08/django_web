# django_web

djangoによるWebページ

## 展開方法

```bash
git clone -b devlop https://github.com/naritomo08/django_docker
cd django_docker
cp .env.example .env
git clone -b <指定のブランチ> https://github.com/naritomo08/django_web src
docker-compose build
docker-compose up -d

以下のサイトを参照
http://localhost:8000/
```

## 各種ブランチ

* main 最新ブランチ

```bash
以下のサイトを参照できること。
http://localhost:8000/admin/
管理者ログインサイト
http://localhost:8000/hello/
helloサイト
http://localhost:8000/
BBSサイト
```

* initialize 初期状態
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

* dbshow db参照サイト

```bash
以下のコマンドを入力する。
docker-compose exec django /bin/bash
python3 manage.py createsuperuser
スーパーユーザ、メールアドレス、パスワードを設定

以下のサイトに入り、Articleテーブルにデータを追加する。
http://localhost:8000/admin/
```

* classbase クラスベースの汎用ビューへの変更サイト
* bbsbase つぶやきサイト作成base

```bash
以下のコマンドを入力する。
docker-compose exec django /bin/bash
python3 manage.py makemigrations bbs
python3 manage.py migrate
```

* bbsindex 投稿インデックスページ

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
```

* bbsdetail 投稿詳細ページ

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
→投稿部分のリンクをクリックして要項詳細を参照できること。
```
