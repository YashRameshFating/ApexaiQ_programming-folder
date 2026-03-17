async function getPrice() {

    const coin = document.getElementById("coin").value;

    if (!coin) {
        alert("Enter a cryptocurrency name");
        return;
    }

    const response = await fetch("/price", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            coin_id: coin
        })
    });

    const data = await response.json();

    const container = document.getElementById("result");

    container.innerHTML = "";

    if (data.data) {

        const price = data.data[coin].usd;

        container.innerHTML = `
        <div class="border p-3">
            <h2 class="font-bold">${coin.toUpperCase()}</h2>
            <p>Price: $${price}</p>
        </div>
        `;

    } else {

        container.innerHTML = `<p class="text-red-500">Error fetching price</p>`;

    }
}