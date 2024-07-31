async function generate() {
	const question = document.getElementById("question").value;
	const errorMessage = document.getElementById("errorMessage");
	const loading = document.getElementById("loading");
	const responseContainer = document.getElementById("responseContainer");
	const responseContent = document.getElementById("responseContent");

	if (!question) {
		errorMessage.style.display = "block";
		return;
	} else {
		errorMessage.style.display = "none";
	}

	loading.style.display = "block";

	try {
		const response = await fetch("/generate", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ question }),
		});

		const result = await response.json();

		if (response.ok) {
			responseContent.innerHTML = result.response;
			responseContainer.style.display = "block";
		} else {
			responseContent.innerHTML = `<p style="color: red">${result.error}</p>`;
			responseContainer.style.display = "block";
		}
	} catch (error) {
		responseContent.innerHTML = `<p style="color: red">Error: ${error.message}</p>`;
		responseContainer.style.display = "block";
	} finally {
		loading.style.display = "none";
	}
}
