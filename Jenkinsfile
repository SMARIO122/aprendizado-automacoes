pipeline {
    agent any

    stages {
        stage('Preparar ambiente Python') {
            steps {
                sh '''
                    apt update || true
                    apt install -y python3-pip python3-venv || true
                '''
            }
        }

        stage('Criar venv e instalar dependências') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install flake8
                '''
            }
        }

        stage('Executar iniciar.sh') {
            steps {
                sh '''
                    chmod +x iniciar.sh
                    . venv/bin/activate
                    ./iniciar.sh
                '''
            }
        }

        stage('Rodar app.py') {
            steps {
                sh '''
                    . venv/bin/activate
                    nohup python3 app.py &
                '''
            }
        }

        stage('Aguardar app') {
            steps {
                echo '⏳ Esperando app ficar disponível na porta 8050...'
                sh '''
                    until curl -s http://127.0.0.1:8050; do
                        echo "Aguardando app subir..."
                        sleep 2
                    done
                '''
            }
        }

        stage('Análise estática com flake8') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || true
                '''
            }
        }

        stage('Rodar testes') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }
    }

    post {
        always {
            echo '🔄 Pipeline finalizada.'
        }
        success {
            echo '✅ Tudo certo! Deploy/execução finalizada.'
        }
        failure {
            echo '❌ Algo deu errado na pipeline.'
        }
    }
}
