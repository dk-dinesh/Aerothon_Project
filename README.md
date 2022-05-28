# Aerothon_Project
![Screenshot from 2022-05-28 09-42-03](https://user-images.githubusercontent.com/55187704/170809396-f1c70789-5215-4699-995e-3fc6d3a1eb49.png)

A tool which can generate template files for particular combination chosen for Backend and Frontend Frameworks

User will be allowed to input a Frontend framework and a backend framework of his/her choice after processing when someone click the Submit it will download the required template
files. Ex- React and Flask

## How to run this project:

First clone the project.<br />
```
cd Aerothon_Project
pip install -r requirements.txt
python manage.py runserver
```

Now, server will start running at localhost:8000<br />
go to Tool section<br />
![Screenshot from 2022-05-28 09-42-34](https://user-images.githubusercontent.com/55187704/170809421-350191eb-727a-44ef-b977-34108e001fbb.png)

Select frontend and backend framework<br />
Click submit<br />
Wait for 1 min, integrated files will be downloaded in zip format.<br />

Extract the zip
```
export MESSAGE="Hello World"   ==> This message will be passed from backend to frontend.
cd Poroject
cd backend_flask
python app.py   ==> This will start the flask server
cd..
cd frontend_react
npm start       ==> This will start the react server, and above message will be shown in browser
```
## Our Team
![Screenshot from 2022-05-28 09-42-54](https://user-images.githubusercontent.com/55187704/170809459-b93c5a93-12fb-47fc-a789-faaa3d8c23be.png)
