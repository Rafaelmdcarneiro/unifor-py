def forca(palavra):
  errado = 0
  estagios = ["", "_________ ", "| ", "|| ", "| 0 ", "| /|\ ", "| / \ ", "| "]
  letras = list(palavra)
  dicas = ["_"] * len(palavra) win = False
  print("Bem vindo ao jogo da forca")
  while errado < len(estagios) - 1: print("\n")
    msg = "Adivinhe uma letra"
    char = input(msg)
if char in letras:
  cind = letras \
.index(char)
dicas[cind] = char
letras[cind] = '$'
else:
errado += 1
print(("".join(dicas))) e = errado + 1
print("\n"
      .join(estagios[0: e]))
if "_"not in dicas: print("Você ganhou!") print("".join(dicas)) win = True
break
