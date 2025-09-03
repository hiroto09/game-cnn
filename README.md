# 🎮 Game Classifier (CNN)

## 概要
キャプチャしたゲーム画面を CNN で分類するシステム。  
現在は **スマブラ** と **人生ゲーム** の2種類に対応。

## ディレクトリ構成
- `dataset/` : ゲームごとの画像データ（クラスごとにフォルダ分け）
- `src/train.py` : 学習スクリプト
- `src/predict.py` : 推論スクリプト
- `saved_model/` : 保存済みモデル

## 使い方
```bash

pip install -r requirements.txt

# 学習
python src/train.py

# 推論
python src/main.py
