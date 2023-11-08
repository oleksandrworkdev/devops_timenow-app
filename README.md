# Timenow app

Install nginx web server on your virtual machine and configure hosting of the timenow web app: 
- configure hosting of the static content from folder /frontend (on VM it should be stored in the folder: '/var/www/timenow-fe')
- run api manually on the VM and configure reverse proxy for it
- generate a self-signed certtificate to be used for the web site for the TLS encryption

Task requirements: 
- the web site should be available at the domain 'timenow.local' 
- the backend (API) should be available at the url 'https://timenow.local/api'
- the backend should have CORS policy configured to allow requests from the URL 'https://timenow.local'
- the site should use TLS encryption with a self-signed certificate (public key should be located at '/etc/ssl/certs/nginx-selfsigned.crt', private key should be located at '/etc/ssl/private/nginx-selfsigned.key')
- the site should have redirection from http to https
- commit the content of your nginx configuration to the file in this repository: 'configs/nginx/timenow.local'

Notes: 
- to generate a self-signed ssl certificate, you can use script, located in this repository: scripts/generate-ssl-certificate.sh
- use hosts file on your computer to test connection to the web site using domain
