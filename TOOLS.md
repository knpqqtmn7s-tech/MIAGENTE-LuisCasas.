# 🔧 Herramientas Disponibles

## web_fetch — Peticiones HTTP

### Descripción
Herramienta para hacer peticiones HTTP GET a URLs externas y obtener su contenido.

### Uso
```
web_fetch(url, extractMode, maxChars)
```

### Parámetros
| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `url` | string | URL a consultar |
| `extractMode` | string | "text" para extraer texto |
| `maxChars` | int | Límite de caracteres (opcional) |

---

## API del Clima: Open-Meteo

### Endpoint
```
https://api.open-meteo.com/v1/forecast
```

### Parámetros Requeridos
| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `latitude` | float | Latitud (-90 a 90) |
| `longitude` | float | Longitud (-180 a 180) |
| `current_weather` | boolean | `true` para clima actual |

### Ejemplo de URL completa
```
https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true
```

### Respuesta JSON
```json
{
  "current_weather": {
    "temperature": 22.5,
    "windspeed": 12.3,
    "winddirection": 180,
    "weathercode": 0,
    "is_day": 1,
    "time": "2026-04-08T14:00"
  }
}
```

### Interpretación de weathercode
| Código | Clima |
|--------|-------|
| 0 | Despejado |
| 1-3 | Nublado |
| 45, 48 | Niebla |
| 51-55 | Llovizna |
| 61-65 | Lluvia |
| 71-75 | Nieve |
| 95 | Tormenta |