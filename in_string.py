def check_vowels():
    # Código a implementar utilizando input.
    nombre = input("> ")
    print(f"Contiene a: {"a" in nombre.lower()}")
    print(f"Contiene e: {"e" in nombre.lower()}")
    print(f"Contiene i: {"i" in nombre.lower()}")
    print(f"Contiene o: {"o" in nombre.lower()}")
    print(f"Contiene u: {"u" in nombre.lower()}") 

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
