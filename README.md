# Documentación de Casos de Prueba

## Información general

| Campo | Valor |
|---|---|
| Proyecto | Calculadora TDD |
| Metodología | Test-Driven Development |
| Framework de pruebas | Pytest |
| Lenguaje | Python 3 |
| Versión | 1.0 |
| Fecha | 2026-05-07 |

---

# Estructura de casos de prueba

Cada caso de prueba contiene:

- Código del caso
- Título
- Módulo
- Severidad
- Prioridad
- Entradas
- Pasos de ejecución
- Resultado esperado
- Resultado obtenido
- Estado
- Observaciones
- Fecha de ejecución

---

# Casos de Prueba

---

# CP-001 — Validar suma de números positivos

| Campo | Detalle |
|---|---|
| Código | CP-001 |
| Título | Validar suma de números positivos |
| Módulo | Suma |
| Severidad | Alta |
| Prioridad | Alta |
| Entradas | a = 2, b = 3 |
| Resultado esperado | El sistema debe retornar 5 |
| Resultado obtenido | 5 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Operación ejecutada correctamente |

## Pasos de ejecución

1. Instanciar la clase `Calculadora`
2. Ejecutar método `sumar(2,3)`
3. Validar resultado

## Código del test

```python
def test_suma_positiva():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5
```

---

# CP-002 — Validar suma de números negativos

| Campo | Detalle |
|---|---|
| Código | CP-002 |
| Título | Validar suma de números negativos |
| Módulo | Suma |
| Severidad | Media |
| Prioridad | Alta |
| Entradas | a = -2, b = -3 |
| Resultado esperado | El sistema debe retornar -5 |
| Resultado obtenido | -5 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | El sistema soporta números negativos |

## Pasos de ejecución

1. Instanciar calculadora
2. Ejecutar `sumar(-2,-3)`
3. Verificar resultado

## Código del test

```python
def test_suma_negativa():
    calc = Calculadora()
    assert calc.sumar(-2, -3) == -5
```

---

# CP-003 — Validar suma con cero

| Campo | Detalle |
|---|---|
| Código | CP-003 |
| Título | Validar suma con cero |
| Módulo | Suma |
| Severidad | Baja |
| Prioridad | Media |
| Entradas | a = 5, b = 0 |
| Resultado esperado | El sistema debe retornar 5 |
| Resultado obtenido | 5 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Correcto manejo del cero |

## Pasos de ejecución

1. Ejecutar `sumar(5,0)`
2. Validar resultado

## Código del test

```python
def test_suma_con_cero():
    calc = Calculadora()
    assert calc.sumar(5, 0) == 5
```

---

# CP-004 — Validar resta positiva

| Campo | Detalle |
|---|---|
| Código | CP-004 |
| Título | Validar resta positiva |
| Módulo | Resta |
| Severidad | Alta |
| Prioridad | Alta |
| Entradas | a = 5, b = 3 |
| Resultado esperado | El sistema debe retornar 2 |
| Resultado obtenido | 2 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Operación correcta |

## Pasos de ejecución

1. Ejecutar `restar(5,3)`
2. Verificar resultado

## Código del test

```python
def test_resta_positiva():
    calc = Calculadora()
    assert calc.restar(5, 3) == 2
```

---

# CP-005 — Validar resultado negativo en resta

| Campo | Detalle |
|---|---|
| Código | CP-005 |
| Título | Validar resultado negativo en resta |
| Módulo | Resta |
| Severidad | Media |
| Prioridad | Media |
| Entradas | a = 3, b = 5 |
| Resultado esperado | El sistema debe retornar -2 |
| Resultado obtenido | -2 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Resultado negativo correcto |

## Pasos de ejecución

1. Ejecutar `restar(3,5)`
2. Validar resultado

## Código del test

```python
def test_resta_negativa():
    calc = Calculadora()
    assert calc.restar(3, 5) == -2
```

---

# CP-006 — Validar multiplicación positiva

| Campo | Detalle |
|---|---|
| Código | CP-006 |
| Título | Validar multiplicación positiva |
| Módulo | Multiplicación |
| Severidad | Alta |
| Prioridad | Alta |
| Entradas | a = 4, b = 5 |
| Resultado esperado | El sistema debe retornar 20 |
| Resultado obtenido | 20 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Multiplicación correcta |

