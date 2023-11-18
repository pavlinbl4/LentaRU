import os

def notification(message, title="Ready"):

    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)
