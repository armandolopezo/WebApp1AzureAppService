##### In a local environment, Azure App Service or Microsoft Learn Sandbox the following 3 commands are required 
##### to activate a Python Virtual Environment and install FLASK with PIP. PIP manages and installs PYTHON PACKAGES.
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
##### The following command creates de file "requirements.txt" with the python packages needed. 

```
pip freeze > requirements.txt
```
##### FLASK looks code in APPLICATION.PY program. In Azure App Service, by default for this kind of application the main program should be named
##### APP.PY or APPLICATION.PY (I had problems using WEB.PY program name) and the ports available are 80 and 443 instead some local
##### FLASK configurations that works with port TCP=5000 by default. 
```
cd ~/BestBikeApp
export FLASK_APP=application.py
flask run &
```
##### The following block of five export commands should be executed in AZURE CLOUD SHELL after the Azure App Service is configured with one App and with an
##### Azure Plan (unique). I used Azure App Free tier with one App, and the following code has not being tested with several apps or several azure plans working
##### or installed concurrently. 
```
export APPNAME=$(az webapp list --query [0].name --output tsv)
export APPRG=$(az webapp list --query [0].resourceGroup --output tsv)
export APPPLAN=$(az appservice plan list --query [0].name --output tsv)
export APPSKU=$(az appservice plan list --query [0].sku.name --output tsv)
export APPLOCATION=$(az appservice plan list --query [0].location --output tsv)
```
##### The command "az webapp up" update the code of the application of the Azure App Service.
```
cd ~/BestBikeApp
az webapp up --name $APPNAME --resource-group $APPRG --plan $APPPLAN --sku $APPSKU --location "$APPLOCATION"
```
##### My published Azure WEb page is shown below, and it is redirected to MEDIATECH.COM.EC  
```
http://mediatech-c0h7bjatg8bwb2ex.eastus2-01.azurewebsites.net
```
<span style="color: blue;"> I learned that Azure App Service uses the following layers for a Python Web App with Flask: .</span>
##### I learned that Azure App Service uses the following layers for a Python Web App with Flask: 
##### 1) Ubuntu (or other Linux Distro)  2) Docker.  3) Python.  4) Virtual Python Environment.  5) Flask  6) NGINX  7) Gunicorn
##### NGINX act as reverse proxy server, load balancer, content cache server, web server for Static clients, can manage slow connections,
##### other SSL/HTTP/HTTPS features, protection de DDOS attacks and can PASS DYNAMIC WEB CONTENT to GUNICORM while NGINX manages STATIC WEB CONTENT
