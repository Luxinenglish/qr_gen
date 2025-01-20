import os
import qrcode
from PIL import Image
from flask import Flask, render_template, request, send_from_directory, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = "qrcodes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def create_qrcode(link, image_path=None, output_dir=UPLOAD_FOLDER):
    os.makedirs(output_dir, exist_ok=True)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")
    
    if image_path and os.path.exists(image_path):
        overlay = Image.open(image_path)
        overlay = overlay.resize((50, 50))
        qr_width, qr_height = qr_img.size
        pos = ((qr_width - overlay.width) // 2, (qr_height - overlay.height) // 2)
        qr_img.paste(overlay, pos, overlay if overlay.mode == "RGBA" else None)
    
    filename = f"qr_{len(os.listdir(output_dir)) + 1}.png"
    filepath = os.path.join(output_dir, filename)
    qr_img.save(filepath)
    
    with open(os.path.join(output_dir, "links.txt"), "a") as f:
        f.write(f"{filename},{link}\n")
    
    return filename

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_qr():
    link = request.form.get("link")
    image = request.files.get("image")

    if not link:
        return "Erreur : Aucun lien fourni", 400

    image_path = None
    if image:
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)
    
    filename = create_qrcode(link, image_path)
    return f"/qrcodes/{filename}"

@app.route("/qrcodes/<filename>")
def serve_qr(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/list")
def list_qr():
    qr_list = []
    links_file = os.path.join(UPLOAD_FOLDER, "links.txt")
    
    if os.path.exists(links_file):
        with open(links_file, "r") as f:
            for line in f:
                filename, link = line.strip().split(",")
                qr_list.append({"image": f"/qrcodes/{filename}", "link": link})

    return jsonify(qr_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
