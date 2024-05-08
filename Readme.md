# django_web

djangoによるWebページ

## 展開方法

```bash
git clone -b djangosite https://github.com/naritomo08/django_docker
cd django_docker
cp .env.example .env
git clone -b <指定のブランチ> https://github.com/naritomo08/django_web src
docker-compose build
docker-compose up -d
```

## 各種ブランチ

* main 最新ブランチ

```bash
展開後以下の作業を行うこと。

cp src/.env.example src/.env

.env内のSECRET_KEYを以下の方法で入手する。

docker-compose exec django /bin/bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
→出てきた値を.env内のsecret_keyに設定すること。

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

* bbscreate 投稿作成ページ

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
→新規投稿部分のボタンをクリックして新規投稿できること。
```

* bbsupdate 投稿更新ページ

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
→投稿詳細画面から投稿を更新できること。
```

* bbsdelete 投稿削除ページ

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
→投稿詳細画面から投稿を削除できること。
```

* bbsbootstrap bootstrap適用

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
→様々な大きさに変更しレスポンシブになっていること。
```

* django_secret djamgoセキュア化

```bash
cp src/.env.example src/.env

.env内のSECRET_KEYを以下の方法で入手する。

docker-compose exec django /bin/bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
→出てきた値を.env内のsecret_keyに設定すること。

docker-compose down
docker-compose up -d
```

* bbssearch

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
→投稿検索できること。
```

* bbsencrypt

```bash
http://localhost:8000/
→投稿インデックスページ参照できること。
→ユーザー登録、投稿できること。
```
