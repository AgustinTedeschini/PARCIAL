def validar_casteo_int(string: str) -> bool:
    for i in string:
        if ((i < "0" or i > "9") and i != ".") or len(string) < 1 or string[0] == ".":
            return False
    return True