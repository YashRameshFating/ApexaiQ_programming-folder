async function lookupIP() {

    const ip = document.getElementById("ip").value;

    if (!ip) {
        alert("Please enter an IP address");
        return;
    }

    const response = await fetch("/lookup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            ip: ip
        })
    });

    const data = await response.json();

    const container = document.getElementById("result");

    if (data.data) {

        const d = data.data;

        container.innerHTML = `
        <div class="border p-3">
            <p><strong>Country:</strong> ${d.country}</p>
            <p><strong>City:</strong> ${d.city}</p>
            <p><strong>Region:</strong> ${d.regionName}</p>
            <p><strong>ISP:</strong> ${d.isp}</p>
            <p><strong>Timezone:</strong> ${d.timezone}</p>
        </div>
        `;

    } else {

        container.innerHTML = "<p class='text-red-500'>Lookup failed</p>";

    }
}