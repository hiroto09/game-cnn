APP_NAME=cnn-app
PORT=8000

# Docker イメージをビルド
build:
	docker build -t $(APP_NAME) .

# コンテナを起動 (-d バックグラウンド)
run:
	docker run -d -p $(PORT):8000 --name $(APP_NAME) $(APP_NAME)

# ログを確認
logs:
	docker logs -f $(APP_NAME)

# コンテナに入る
exec:
	docker exec -it $(APP_NAME) /bin/bash

# コンテナを停止して削除
stop:
	docker stop $(APP_NAME) || true
	docker rm $(APP_NAME) || true

# 再起動 (ビルド → 停止 → 起動)
restart: build stop run
