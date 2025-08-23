def duplicate_count(text: str):
    text = text.lower()
    contador = 0
    for char in set(text):
        if text.count(char) > 1:
            contador += 1
            print(contador)
    return contador

duplicate_count("hola")
duplicate_count("holaa")
duplicate_count("holaA")
duplicate_count("Bus")
duplicate_count("Busbbaa")