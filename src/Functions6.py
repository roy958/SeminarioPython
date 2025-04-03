def contar (cont,descriptions):
    for frase in descriptions:
        for word in frase:
            if word == "música":
                cont ["música"] += 1
            elif word == "entretenimiento":
                cont ["entretenimiento"] += 1
            elif word == "charla":
                cont ["charla"]+= 1
    return cont                