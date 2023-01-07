TBD:
 - Build and install with _wheel_
 - Cleanup obsolete images
 - How to update the app

## Install the app and launch server

```
curl -fLO https://github.com/aautio/slider-gallery/archive/refs/heads/main.zip
unzip main.zip
mv slider-gallery-main/* ./
rm -rf slider-gallery-main main.zip

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

pip install waitress
waitress-serve --call 'flaskr:create_app'
```

## Set cronjob to capture images

```
mkdir -p static
crontab crontab.example
```
