# Coding Standards

Este proyecto sigue estándares específicos de código definidos en `.pylintrc`.

## Convenciones de Nomenclatura

### Variables y Funciones - camelCase
```python
# ✅ Correcto
userName = 'john'
def getUserData():
    pass

# ❌ Incorrecto  
user_name = 'john'
def get_user_data():
    pass
```

### Clases - PascalCase
```python
# ✅ Correcto
class UserService:
    pass

# ❌ Incorrecto
class user_service:
    pass
```

### Constantes y Atributos de Clase - UPPER_CASE
```python
# ✅ Correcto
API_VERSION = '1.0.0'

class Echo(BaseModel):
    MSG: str

# ❌ Incorrecto
api_version = '1.0.0'

class Echo(BaseModel):
    msg: str
```

## Strings y Comillas

### Strings Regulares - Comillas Simples
```python
# ✅ Correcto
message = 'Hello world'
url = '/api/v1/users'

# ❌ Incorrecto
message = "Hello world"
```

### Docstrings - Comillas Dobles
```python
# ✅ Correcto
def processData():
    """Process user data and return results."""
    
    return data

# ❌ Incorrecto
def processData():
    '''Process user data and return results.'''
```

## Estructura de Funciones y Clases

### Formato Requerido
```python
def functionName():
    """Function description in English."""
    
    variableName = 'value'
    return variableName

class ClassName:
    """Class description in English."""
    
    CONSTANT_VALUE: str = 'default'
    
    def methodName(self):
        """Method description in English."""
        
        return self.CONSTANT_VALUE
```

## Reglas de Formato

- **Longitud máxima de línea**: 100 caracteres
- **Terminación de línea**: LF (Unix)
- **Espacios**: Usar espacios, no tabs
- **Línea en blanco**: Después de cada docstring

## Middlewares y Parámetros Especiales

Para middlewares de FastAPI/Starlette:
```python
async def middleware(request: Request, callNext):
    """Handle HTTP request middleware."""
    
    response = await callNext(request)
    return response
```

## Configuración Pylint

El archivo `.pylintrc` está configurado para:
- Ignorar directorios: `.venv`, `venv`, `.pdm-build`
- Deshabilitar: docstrings de módulo, trailing newlines, whitespace
- Enforcar: camelCase para variables/funciones, PascalCase para clases
- Strings: comillas simples con consistencia