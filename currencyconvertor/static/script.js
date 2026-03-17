const API = "http://127.0.0.1:8000";


async function convertCurrency() {

    const amount = document.getElementById("amount").value;
    const from = document.getElementById("from").value;
    const to = document.getElementById("to").value;

    const response = await fetch(`${API}/convert`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            from_currency: from,
            to_currency: to,
            amount: parseFloat(amount)
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        "Converted Amount: " + data.converted_amount;
}