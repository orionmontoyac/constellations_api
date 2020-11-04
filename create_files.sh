#!/bin/bash
OBJ_NAME="constellations"

mkdir "app"
touch "app/__init__.py"
touch "app/db.py" # Configuración de la base de datos
touch "app/ext.py" # Instanciación de las extensiones

mkdir "app/common"
touch "app/common/__init__.py" # Configuración de la aplicación
touch "app/common/error_handling.py" # Utilidades para el manejo de errores

mkdir "app/"$OBJ_NAME
touch "app/"$OBJ_NAME"/__init__.py"
touch "app/"$OBJ_NAME"/models.py" # Modelos

mkdir "app/"$OBJ_NAME"/api_v1_0"
touch "app/"$OBJ_NAME"/api_v1_0/__init__.py"
touch "app/"$OBJ_NAME"/api_v1_0/resources.py" # Endpoints del API
touch "app/"$OBJ_NAME"/api_v1_0/schemas.py" # Esquemas para serializar los modelos

mkdir "config"
touch "config/__init__.py"
touch "config/default.py" # Configuración por defecto

touch "entrypoint.py" # Crea la instancia de la app