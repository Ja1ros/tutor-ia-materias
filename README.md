# Tutor IA por Materia

Tutor virtual que responde dudas de matematicas, programacion, fisica, quimica y biologia usando un LLM (OpenAI GPT-4o-mini).

## Caracteristicas

- Seleccion de materia y nivel academico (escolar, bachillerato, universitario).
- Explicaciones paso a paso con ejemplos.
- Interfaz de chat conversacional con historial de la sesion.
- Prompt de sistema adaptado dinamicamente segun la materia y el nivel elegido.

## Stack tecnologico

- Python 3.10+
- Streamlit
- OpenAI API

## Instalacion

```bash
git clone https://github.com/Ja1ros/tutor-ia-materias.git
cd tutor-ia-materias
pip install -r requirements.txt
```

## Uso

```bash
streamlit run app.py
```

1. Ingresa tu API Key de OpenAI en la barra lateral.
2. Selecciona la materia y el nivel academico.
3. Escribe tu pregunta en el chat.

## Variables de entorno

Crea un archivo `.env` basado en `.env.example` si prefieres no ingresar la API Key manualmente.

## Proximas mejoras

- Guardar historial de conversaciones por materia.
- Generacion de ejercicios practicos personalizados.
- Despliegue en Streamlit Cloud.

## Licencia

Proyecto con fines educativos y de portafolio.
