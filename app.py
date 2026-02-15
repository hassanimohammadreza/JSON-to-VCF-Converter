import json
import os
import zipfile
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if not file:
        return "No file uploaded"

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        contacts = json.load(f)

    vcf_folder = os.path.join(OUTPUT_FOLDER, "vcf_files")
    os.makedirs(vcf_folder, exist_ok=True)

    for contact in contacts:
        name = contact["name"]
        number = contact["phone"]

        safe_name = name.replace("/", "-").replace("\\", "-")
        vcf_path = os.path.join(vcf_folder, f"{safe_name}.vcf")

        vcard = f"""BEGIN:VCARD
VERSION:2.1
N:{name}
FN:{name}
TEL;CELL:{number}
END:VCARD
"""

        with open(vcf_path, "w", encoding="utf-8") as vcf_file:
            vcf_file.write(vcard)

    zip_path = os.path.join(OUTPUT_FOLDER, "contacts.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in os.listdir(vcf_folder):
            zipf.write(os.path.join(vcf_folder, file), file)

    return send_file(zip_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
