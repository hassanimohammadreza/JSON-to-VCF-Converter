function showFileName(input) {
    const fileName = input.files[0]?.name;
    document.getElementById("fileName").textContent = fileName ? "Selected: " + fileName : "";
}
