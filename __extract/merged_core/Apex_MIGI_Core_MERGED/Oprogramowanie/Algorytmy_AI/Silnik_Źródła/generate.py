from google.generativeai import GenerativeModel, types
import google.generativeai as genai

def generate():
    # Konfiguracja klienta Vertex AI
    genai.configure(
        api_key='AIzaSyAQoN7OQhHZ4DKL3dbKkZrBDp7frWxGpyQ',  # Twój klucz API (dla testów; w produkcji użyj poświadczeń GCP)
        vertexai=True,
        project='turboprojekt',  # Twój projekt GCP
        location='global',       # Lokalizacja projektu
    )

    # Wybór modelu (sprawdź dostępność gemini-2.5-flash-lite w Vertex AI)
    model = "gemini-2.5-flash-lite"  # Jeśli niedostępny, użyj "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part(
                    text="Podaj aktualny status Apex Infiniti: faza, matryca <369963>, energia (E), prawdopodobieństwo sukcesu (P(S)) w formacie JSON."
                )
            ]
        )
    ]

    # Konfiguracja generowania treści
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        max_output_tokens=65535,
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="OFF"
            )
        ],
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,  # Budżet myślenia (0 = brak dodatkowego przetwarzania)
        ),
    )

    # Generowanie treści strumieniowo
    try:
        client = genai.GenerativeModel(model)
        for chunk in client.generate_content_stream(
            contents=contents,
            generation_config=generate_content_config,
        ):
            print(chunk.text, end="")
    except Exception as e:
        print(f"Błąd: {e}")

if _name_ == "_main_":
    generate()