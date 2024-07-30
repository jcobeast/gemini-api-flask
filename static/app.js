async function generate() {
	const question = $("#question").val().trim();
	if (!question) {
		$("#errorMessage").show();
		return;
	}

	$("#errorMessage").hide();
	$("#loading").show();

	try {
		const response = await fetch("/generate", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ question }),
		});

		const data = await response.json();

		$("#loading").hide();
		if (response.ok) {
			$("#responseContent").html(data.response);
		} else {
			$("#responseContent").html(
				"<p>An error occurred. Please try again.</p>"
			);
		}
		$("#responseContainer").show();
	} catch (error) {
		$("#loading").hide();
		$("#responseContent").html(
			"<p>An error occurred. Please try again.</p>"
		);
		$("#responseContainer").show();
	}
}
