
from datetime import datetime
from zoneinfo import ZoneInfo
import random

# Fecha y hora del lanzamiento (provisional)
LANZAMIENTO = datetime(2026, 11, 5, 0, 0, tzinfo=ZoneInfo("Europe/Madrid"))

FRASES = [
    "⚔️ ¡Afilad vuestras armas, aventureros!",
    "🐉 ¡Azeroth nos espera!",
    "🔥 ¡Por la Horda! ¡Por la Alianza!",
    "🛡️ ¡La batalla está cada vez más cerca!",
    "✨ ¡Pronto volveremos a vivir una aventura legendaria!"
]

ahora = datetime.now(ZoneInfo("Europe/Madrid"))

if ahora >= LANZAMIENTO:
    mensaje = (
        "🎉⚔️ ¡HA LLEGADO EL DÍA! ⚔️🎉\n\n"
        "🔥 ¡WOW FOREVER YA ESTÁ AQUÍ!\n"
        "🛡️ ¡Nos vemos en Azeroth!"
    )
else:
    dias = (LANZAMIENTO.date() - ahora.date()).days
    frase = random.choice(FRASES)

    mensaje = (
        "⚔️ *CUENTA ATRÁS PARA WOW FOREVER* ⚔️\n\n"
        f"⏳ ¡QUEDAN *{dias} DÍAS*!\n\n"
        f"{frase}\n\n"
        "🌍 ¡Nos vemos en Azeroth!"
    )

print(mensaje)
