#!/usr/bin/env python3
"""Génère le QR code du Protocole Élu (PNG pour l'écran, SVG pour l'impression).

Usage : python3 generer_qr.py https://ton-adresse.netlify.app
Nécessite : pip install segno
"""
import sys
import segno

if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
    sys.exit("Usage : python3 generer_qr.py https://adresse-de-la-page")

url = sys.argv[1]
# Correction d'erreur élevée (H) : le QR reste lisible même un peu abîmé ou
# déformé par les plis du T-shirt.
qr = segno.make(url, error="h")
qr.save("qr-protocole-elu.png", scale=20, border=4, dark="black", light="white")
qr.save("qr-protocole-elu.svg", scale=20, border=4, dark="black", light="white")
print("OK : qr-protocole-elu.png et qr-protocole-elu.svg créés pour", url)
