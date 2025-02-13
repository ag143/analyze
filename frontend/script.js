async function fetchStockData() {
    let symbol = document.getElementById("stockSymbol").value.toUpperCase();
    let response = await fetch(`https://your-api.onrender.com/get_stock_data?symbol=${symbol}`);
    let data = await response.json();

    document.getElementById("price").innerText = `Stock Price: ₹${data.price}`;
    document.getElementById("fundamentals").innerHTML = `
        <p>Market Cap: ${data.market_cap}</p>
        <p>PE Ratio: ${data.pe_ratio}</p>
        <p>Book Value: ${data.book_value}</p>
    `;
}
