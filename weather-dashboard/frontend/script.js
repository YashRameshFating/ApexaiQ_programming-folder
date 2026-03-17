async function getWeather(){

const city = document.getElementById("city").value

const response = await fetch("http://127.0.0.1:8000/weather",{
method:"POST",
headers:{"Content-Type":"application/json"},
body: JSON.stringify({city:city})
})

const data = await response.json()

let html = ""

const icon = `https://openweathermap.org/img/wn/${data.icon}@2x.png`

html += `
<div class="bg-white rounded shadow hover:shadow-lg transition p-6 text-center">

<h2 class="text-xl font-bold mb-2">${data.city}</h2>

<img src="${icon}" class="mx-auto">

<p class="text-3xl font-semibold">${data.temperature}°C</p>

<p class="text-gray-500 capitalize">${data.description}</p>

<p class="text-sm text-gray-400 mt-2">Source: ${data.source}</p>

</div>
`

document.getElementById("result").innerHTML = html
}