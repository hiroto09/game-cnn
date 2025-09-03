FROM python:3.10-slim

# 作業ディレクトリ作成
WORKDIR /app

# 必要パッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコードをコピー
COPY . .

# FastAPI を起動する (外部アクセス可能にする)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
