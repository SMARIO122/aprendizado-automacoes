#!/bin/bash

echo "🎯 Ativando ambiente virtual..."
source venv/bin/activate

echo "🚀 Iniciando o servidor Dash em segundo plano..."
python app.py &

APP_PID=$!
echo "🧠 Servidor rodando no PID: $APP_PID"
echo "⏳ Aguardando o servidor iniciar..."
sleep 5

echo "🧪 Executando os testes com pytest..."
pytest -v

echo "🧼 Encerrando o servidor..."
kill -9 $APP_PID

echo "✅ Finalizado!"
