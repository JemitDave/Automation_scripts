from pynput.keyboard import Key, Listener
'''<qwwsxfdxdcs   < 	   ī                     '''
def on_press(key):
    if key==Key.ctrl_l:
        print('ctrl is pressed')
        #enter screenchot Code

    elif key==Key.tab:
        print('tab is pressed')
        #copy paste code
    else:pass
    # print('{0} pressed'.format(
    #     key))

def on_release(key):
    # print('{0} release'.format(
    #     key))
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
