# 🌤️ MIAGENTE-LuisCasas

Agente de IA para consultas meteorológicas usando **nanobot-ai** y la API de **Open-Meteo**.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/knpqqtmn7s-tech/MIAGENTE-LuisCasas..git
cd MIAGENTE-LuisCasas.
```

### 2. Crear entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar entorno virtual

**Linux / macOS:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install nanobot-ai
```
---

## ▶️ Ejecución

```bash
make run
```

O manualmente:

```bash
python nanobots-skills.py
```

---

## Ejemplo de Uso

```
==================================================
🤖 NANOBOT - Agente del Clima
==================================================

👤 Tú: ¿Cómo está el clima en Ciudad de México?

🔄 Procesando...

🤖 Nanobot: El clima actual en Ciudad de México es de 22°C con 
   viento de 12 km/h. Está despejado, ¡buen día para salir! ☀️
```

---

## API Utilizada

**Open-Meteo** - API gratuita de clima (sin registro requerido)

```
https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true
```

---

## 💰 Modelo de IA

**gemini-3.1-flash-lite-preview** via gemini


---

## 📝 Licencia

Proyecto educativo - Libre uso