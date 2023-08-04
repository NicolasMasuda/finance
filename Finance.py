import math

################################################Interes Simple###########################################
def Interes(ValorPresente: float, Periodo: float, Tasa:float) -> float:
    """
    Calcula el interés sobre una cantidad de dinero.

    Args:
        ValorPresente (float): Valor presente o cantidad de dinero.
        Periodo (Float): Período de tiempo.
        Tasa (float): Tasa de interés.

    Returns:
        float: El interés calculado.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.
    """

    if ValorPresente < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")
    
    # Calcula el interés multiplicando el valor presente, el período y la tasa de interés
    Interes = ValorPresente * Periodo * Tasa

    # Devuelve el valor del interés calculado
    return Interes

def ValorFuturoSimple(ValorPresente: float, Periodo: float, Tasa:float) -> float:
    """
    Calcula el valor futuro de una inversión utilizando el método de interés simple.

    Args:
        ValorPresente (float): El valor presente o cantidad de dinero a invertir.
        Periodo (float): El período de tiempo.
        Tasa (float): La tasa de interés.

    Returns:
        float: El valor futuro calculado como un número de punto flotante.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.
    """

    if ValorPresente < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")
    
    # Calcula el valor futuro utilizando la fórmula del interés simple
    ValorFuturoSimple = ValorPresente * (1 + Periodo * Tasa)

    # Devuelve el valor del Valor Futuro Simple
    return ValorFuturoSimple

################################################Interes Compuesto###########################################
def ValorFuturoCompuesto(ValorPresente: float, Periodo: float, Tasa: float) -> float:
    """
    Calcula el valor futuro de una inversión utilizando el método de interés compuesto.

    Args:
        ValorPresente (float): El valor presente o cantidad de dinero a invertir.
        Periodo (float): El período de tiempo.
        Tasa (float): La tasa de interés.

    Returns:
        float: El valor futuro calculado como un número de punto flotante.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.

    Notes:
        El cálculo del valor futuro se realiza utilizando la fórmula: 
        ValorFuturoCompuesto = ValorPresente * (1 + Tasa)^Periodo

    """
    if ValorPresente < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")

    # Calcula el valor futuro utilizando la fórmula del interés compuesto
    ValorFuturoCompuesto = ValorPresente * pow(1 + Tasa, Periodo)

    return ValorFuturoCompuesto

def ValorPresenteCompuesto(ValorFuturo: float, Periodo: float, Tasa: float) -> float:
    """
    Calcula el valor presente de una inversión utilizando el método de interés compuesto.

    Args:
        ValorFuturo (float): El valor futuro deseado.
        Periodo (float): El período de tiempo.
        Tasa (float): La tasa de interés.

    Returns:
        float: El valor presente calculado como un número de punto flotante.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.

    Notes:
        El cálculo del valor presente se realiza utilizando la fórmula: 
        ValorPresenteCompuesto = ValorFuturo / (1 + Tasa)^Periodo

    """
    if ValorFuturo < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")

    # Calcula el valor presente utilizando la fórmula del interés compuesto
    ValorPresenteCompuesto = ValorFuturo / pow(1 + Tasa, Periodo)

    return ValorPresenteCompuesto

################################################Anualidad###########################################

def ValorPresenteAnualidad(Anualidad: float, Periodo: float, Tasa: float) -> float:
    """
    Calcula el valor presente de una anualidad.

    Args:
        Anualidad (float): El valor de la anualidad.
        Periodo (float): El período de tiempo en años.
        Tasa (float): La tasa de interés anual.

    Returns:
        float: El valor presente de la anualidad.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.

    Notes:
        El cálculo del valor presente de una anualidad se realiza utilizando la fórmula: 
        ValorPresenteAnualidad = Anualidad * ((1 - (1 + Tasa)^(Periodo)) / Tasa)

    """
    if Anualidad < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")

    # Calcula el valor presente de la anualidad utilizando la fórmula de la anualidad
    #ValorPresenteAnualidad = Anualidad * ((1 - 1 / pow(1 + Tasa, Periodo)) / Tasa)
    ValorPresenteAnualidad = Anualidad * (( 1 - (1+Tasa)**-Periodo)/Tasa)

    return ValorPresenteAnualidad

def ValorFuturoAnualidad(Anualidad: float, Periodo: float, Tasa: float) -> float:
    """
    Calcula el valor futuro de una anualidad.

    Args:
        Anualidad (float): El valor de la anualidad.
        Periodo (float): El período de tiempo en años.
        Tasa (float): La tasa de interés anual.

    Returns:
        float: El valor futuro de la anualidad.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.

    Notes:
        El cálculo del valor futuro de una anualidad se realiza utilizando la fórmula: 
        ValorFuturoAnualidad = Anualidad * ((1 + Tasa)^Periodo - 1) / Tasa

    """
    if Anualidad < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")

    # Calcula el valor futuro de la anualidad utilizando la fórmula de la anualidad
    ValorFuturoAnualidad = Anualidad * ((pow(1 + Tasa, Periodo) - 1) / Tasa)

    return ValorFuturoAnualidad

def CuotaValorPresente(ValorPresenteAnualidad: float, Periodo: float, Tasa: float) -> float:
    """
    Calcula la cuota periódica necesaria para obtener un valor presente de una anualidad.

    Args:
        ValorPresenteAnualidad (float): El valor presente de la anualidad.
        Periodo (float): El período de tiempo en años.
        Tasa (float): La tasa de interés anual.

    Returns:
        float: La cuota periódica necesaria.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.

    Notes:
        El cálculo de la cuota periódica se realiza utilizando la fórmula: 
        CuotaValorPresente = ValorPresenteAnualidad / ((1 - (1 + Tasa)^(-Periodo)) / Tasa)

    """
    if ValorPresenteAnualidad < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")

    # Calcula la cuota periódica utilizando la fórmula correspondiente
    CuotaValorPresente = ValorPresenteAnualidad / ((1 - 1 / pow(1 + Tasa, Periodo)) / Tasa)

    return CuotaValorPresente

def CuotaValorFuturo(ValorFuturoAnualidad: float, Periodo: float, Tasa: float) -> float:
    """
    Calcula la cuota periódica necesaria para obtener un valor futuro de una anualidad.

    Args:
        ValorFuturoAnualidad (float): El valor futuro de la anualidad.
        Periodo (float): El período de tiempo en años.
        Tasa (float): La tasa de interés anual.

    Returns:
        float: La cuota periódica necesaria.

    Raises:
        ValueError: Si algún argumento tiene un valor negativo.

    Notes:
        El cálculo de la cuota periódica se realiza utilizando la fórmula: 
        CuotaValorFuturo = ValorFuturoAnualidad / ((1 + Tasa)^Periodo - 1) / Tasa)

    """
    if ValorFuturoAnualidad < 0 or Periodo < 0 or Tasa < 0:
        raise ValueError("Los argumentos deben ser valores no negativos.")

    # Calcula la cuota periódica utilizando la fórmula correspondiente
    CuotaValorFuturo = ValorFuturoAnualidad / ((pow(1 + Tasa, Periodo) - 1) / Tasa)

    return CuotaValorFuturo

