from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# NSE API Headers to avoid blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/"
}

NSE_QUOTE_URL = "https://www.nseindia.com/api/quote-equity?symbol={}"

@app.route("/get_stock_data", methods=["GET"])
def get_stock_data():
    symbol = request.args.get("symbol", "RELIANCE")
    
    try:
        session = requests.Session()
        session.headers.update(HEADERS)
        
        # Get Stock Quote Data
        response = session.get(NSE_QUOTE_URL.format(symbol))
        
        if response.status_code == 200:
            data = response.json()
            
            stock_info = {
                "price": data["priceInfo"]["lastPrice"],
                "market_cap": data["marketDeptOrderBook"]["totalBuyQuantity"],
                "pe_ratio": data["priceInfo"].get("pE", "N/A"),
                "book_value": data["metadata"].get("bookValue", "N/A"),
                "high_52w": data["priceInfo"].get("weekHigh52", "N/A"),
                "low_52w": data["priceInfo"].get("weekLow52", "N/A"),
                "day_high": data["priceInfo"].get("intraDayHighLow", {}).get("max", "N/A"),
                "day_low": data["priceInfo"].get("intraDayHighLow", {}).get("min", "N/A")
            }
            return jsonify(stock_info)
    
        return jsonify({"error": "Stock data not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
