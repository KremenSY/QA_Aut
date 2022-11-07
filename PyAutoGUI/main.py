import pyautogui
import pyperclip
from settings import *
import time

def get_result():
    pyautogui.click(GUI_POS['field'], button='right')
    pyautogui.move(10,10)
    pyautogui.click()
    result=pyperclip.paste()
    return result

def test_plus(x,y,z):
    print('test_plus')
    pyautogui.click(GUI_POS['btn_c'])
    l=len(f"{x}")
    for digit in f"{x}":
        #print (digit)
        if digit==".":
            pyautogui.click(GUI_POS[f'btn_point'])
        else:
            pyautogui.click(GUI_POS[f'btn_{digit}'])
    pyautogui.click(GUI_POS['btn_plus'])
    for digit in f"{y}":
        #print (digit)
        if digit==".":
            pyautogui.click(GUI_POS[f'btn_point'])
        else:
            pyautogui.click(GUI_POS[f'btn_{digit}'])
    pyautogui.click(GUI_POS['btn_equals'])
    actual_result=f"{get_result()}".replace(",", ".") # for separator=,
    expected_result=f"{z}"
    # print(actual_result==expected_result)
    assert(actual_result==expected_result), f"{x}+{y}: expected={expected_result}, actual={actual_result}"
    pyautogui.click(GUI_POS['btn_c'])

test_plus(245.34,500.67,746.01)

