pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '"C:\\Users\\chanc\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe" install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat '"C:\\Users\\chanc\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pytest.exe"'
            }
        }
        stage('Package') {
            when {
                anyOf { branch "master"; branch "release" }
            }
            steps {
                // Use Python to zip instead of PowerShell
                bat '"C:\\Users\\chanc\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -c "import shutil; shutil.make_archive(\'sbdl\', \'zip\', \'lib\')"'
            }
        }
    }
}
