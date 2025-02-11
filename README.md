##### In a local environment or Microsoft Learn Sandbox the following 3 commands are required 
##### to activate a Python Virtual Environment and install FLASK with PIP. PIP manages and installa PYTHON PACKAGES.
```
python3 -m venv venv
source venv/bin/activate
pip install flask
```
##### I will create and work with de "BestBikeApp" directory (the following two commands)
```
mkdir ~/BestBikeApp
cd ~/BestBikeApp
```
##### I will create the code for the APPLICATION.PY program with the following block.
```
cat >application.py <<EOL
from flask import Flask, redirect
import os
app = Flask(__name__)
@app.route('/')
def page():
    return redirect('http://mediatech.com.ec/', code=301)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    print ("Running on port: ", port)
    app.run(host='0.0.0.0', port=port)
EOL
```
##### The following command creates de file "requirements.txt" with the python packages needed in a local environment. I believe this command is not needed
##### with Azure App Service ( I assume Azure loads common packages).

```
pip freeze > requirements.txt
```
