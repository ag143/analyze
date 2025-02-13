from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

NSE_API_URL = "https://www.nseindia.com/api/quote-equity"

@app.route("/get_stock_data", methods=["GET"])
def get_stock_data():
    symbol = request.args.get("symbol", "RELIANCE")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(f"{NSE_API_URL}?symbol={symbol}", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "price": data["priceInfo"]["lastPrice"],
            "market_cap": data["marketDeptOrderBook"]["totalBuyQuantity"],
            "pe_ratio": data["priceInfo"].get("pE"),
            "book_value": data["metadata"].get("bookValue"),
        })
    return jsonify({"error": "Stock data not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
