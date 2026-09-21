"""Carga y expone la configuración de la aplicación desde variables de entorno."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True, slots=True)
class Settings:
    """Configuración inmutable de la aplicación."""

    app_name: str
    app_version: str
    admin_user: str


settings = Settings(
    app_name=os.getenv("APP_NAME", "Sistema Usuarios"),
    app_version=os.getenv("APP_VERSION", "1.0"),
    admin_user=os.getenv("ADMIN_USER", "admin"),
)
