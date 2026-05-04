import json
import os
from datetime import datetime

def scrape():
    # 定義你的投資組合
    portfolio_ids = ["2330", "2454", "6669", "2317"]
    
    results = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "stocks": {}
    }

    for sid in portfolio_ids:
        # 這裡未來會接上真實的爬蟲函數
        # 目前先產出符合你需求的完整指標結構
        results["stocks"][sid] = {
            "stock_id": sid,
            "name": "台積電" if sid == "2330" else "聯發科" if sid == "2454" else "緯穎" if sid == "6669" else "鴻海",
            "price": 800, # 示意價
            # 三大法人
            "inst_foreign": 1500,  # 外資
            "inst_trust": 450,    # 投信
            "inst_dealer": -120,   # 自營商
            # 集保分布
            "major_holders": 75.8, # 大戶持股%
            "retail_holders": 12.4, # 散戶持股%
            # 分點進出 (前三名摘要)
            "top_brokers": "摩根大通(+500), 凱基台北(+300)",
            # 融資券
            "margin_buy": 200,    # 融資增減
            "short_sell": -50,    # 融券增減
            # 借券
            "sbl_balance": 12000, # 借券賣出餘額
            "sbl_change": 150,    # 借券當日變動
            "chip_score": 2       # 綜合評分
        }

    os.makedirs('public/data', exist_ok=True)
    with open('public/data/latest_chips.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print("多支個股完整籌碼數據已更新")

if __name__ == "__main__":
    scrape()
