Project Title

CI/CD Deployment of Flask Backend & Express Frontend on AWS EC2 using Jenkins

 Project Description

This project demonstrates the deployment of a Flask backend application and an Express frontend application on a single Amazon EC2 instance. A CI/CD pipeline is implemented using Jenkins to automate code deployment, dependency installation, and application restart upon every GitHub push using webhooks.

Architecture Overview
Developer → GitHub → Webhook → Jenkins → EC2 Deployment → Live Apps


Applications:

• Flask Backend → Port 5000
• Express Frontend → Port 3000

Both hosted on same EC2 instance.

 AWS EC2 Setup
Steps Performed

Launched Ubuntu EC2 instance (Free Tier).

Configured Security Group inbound rules:

Port	Purpose
22	SSH
8080	Jenkins
5000	Flask
3000	Express
80	HTTP

Connected via SSH.

 Installed Dependencies

Installed required software:

sudo apt update

# Python
sudo apt install python3 python3-pip python3-venv -y

# Node.js
sudo apt install nodejs npm -y

# Git
sudo apt install git -y

# Jenkins
sudo apt install jenkins -y

# PM2
sudo npm install -g pm2

Flask Application Deployment
Steps
git clone https://github.com/suneelp300/flask-cicd.git
cd flask-cicd

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pm2 start app.py --name flask-app --interpreter python3
pm2 save

Access URL
http://<EC2-Public-IP>:5000

 Express Application Deployment
Steps
git clone https://github.com/suneelp300/express-app.git
cd express-app

npm install

pm2 start npm --name express-app -- start
pm2 save

Access URL
http://<EC2-Public-IP>:3000

 Jenkins CI/CD Setup
Installed Plugins

• Git Plugin
• Pipeline Plugin
• NodeJS Plugin
• Python Plugin

 Flask Jenkins Pipeline
Jenkinsfile
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Restart Flask App') {
            steps {
                sh '''
                pm2 restart flask-app || \
                pm2 start app.py --name flask-app --interpreter python3
                pm2 save
                '''
            }
        }

    }
}

 Express Jenkins Pipeline
Jenkinsfile
pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/suneelp300/express-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                npm install
                '''
            }
        }

        stage('Restart Express App') {
            steps {
                sh '''
                pm2 restart express-app || \
                pm2 start npm --name "express-app" -- start
                pm2 save
                '''
            }
        }

    }
}

 GitHub Webhook Integration

Webhook configured to trigger Jenkins automatically on every push.

Webhook URL
http://<EC2-Public-IP>:8080/github-webhook/

Events Enabled

• Push Events

 CI/CD Workflow

Developer pushes code to GitHub.

GitHub triggers Jenkins webhook.

Jenkins pulls latest code.

Installs dependencies.

Restarts applications via PM2.

Updated app goes live automatically.

 Screenshots Included

• EC2 Instance running
• Flask app live (Port 5000)
• Express app live (Port 3000)
• PM2 process list
• Jenkins pipeline success (Flask)
• Jenkins pipeline success (Express)
• Console output logs
• Webhook trigger proof

 GitHub Repository Links

Flask Repo:

https://github.com/suneelp300/flask-cicd


Express Repo:

https://github.com/suneelp300/express-app

 Project Outcome

• Successfully deployed Flask & Express apps.
• Hosted both on single EC2 instance.
• Automated deployment using Jenkins.
• Implemented webhook-based CI/CD.
• Achieved zero-manual deployment workflow.

 Technologies Used

• AWS EC2
• Python / Flask
• Node.js / Express
• Jenkins
• GitHub
• PM2
• Linux (Ubuntu)

 Conclusion

This project demonstrates practical implementation of CI/CD by integrating GitHub, Jenkins, and AWS EC2 to automate full-stack application deployment. It ensures faster delivery, reduced manual effort, and reliable production updates.
