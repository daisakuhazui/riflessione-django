Riflessioneサービスのリポジトリ

=================================

開発環境の構築手順、また開発時に必要となる各種手順について記載する。

## 開発環境構築

- Mac OSXによる開発を前提とする
- Docker for Macをインストールする
- リポジトリをクローンする

```bach
git clone git@github.com/daisakuhazui/introspective-question-genarator.git
cd introspective-question-genarator
```

## .envファイル設定

`env.sample` ファイルをコピーして `.env` を作成。
`.env` にAWSアクセスキーなど必要な情報を入力する

```bash
cp env.sample .env
```

## Dockerコンテナをビルド、データのインポート
```bash
make build
```

でDockerコンテナのビルドを行い、

```bash
make migrate
```

## 各種コマンド

### Dockerコンテナのビルド

```bash
make build
```

### Dockerコンテナの起動

```bash
make up
```

### テストの実行

```bash
make test
```

### Docker appコンテナ内で作業

```bash
make run
```

### Docker コンテナ停止

```bash
make stop
```

### Djangoマイグレーション

```bash
make migrate
```
