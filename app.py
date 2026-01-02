from flask import Flask, render_template
import os

app = Flask(__name__)

# =========================
# CONFIGURACIÓN TRANSAK
# =========================
TRANSAK_API_KEY = os.getenv(
    "TRANSAK_API_KEY",
    "cd9a1ba5-0d99-4d95-8b5b-a1ca303d3b3b"
)

WALLET_ADDRESS = os.getenv(
    "WALLET_ADDRESS",
    "0x42fdb87a036e0ac3bff63a2f7a81571fd3a80c84"
)

@app.route("/")
def home():
    return render_template(
        "transak.html",
        transak_api_key=TRANSAK_API_KEY,
        wallet_address=WALLET_ADDRESS
    )

if __name__ == "__main__":
    app.run(debug=True)