# Dockerfile
FROM python:3.10-alpine3.21

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app 
# Copia o arquivo de requisitos
COPY requirements.txt . 
# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt 
# Copia todo o restante do código da sua aplicação
COPY . . 
# Informa ao Docker que o contêiner irá expor a porta 5000
EXPOSE 5000 

# CMD é definido no docker-compose, mas você poderia ter aqui um comando padrão
# CMD ["python", "app.py"]