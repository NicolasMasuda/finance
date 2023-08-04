# Interés Simple y Compuesto en Python

Este repositorio contiene funciones en Python para calcular el interés simple y compuesto, así como para calcular el valor presente y futuro de anualidades.

## Interés Simple

La función `Interes(ValorPresente, Periodo, Tasa)` calcula el interés simple sobre una cantidad de dinero, utilizando la fórmula `ValorPresente * Periodo * Tasa`.

La función `ValorFuturoSimple(ValorPresente, Periodo, Tasa)` calcula el valor futuro de una inversión utilizando el método de interés simple, utilizando la fórmula `ValorPresente * (1 + Periodo * Tasa)`.

## Interés Compuesto

La función `ValorFuturoCompuesto(ValorPresente, Periodo, Tasa)` calcula el valor futuro de una inversión utilizando el método de interés compuesto, utilizando la fórmula `ValorPresente * (1 + Tasa)^Periodo`.

La función `ValorPresenteCompuesto(ValorFuturo, Periodo, Tasa)` calcula el valor presente de una inversión utilizando el método de interés compuesto, utilizando la fórmula `ValorFuturo / (1 + Tasa)^Periodo`.

## Anualidades

La función `ValorPresenteAnualidad(Anualidad, Periodo, Tasa)` calcula el valor presente de una anualidad, utilizando la fórmula `Anualidad * ((1 - (1 + Tasa)^(-Periodo)) / Tasa)`.

La función `ValorFuturoAnualidad(Anualidad, Periodo, Tasa)` calcula el valor futuro de una anualidad, utilizando la fórmula `Anualidad * ((1 + Tasa)^Periodo - 1) / Tasa`.

La función `CuotaValorPresente(ValorPresenteAnualidad, Periodo, Tasa)` calcula la cuota periódica necesaria para obtener un valor presente de una anualidad, utilizando la fórmula `ValorPresenteAnualidad / ((1 - (1 + Tasa)^(-Periodo)) / Tasa)`.

La función `CuotaValorFuturo(ValorFuturoAnualidad, Periodo, Tasa)` calcula la cuota periódica necesaria para obtener un valor futuro de una anualidad, utilizando la fórmula `ValorFuturoAnualidad / ((1 + Tasa)^Periodo - 1) / Tasa`.

## Uso

Puedes utilizar estas funciones para calcular intereses, valores futuros, valores presentes y cuotas de anualidades.

Ejemplo de uso:

```python
import math

# Calcular interés simple
valor_presente = 1000
periodo = 2
tasa = 0.05
interes = Interes(valor_presente, periodo, tasa)
print(f"Interés simple: {interes}")

# Calcular valor futuro compuesto
valor_futuro = ValorFuturoCompuesto(valor_presente, periodo, tasa)
print(f"Valor futuro compuesto: {valor_futuro}")
