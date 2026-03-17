async function searchHolidays() {

    const country = document.getElementById("country").value;
    const year = document.getElementById("year").value;

    const response = await fetch("/holidays", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            country_code: country,
            year: parseInt(year)
        })
    });

    const data = await response.json();

    const container = document.getElementById("results");
    container.innerHTML = "";

    data.holidays.forEach(h => {

        const div = document.createElement("div");

        div.className = "border p-2 mb-2";

        div.innerHTML = `
            <strong>${h.localName}</strong>
            <p>${h.date}</p>
        `;

        container.appendChild(div);

    });
}