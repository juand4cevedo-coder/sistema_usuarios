"""Validaciones de los datos de entrada de un usuario."""

EDAD_MINIMA = 1
EDAD_MAXIMA = 120


class ValidacionError(ValueError):
    """Se lanza cuando un dato de entrada no cumple las reglas de validación."""


def validar_nombre(nombre: str) -> str:
    """Devuelve el nombre sin espacios sobrantes o lanza ValidacionError."""
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValidacionError("El nombre no puede estar vacío.")
    if not nombre_limpio.replace(" ", "").isalpha():
        raise ValidacionError("El nombre solo puede contener letras y espacios.")
    return nombre_limpio


def validar_edad(edad: str) -> int:
    """Convierte la edad a entero y verifica que esté en el rango permitido."""
    try:
        edad_numerica = int(edad)
    except ValueError:
        raise ValidacionError("La edad debe ser un número entero.") from None
    if not EDAD_MINIMA <= edad_numerica <= EDAD_MAXIMA:
        raise ValidacionError(
            f"La edad debe estar entre {EDAD_MINIMA} y {EDAD_MAXIMA}."
        )
    return edad_numerica
