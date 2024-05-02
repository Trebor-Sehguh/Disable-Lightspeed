import os
import sys
import webbrowser
webbrowser.get(using='google-chrome').open(url,new=new)
and
import psutil
def close_app(app_name):
    running_apps=psutil.process_iter(['pid','name']) 

    found=False
    for app in running_apps:
        sys_app=app.info.get('name').split('.')[0].lower()

        if sys_app in app_name.split() or app_name in sys_app:
            pid=app.info.get('pid') 

            try: 
                app_pid = psutil.Process(pid)
                app_pid.terminate()
                found=True
            except: pass

        else: pass
    if not found:
        print(app_name+" not found running")
    else:
        print(app_name+'('+sys_app+')'+' closed')

close_app('Lightspeed Filter Agent')