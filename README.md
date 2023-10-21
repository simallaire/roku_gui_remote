# roku_gui_remote
Simple Qt6 UI replicating a simple remote control for Roku TVs

## Getting started
```
pipenv install
pipenv shell
python app.py --host [Roku_IP]
```

## Modifiy UI
Make modifications with Qt6 Designer and then compile qt6 ui file with this command:
`pyuic6 remote.ui -o remote.py`

