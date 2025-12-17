const API_URL = "http://127.0.0.1:8000/predict";

async function predict() {
    const input = document.getElementById("imageInput");
    const result = document.getElementById("result");
    const preview = document.getElementById("preview");

    if (!input.files.length) {
        alert("Please upload an image");
        return;
    }

    const file = input.files[0];

    // Show preview
    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";

    const formData = new FormData();
    formData.append("file", file);

    result.innerText = "⏳ Predicting...";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        result.innerText = `Prediction: ${data.prediction} (${data.confidence}%)`;
    } catch (error) {
        result.innerText = "❌ Error connecting to server";
    }
}
