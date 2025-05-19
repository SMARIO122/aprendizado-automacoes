#!/bin/bash
echo "🚀 Iniciando testes Dash + Selenium..."

# Ativa o ambiente virtual
source venv/bin/activate

# Inicia o app em segundo plano
python app.py &

# Pega o PID do app.py
APP_PID=$!

# Espera o servidor subir
sleep 7

# Executa os testes
pytest test/ --maxfail=1 --disable-warnings -v

# Finaliza o servidor
kill $APP_PID

echo "✅ Testes encerrados."
