"""Gestión en memoria de usuarios: registro, listado y búsqueda."""

from dataclasses import dataclass

from app.usuarios.validaciones import validar_edad, validar_nombre


@dataclass(frozen=True, slots=True)
class Usuario:
    """Representa a un usuario registrado."""

    id: int
    nombre: str
    edad: int


class GestorUsuarios:
    """Administra la colección de usuarios en memoria."""

    def __init__(self) -> None:
        self._usuarios: list[Usuario] = []

    def registrar(self, nombre: str, edad: str) -> Usuario:
        """Valida los datos y registra un nuevo usuario."""
        usuario = Usuario(
            id=len(self._usuarios) + 1,
            nombre=validar_nombre(nombre),
            edad=validar_edad(edad),
        )
        self._usuarios.append(usuario)
        return usuario
