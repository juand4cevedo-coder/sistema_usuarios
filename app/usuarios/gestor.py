"""Gestión en memoria de usuarios: registro, listado y búsqueda."""

from dataclasses import dataclass

from app.usuarios.validaciones import ValidacionError, validar_edad, validar_nombre


@dataclass(frozen=True, slots=True)
class Usuario:
    """Representa a un usuario registrado."""

    id: int
    nombre: str
    edad: int


class UsuarioNoEncontradoError(LookupError):
    """Se lanza cuando una búsqueda no produce coincidencias."""


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

    def listar(self) -> list[Usuario]:
        """Devuelve una copia de la lista de usuarios registrados."""
        return list(self._usuarios)

    def buscar(self, termino: str) -> list[Usuario]:
        """Busca usuarios cuyo nombre contenga el término, sin distinguir mayúsculas."""
        termino_normalizado = termino.strip().casefold()
        if not termino_normalizado:
            raise ValidacionError("El término de búsqueda no puede estar vacío.")
        coincidencias = [
            usuario
            for usuario in self._usuarios
            if termino_normalizado in usuario.nombre.casefold()
        ]
        if not coincidencias:
            raise UsuarioNoEncontradoError(
                f"No se encontraron usuarios que coincidan con '{termino}'."
            )
        return coincidencias
