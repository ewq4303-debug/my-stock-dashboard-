import requests
import pandas as pd
import os
import json
from datetime import datetime

def scrape():
    # 這裡以台積電 (2330) 為範例
    stock_id = "2330"
    print(f"正在抓取 {stock_id} 的籌碼資料...")
    
    # 範例：抓取三大法人資料 (這裡先用一個模擬數據確保流程正確)
    # 實務上你會在這裡放之前的 requests 邏輯
    result = {
        "stock_id": stock_id,
        "name": "台積電",
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "it_buy": 1250, # 假設投信買超張數
        "major_ratio": 75.4, # 假設大戶持股比例
        "chip_score": 1 # 評分
    }

    # 確保資料夾存在
    os.makedirs('public/data', exist_ok=True)
    
    # 存成 JSON 檔
    file_path = 'public/data/latest_chips.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    
    print(f"資料已成功存入 {file_path}")

if __name__ == "__main__":
    scrape()
