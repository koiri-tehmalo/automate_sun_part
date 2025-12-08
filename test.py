from pywinauto.application import Application
import time

WINDOW_TITLE = ".*Riposte POS Application.*"

app = Application(backend="uia").connect(title_re=WINDOW_TITLE, timeout=10)
win = app.top_window()
win.set_focus()

print("\n=========== SCANNING ALL EDIT BOXES ===========\n")

elements = win.descendants(control_type="Edit")

if not elements:
    print("ไม่เจอ Edit เลยในหน้านี้!!")

for i, elm in enumerate(elements):
    print(f"\n--- Edit #{i+1} ---")
    try:
        print("Name/title :", elm.window_text())
    except:
        print("Name/title : [อ่านไม่ได้]")

    try:
        print("Auto_id    :", elm.element_info.auto_id)
    except:
        print("Auto_id    : [อ่านไม่ได้]")

    try:
        print("ControlType:", elm.element_info.control_type)
    except:
        print("ControlType: [อ่านไม่ได้]")

    try:
        print("ClassName  :", elm.element_info.class_name)
    except:
        print("ClassName  : [อ่านไม่ได้]")

    try:
        rect = elm.rectangle()
        print("Rect       :", rect)
    except:
        print("Rect       : [อ่านไม่ได้]")

print("\n=========== DONE ===========\n")
