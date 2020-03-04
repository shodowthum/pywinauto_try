from pywinauto.application import Application
from pywinauto import Desktop
from subprocess import Popen
import time

# app = Application(backend="uia").start('notepad.exe')
# dlg_spec = app.UntitledNotepad
# actionable_dlg = dlg_spec.wait('visible')
# print(dlg_spec)

# Popen('calc.exe', shell=True)
# dlg = Desktop(backend="uia").Calculator
# dlg.wait('visible')

# dlg_spec = app.window(title='Untitled - Notepad')
# print(dlg_spec)
# print(dlg_spec.wrapper_object())
# dlg_spec.wrapper_object().minimize()
# dlg_spec.minimize()

# app.window(title_re='.* - Notepad$').window(class_name='Edit')

# dlg = Desktop(backend="uia").Calculator
# dlg.window(auto_id='num8Button', control_type='Button')

# app.UntitledNotepad.menu_select("File->SaveAs")
#
# app.SaveAs.edit1.set_text("Example-utf8.txt")_
# app.UntitledNotepad
# app['Untitled - Notepad']
# print(app.Properties.print_control_identifiers())


#############################################
from pywinauto import application

app = application.Application()
# app.start("Notepad.exe")
# app.start()


# Notepad Path and Exe
program_path = r"C:\WINDOWS\system32\notepad.exe"
file_path = r"F:\python_control_Text.txt"

# Read existing notepad from path example
app = Application(backend="win32").start(r'{} "{}"'.format(program_path, file_path))

app.UntitledNotepad.draw_outline()  # Cannot use in backend="uia"

app.UntitledNotepad.menu_select("Edit -> Replace")

# read Notepad interface have what.
app.Replace.print_control_identifiers()

#Edit box insert some texts
app.Replace.edit.set_text("OKOK")
app.Replace.edit2.set_text("Test")

# Click Find Next Button
app.Replace.FindNext.click()
time.sleep(1)
app.Replace.FindNext.click()

# insert  some text
app.UntiledNotepad.Edit.type_keys("OKOK      OKOK OKOK", with_spaces=True)  # spacing in
# Click Home Buttong at Notepad, set cursor back to front for searching purpose
app.UntitledNotepad.Edit.type_keys('{VK_HOME}')

# Click Replace button.
app.Replace.Replace.click()
app.Replace.Replace.click()

app.Replace.edit.set_text("Test")
app.Replace.edit2.set_text("OKOK")

app.Replace.CheckBox0.check()
time.sleep(2)
# get properties of the item
print("This is check get details : %s", app.Replace.CheckBox0.get_properties())
print("This is check getcheckstate details : ", app.Replace.CheckBox0.get_check_state())

app.Replace.CheckBox0.uncheck()
time.sleep(2)
print("This is uncheck get details : %s", app.Replace.CheckBox0.get_properties())
print("This is uncheck getcheckstate details : ", app.Replace.CheckBox0.get_check_state())
time.sleep(3)

app.UntitledNotepad.Edit.type_keys('{VK_HOME}')

# Click ReplaceAll Button
app.Replace.ReplaceAll.click()
time.sleep(2)
# Click Cancel Button
app.Replace.Cancel.click()

app.UntiledNotepad.Edit.type_keys('{ENTER}')
app.UntiledNotepad.Edit.type_keys('{ENTER}')

time.sleep(5)

# Type Alt +F4 to close application
app.UntiledNotepad.type_keys("%{F4}")  # Alt-F4
app.Notepad.DontSave.click()




# print("edit " + str(app.Replace.Edit))
# print("edit0 " + str(app.Replace.Edit0))
# print("edit1 " + str(app.Replace.Edit1))
# print("findedit " + str(app.FindwhatEdit))


# time.sleep(3)
# app.Replace.Cancel.click()
# app.UntitledNotepad.Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)
# time.sleep(3)
# app.UntitledNotepad.menu_select("File -> Exit")
# time.sleep(3)
# # app.UntitledNotepad.DontSave.click()
