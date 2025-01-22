pipeline{
  agent any
  stages{
    stage("Build"){
      steps{
        echo "Building in progress"
        sh'''
        pip3 install -r requirements.txt
        '''
      }
    }
    stage("Test"){
      steps{
        echo "Testing in progress"
        sh'''
        python3 -m pytest -vs test_free_api.py
        '''
      }
    }
   
    }
  }
