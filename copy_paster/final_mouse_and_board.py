from  pynput import mouse
from  pynput import keyboard
def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    if pressed:print(f"pressed at {x,y}")
    else :
        print(f"Released at {x,y}")
        return m_listener.stop()
    # print('{0} at {1}'.format<
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))

    if not pressed:
        # Stop listener
        return False

def on_press(key):
    if key==keyboard.Key.ctrl_l:
        print("starting mouse listner")
        m_listener.start()

    else:
        print("wrong key")
        return False


# Collect events until released
m_listener= mouse.Listener(on_click=on_click)
with keyboard.Listener(on_press=on_press) as klisetner:
    klisetner.join()
