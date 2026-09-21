"""Punto de entrada: menú de consola del sistema de gestión de usuarios."""

from collections.abc import Callable

from app.config.settings import settings
from app.usuarios.gestor import GestorUsuarios, UsuarioNoEncontradoError
from app.usuarios.validaciones import ValidacionError

MENU = """
1. Registrar usuario
2. Listar usuarios
3. Buscar usuario
4. Salir
"""


def registrar_usuario(gestor: GestorUsuarios) -> None:
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    usuario = gestor.registrar(nombre, edad)
    print(f"✔ Usuario '{usuario.nombre}' registrado con ID {usuario.id}.")


def listar_usuarios(gestor: GestorUsuarios) -> None:
    usuarios = gestor.listar()
    if not usuarios:
        print("No hay usuarios registrados todavía.")
        return
    for usuario in usuarios:
        print(f"[{usuario.id}] {usuario.nombre} - {usuario.edad} años")


def buscar_usuarios(gestor: GestorUsuarios) -> None:
    termino = input("Nombre a buscar: ")
    for usuario in gestor.buscar(termino):
        print(f"[{usuario.id}] {usuario.nombre} - {usuario.edad} años")


ACCIONES: dict[str, Callable[[GestorUsuarios], None]] = {
    "1": registrar_usuario,
    "2": listar_usuarios,
    "3": buscar_usuarios,
}


def main() -> None:
    gestor = GestorUsuarios()
    print(f"=== {settings.app_name} v{settings.app_version} ===")
    print(f"Administrador: {settings.admin_user}")

    while True:
        print(MENU)
        opcion = input("Elige una opción: ").strip()
        if opcion == "4":
            print("¡Hasta pronto!")
            break
        accion = ACCIONES.get(opcion)
        if accion is None:
            print("✖ Opción no válida. Intenta de nuevo.")
            continue
        try:
            accion(gestor)
        except (ValidacionError, UsuarioNoEncontradoError) as error:
            print(f"✖ {error}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt, EOFError:
        print("\nPrograma interrumpido. ¡Hasta pronto!")
