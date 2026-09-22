allowed_statuses={"disponible","reservado","vendida"}
required_keywords={"usada","certificada"}

def validate_not_empty(value:str,field_name:str)->None:
    if not isinstance(value,str) or not value.strip():
        raise ValueError(f"El campo ${field_name} no puede estar vacia")

def validate_price(price:float)-> None:
    if not isinstance(price,(int,float)) or isinstance(price,bool):
        raise ValueError("El precio debe ser un valor numerico")
    if price<=0:
        raise ValueError("El precio debe ser mayor que 0")

def validate_status(status:str)->None:
    validate_not_empty(status,"status")
    normalized_status=status.strip().lower()
    if normalized_status not in allowed_statuses:
        allowed=",".join(list(allowed_statuses))
        raise ValueError(f"Estado {status} no valido. Estado permitido: {allowed}")

def validate_description(description: str) -> None:
    validate_not_empty(description, "description")
    text = description.lower()
    if not any(keyword in text for keyword in required_keywords):
        raise ValueError("La descripción debe incluir las palabras 'usada' o 'certificada'.")