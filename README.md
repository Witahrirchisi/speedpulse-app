# SpeedPulse — Real-Time Network Speed & Diagnostics Core

SpeedPulse — bu real vaqtda tarmoq o'tkazuvchanligi, Ping, Jitter va tarmoq diagnostikasini yuqori aniqlikda o'lchovchi mustaqil (standalone) desktop ilovasi.

## 🚀 Asosiy Imkoniyatlar
- **Real-Time Streaming Engine**: Cloudflare Global Edge tugunlari orqali baytma-bayt yuklab olish va aniq Mbps hisoblash.
- **Diagnostics**: Packet loss, DNS qidiruv tezligi, TCP handshake va bufer tekshiruvi.
- **Floating Glass Tab Bar**: Sof Jetpack Compose prujina fizikasi (`stiffness: 380, damping: 0.75`) bilan ishlovchi shaffof navigatsiya paneli.
- **Autonomous 10-Hour OTA Pipeline**: Antigravity avtonom agenti orqali har 10 soatda yangilanishlarni qabul qilish va dinamik "Upgrade" ko'k tugmasini faollashtirish.

## 📦 Fayllar Tuzilishi
- `main.py`: PyQt6 WebEngine mustaqil desktop oynasi kirish nuqtasi.
- `index.html`: SpeedPulse foydalanuvchi interfeysi va real vaqtli o'lchov dvigateli.
- `speedpulse.ico`: Ilovaning yuqori aniqlikdagi rasmiy belgisi.
- `manifest.json`: OTA Live Upgrade konfiguratsiyasi va relizlar ta'rifi.

## 🛠️ Kompilyatsiya
```bash
python -m PyInstaller --onefile --windowed --icon="speedpulse.ico" --add-data "index.html;." --add-data "speedpulse.ico;." --name "SpeedPulse_v1" main.py
```
