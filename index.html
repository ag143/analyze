async function fetchStockData() {
    let symbol = document.getElementById("stockSymbol").value.toUpperCase();
    let nseUrl = `https://www.nseindia.com/api/quote-equity?symbol=${symbol}`;
    
    // Using a CORS proxy
    let proxyUrl = `https://corsproxy.io/?` + encodeURIComponent(nseUrl);
    
    try {
        let response = await fetch(proxyUrl, {
            headers: {
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json",
                "Referer": "https://www.nseindia.com/"
            }
        });

        if (!response.ok) {
            throw new Error("Failed to fetch stock data.");
        }

        let data = await response.json();

        document.getElementById("price").innerText = `Stock Price: ₹${data.priceInfo.lastPrice}`;
        document.getElementById("fundamentals").innerHTML = `
            <p>Market Cap: ${data.marketDeptOrderBook.totalBuyQuantity}</p>
            <p>PE Ratio: ${data.priceInfo.pE || "N/A"}</p>
            <p>Book Value: ${data.metadata.bookValue || "N/A"}</p>
            <p>52-Week High: ${data.priceInfo.weekHigh52}</p>
            <p>52-Week Low: ${data.priceInfo.weekLow52}</p>
            <p>Day High: ${data.priceInfo.intraDayHighLow.max}</p>
            <p>Day Low: ${data.priceInfo.intraDayHighLow.min}</p>
        `;
    } catch (error) {
        console.error("Error fetching stock data:", error);
        document.getElementById("price").innerText = "Stock Price: Data not available";
    }
}
