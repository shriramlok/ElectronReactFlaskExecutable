# ElectronReactFlaskExecutable

### Electron+React

First do, cp app

To run electron app 
```
yarn electron-dev
```
To create executable , (with electron-builder the resulting installer can be of any specified system)
```
yarn electron-pack
```
Above creates an executable 
-- scripts can be changed from package.json 
-- don't know why we the "build": in package.json. 

## Flask+pyinstaller

After cd flask

Flask server can be run in development mode by running the following command in the folder containing app.py
```
flask run 
```
To create the installer"-
```
pip install pyinstaller
```
```
pyinstaller -F apps.py
```
('-F' creates a single file executable) 
