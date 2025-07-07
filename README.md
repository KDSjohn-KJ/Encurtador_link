# 🔗 Encurtador de Link via Termux

Script simples em Python que encurta URLs usando a API gratuita do [is.gd](https://is.gd/). Ideal para uso direto no **Termux**.

Repositório oficial: [https://github.com/KDSjohn-KJ/Encurtador_link.git](https://github.com/KDSjohn-KJ/Encurtador_link.git)


## Requisitos

- Python 3
- Biblioteca `requests`
- Conexão com a internet
- Permissão de acesso à rede no Termux


## 🛠️ Instalação no Termux

Abra o Termux e execute os comandos abaixo:

```bash
# Atualize o Termux
pkg update && pkg upgrade -y

# Instale o Python
pkg install python -y

# Instale a biblioteca necessária
pip install requests

# Clone o repositório
git clone https://github.com/KDSjohn-KJ/Encurtador_link.git

# Acesse a pasta do projeto
cd Encurtador_link
python encurtador.py
