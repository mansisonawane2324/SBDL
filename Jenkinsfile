pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '"C:\\Users\\chanc\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'


            }
        }
        stage('Test') {
            steps {
                 bat '"C:\Users\chanc\AppData\Local\Programs\Python\Python311\python.exe"'
            }
        }
        stage('Package') {
            when {
                anyOf { branch "master"; branch "release" }
            }
            steps {
                bat 'powershell Compress-Archive -Path lib -DestinationPath sbdl.zip -Force'
            }
        }
    }
}
