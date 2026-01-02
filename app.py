from flask import Flask, render_template
import os

app = Flask(__name__)

# =========================
# CONFIGURACIÓN TRANSAK
# =========================
TRANSAK_API_KEY = os.getenv(
    "TRANSAK_API_KEY",
    "STAGING_API_KEY_AQUI"  # <-- reemplaza por tu API Key de STAGING
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