## Pasos de ejecución

1. Ejecutar `multiplicar(4,5)`
2. Verificar resultado

## Código del test

```python
def test_multiplicacion_positiva():
    calc = Calculadora()
    assert calc.multiplicar(4, 5) == 20
```

---

# CP-007 — Validar multiplicación por cero

| Campo | Detalle |
|---|---|
| Código | CP-007 |
| Título | Validar multiplicación por cero |
| Módulo | Multiplicación |
| Severidad | Media |
| Prioridad | Alta |
| Entradas | a = 4, b = 0 |
| Resultado esperado | El sistema debe retornar 0 |
| Resultado obtenido | 0 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Correcto manejo del cero |

## Pasos de ejecución

1. Ejecutar `multiplicar(4,0)`
2. Verificar resultado

## Código del test

```python
def test_multiplicacion_por_cero():
    calc = Calculadora()
    assert calc.multiplicar(4, 0) == 0
```

---

# CP-008 — Validar multiplicación negativa

| Campo | Detalle |
|---|---|
| Código | CP-008 |
| Título | Validar multiplicación negativa |
| Módulo | Multiplicación |
| Severidad | Media |
| Prioridad | Media |
| Entradas | a = -2, b = 3 |
| Resultado esperado | El sistema debe retornar -6 |
| Resultado obtenido | -6 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Correcto manejo de signos |

## Código del test

```python
def test_multiplicacion_negativa():
    calc = Calculadora()
    assert calc.multiplicar(-2, 3) == -6
```

---

# CP-009 — Validar división exacta

| Campo | Detalle |
|---|---|
| Código | CP-009 |
| Título | Validar división exacta |
| Módulo | División |
| Severidad | Alta |
| Prioridad | Crítica |
| Entradas | a = 10, b = 2 |
| Resultado esperado | El sistema debe retornar 5 |
| Resultado obtenido | 5 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | División correcta |

## Código del test

```python
def test_division_exacta():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5
```

---

# CP-010 — Validar división decimal

| Campo | Detalle |
|---|---|
| Código | CP-010 |
| Título | Validar división decimal |
| Módulo | División |
| Severidad | Alta |
| Prioridad | Alta |
| Entradas | a = 7, b = 2 |
| Resultado esperado | El sistema debe retornar 3.5 |
| Resultado obtenido | 3.5 |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Manejo correcto de decimales |

## Código del test

```python
def test_division_decimal():
    calc = Calculadora()
    assert calc.dividir(7, 2) == 3.5
```

---

# CP-011 — Validar excepción por división entre cero

| Campo | Detalle |
|---|---|
| Código | CP-011 |
| Título | Validar excepción por división entre cero |
| Módulo | Manejo de errores |
| Severidad | Crítica |
| Prioridad | Crítica |
| Entradas | a = 5, b = 0 |
| Resultado esperado | Lanzar excepción ValueError |
| Resultado obtenido | Excepción capturada correctamente |
| Estado | PASSED |
| Fecha | 2026-05-07 |
| Observaciones | Validación de seguridad correcta |

## Pasos de ejecución

1. Ejecutar `dividir(5,0)`
2. Capturar excepción
3. Validar tipo de excepción

## Código del test

```python
import pytest

def test_division_por_cero():
    calc = Calculadora()

    with pytest.raises(ValueError):
        calc.dividir(5, 0)
```

---

# Resumen de ejecución

| Métrica | Resultado |
|---|---|
| Total casos ejecutados | 11 |
| Casos exitosos | 11 |
| Casos fallidos | 0 |
| Cobertura funcional | 100% |
| Estado general | APROBADO |

---

# Evidencia TDD

## RED

Inicialmente los tests fallan porque la implementación no existe.

## GREEN

Se implementa el código mínimo necesario para pasar los tests.

## REFACTOR

Se mejora el código agregando:

- Tipado
- Métodos estáticos
- Documentación
- Mejor legibilidad

Manteniendo todos los tests en estado PASSED.