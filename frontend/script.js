const API_URL = "http://127.0.0.1:8000/recommend";


async function getRecommendation(){


    const data = {

        age: Number(document.getElementById("age").value),

        gender: document.getElementById("gender").value,

        weight: Number(document.getElementById("weight").value),

        height: Number(document.getElementById("height").value),

        goal: document.getElementById("goal").value,

        diet: "normal",

        preference: document.getElementById("preference").value


    };


    console.log("Data dikirim:", data);



    try {


        const response = await fetch(API_URL, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });



        const result = await response.json();


        console.log("Response API:", result);



        if(result.recommendation){

            displayResult(result.recommendation);

        } else {

            document.getElementById("result").innerHTML =
            "Tidak ada rekomendasi";

        }



    } catch(error){


        console.error(error);


        document.getElementById("result").innerHTML =
        "❌ Tidak bisa terhubung ke NutriAI API";


    }


}





function displayResult(data){


    document.getElementById("result").innerHTML = `


        <h1>${data.food}</h1>



        <h3>🥗 Nutrisi</h3>


        <div class="tags">

            ${
                data.nutrition.map(item => 
                `<span>${item}</span>`
                ).join("")
            }

        </div>



        <h3>💪 Manfaat</h3>


        <ul>

            ${
                data.benefit.map(item =>
                `<li>${item}</li>`
                ).join("")
            }

        </ul>


    `;


}