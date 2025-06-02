pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                git 'https://github.com/SMARIO122/aprendizado-automacoes.git'
            }
        }

        stage('Criar ambiente virtual') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Ativar venv e instalar dependências') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
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

        stage('Rodar app.py em background') {
            steps {
                sh '''
                    . venv/bin/activate
                    nohup python3 app.py > output.log 2>&1 &
                '''
            }
        }

        stage('Executar testes') {
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
        failure {
            echo '❌ Algo deu ruim na pipeline!'
        }
        success {
            echo '✅ Tudo certo! Deploy/execução finalizada.'
        }
    }
}
