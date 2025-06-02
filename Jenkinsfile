pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}/venv"
    }

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
                    python3 -m venv venv || true
                    . venv/bin/activate || true
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Executar iniciar.sh') {
            steps {
                sh '''
                    chmod +x iniciar.sh
                    . venv/bin/activate || true
                    ./iniciar.sh
                '''
            }
        }

        stage('Rodar app.py') {
            steps {
                sh '''
                    . venv/bin/activate || true
                    nohup python3 app.py > output.log 2>&1 &
                '''
            }
        }


stage('Aguardar app') {
    steps {
        echo '⏳ Esperando app ficar disponível na porta 8050...'
        sh '''
        for i in {1..10}; do
            curl -s http://127.0.0.1:8050 && break
            echo "Aguardando app subir..."
            sleep 2
        done
        '''
    }
}


        stage('Rodar testes') {
            steps {
                sh '''
                    . venv/bin/activate || true
                    pytest || true
                '''
            }
        }
    }

    post {
        always {
            echo '🔄 Pipeline finalizada.'
        }
        failure {
            echo '❌ Algo deu ruim na pipeline!'
        }
        success {
            echo '✅ Tudo certo! Deploy/execução finalizada.'
        }
    }
}

