pipeline {
    agent any

    environment {
        APP_DIR = "/home/ubuntu/flask-app"
        VENV_DIR = "/home/ubuntu/flask-app/venv"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/suneelp300/flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd $APP_DIR
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Restart Flask App') {
            steps {
                sh '''
                pm2 restart flask-app || \
                pm2 start app.py --name flask-app --interpreter python3
                '''
            }
        }
    }
}
