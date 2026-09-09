def generate_food_recommendation(preference):
    """
    AI Prompt Engine NutriAI
    """

    prompt = f"""
    Kamu adalah NutriAI, asisten AI nutrisi.

    User memiliki preferensi makanan:
    {preference}

    Berikan rekomendasi:
    1. Nama makanan
    2. Kandungan nutrisi
    3. Manfaat kesehatan
    4. Alternatif makanan sehat

    Gunakan bahasa yang mudah dipahami.
    """

    return prompt