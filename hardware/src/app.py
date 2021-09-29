import eel
from utils import log, is_raspberry

def start_headless():
    # Development servers does not need to start a chromium instance
    # go to https://localhost:8000/
    log("[ Headless mode ]")
    eel.start(
        'index.html',
        mode=None,
        host='0.0.0.0'
    )

def start_with_client():
    log("[ Client mode ]")
    eel.start(
        'index.html',
        mode='chrome',
        host='0.0.0.0',
        cmdline_args=[
            '--window-size=480,320',
            '--window-position=0,0',
            '--start-fullscreen',
            '--disable-features=Translate',
            '--kiosk'
        ]
    )

if __name__ == '__main__':
    log("Starting web server...")
    eel.init('web')
    import web # Load eel exposed functions
    log("Web server started on http://localhost:8000/")

    if is_raspberry():
        start_with_client()
    else:
        start_headless()
        
    log("Web server terminated")
