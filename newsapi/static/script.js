// Load news from FastAPI backend
async function loadNews() {

    const response = await fetch("/news");
    const data = await response.json();

    const list = document.getElementById("newsList");
    list.innerHTML = "";

    data.articles.forEach(article => {

        const li = document.createElement("li");

        li.innerHTML = `
            <div class="bg-white p-3 shadow rounded">
                <h3 class="font-semibold">${article.title}</h3>
                <p class="text-sm text-gray-600">${article.source}</p>
                <a href="${article.url}" target="_blank"
                class="text-blue-500">Read More</a>
            </div>
        `;

        list.appendChild(li);
    });
}