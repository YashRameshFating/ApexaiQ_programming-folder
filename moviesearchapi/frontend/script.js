async function searchMovie(){

const title = document.getElementById("title").value
const year = document.getElementById("year").value
const page = document.getElementById("page").value || 1

const response = await fetch("http://127.0.0.1:8000/movies",{
method:"POST",
headers:{"Content-Type":"application/json"},
body: JSON.stringify({
title:title,
year: year ? Number(year) : null,
page:Number(page)
})
})

const data = await response.json()

let html = ""

if(data.movies){

data.movies.forEach(movie =>{

const poster = movie.Poster !== "N/A"
? movie.Poster
: "https://via.placeholder.com/300x450?text=No+Image"

html += `
<div class="bg-white rounded shadow hover:shadow-lg transition">

<img src="${poster}" class="w-full h-72 object-cover rounded-t">

<div class="p-3">
<h2 class="font-semibold text-lg">${movie.Title}</h2>
<p class="text-gray-500">${movie.Year}</p>
</div>

</div>
`

})

}else{
html = "<p class='text-red-500'>No movies found</p>"
}

document.getElementById("results").innerHTML = html
}