cd tool
mkdir backend_flask
cat ./server.py > app.py
mv ./app.py ./backend_flask

create-react-app frontend_react
cd frontend_react
tail -n +2 package.json > newPack.json
rm -f package.json
echo "{" > package.json
echo '  "proxy":"http://localhost:5000/",' >> package.json
cat newPack.json >> package.json
cd src
cat ../../app.js > App.js
cd ../../
mkdir Project
mv frontend_react backend_flask Project
zip -r React_Flask.zip Project
rm -rf Project