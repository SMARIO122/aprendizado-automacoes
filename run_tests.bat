@echo off
echo 🧪 Iniciando testes Dash + Selenium...

REM Ativa o ambiente virtual
call venv\Scripts\activate.bat

REM Inicia o app em segundo plano
start "" /B python app.py
timeout /t 5 > nul

REM Executa os testes diretamente
venv\Scripts\pytest.exe test/ --maxfail=1 --disable-warnings -v

REM Encerra o app após o teste
taskkill /F /IM python.exe > nul 2>&1

echo ✅ Testes encerrados.
pause








