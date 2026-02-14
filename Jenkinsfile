pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/python -m pip install --upgrade pip
                venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Restart Flask App') {
            steps {
                sh '''
                pkill -f app.py || true
                nohup venv/bin/python app.py > flask.log 2>&1 &
                '''
            }
        }

    }
}

