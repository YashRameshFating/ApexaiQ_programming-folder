async function getQuote() {

    const response = await fetch("/quote");

    const data = await response.json();

    const box = document.getElementById("quoteBox");

    box.innerHTML = "";

    if (data.data) {

        box.innerHTML = `
        <div class="border p-4">
            <p class="italic">"${data.data.text}"</p>
            <p class="mt-2 font-bold">- ${data.data.author}</p>
        </div>
        `;

    } else {

        box.innerHTML = "<p class='text-red-500'>Could not fetch quote</p>";

    }
}