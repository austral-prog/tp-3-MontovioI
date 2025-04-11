def slice_simple():
    texto = "Awesome"
    print(texto[0:3].lower())
    medio=int(len(texto)/2)
    print(texto[medio-1:medio+2].lower())
    print(texto[0:4].lower()+texto[len(texto)-3:len(texto):].lower())
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
