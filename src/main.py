from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# FastAPI アプリ作成
app = FastAPI()

# モデルとクラス名をロード
model = load_model("../saved_model/game_classifier.h5")
class_names = ["人生ゲーム", "スマブラ"]  # dataset のフォルダ名に合わせる

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    print(f"ファイルだよーーーーー！: {file.filename}")
    # 画像をバイトデータとして読み込み
    contents = await file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # 前処理（128x128, 正規化）
    img_resized = cv2.resize(img, (128, 128))
    img_norm = img_resized / 255.0
    img_input = np.expand_dims(img_norm, axis=0)  # (1, 128,128,3)

    # CNN 推論
    pred = model.predict(img_input)
    class_id = int(np.argmax(pred))
    confidence = float(np.max(pred))

    result = {
        "predicted_class": class_names[class_id],
        "confidence": confidence
    }
    return JSONResponse(content=result)

# サーバー起動方法:
# uvicorn main:app --reload
