import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "desenvolvedor", "algoritmo"]

# Escolhe uma palavra aleatória usando random.randint()
indice = random.randint(0, len(palavras) - 1)
palavra_secreta = palavras[indice]

# Inicializa as variáveis do jogo
letras_descobertas = ["_" for _ in palavra_secreta]  # Palavra oculta
tentativas_restantes = 6
letras_erradas = []

print("🎮 Bem-vindo ao jogo da Forca!")
print("A palavra tem", len(palavra_secreta), "letras.")

# Loop principal do jogo
while "_" in letras_descobertas and tentativas_restantes > 0:
    print("\nPalavra:", " ".join(letras_descobertas))
    print(f"Tentativas restantes: {tentativas_restantes}")
    print(f"Letras erradas: {', '.join(letras_erradas) if letras_erradas else 'Nenhuma'}")

    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi tentada
    if letra in letras_descobertas or letra in letras_erradas:
        print("❗ Você já tentou essa letra.")
        continue

    # Verifica se a letra está na palavra
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
        print("✅ Letra correta!")
    else:
        tentativas_restantes -= 1
        letras_erradas.append(letra)
        print("❌ Letra errada!")

# Verifica o resultado do jogo
if "_" not in letras_descobertas:
    print("\n🎉 Parabéns! Você acertou a palavra:", palavra_secreta)
else:
    print("\n💀 Game Over! A palavra era:", palavra_secreta)

