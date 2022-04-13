import tkinter as tk
from tkinter import *
import pyperclip
import math
from tkinter.messagebox import *
from tkinter import messagebox
import os


""" Create Tkinter """
root = Tk()
root.geometry("800x650+30+30") 
root.resizable(width=FALSE, height=FALSE)
root.title("Artium kot")


""" options 1 in button radio """
strChoose1 = StringVar()

""" options 2 in button radio """
strChoose2 = StringVar()





""" we need to refresh screen(tkinter) when we dont have place """
def Exit_Screen_cleaning():
   
    result=askquestion("TextEditor1.0","Exit(Yes) Or Screen cleaning - for more place(No) ?")
    
    if (result=="yes"):
        close()
        
    if (result=="no"):
        root.destroy()
        os.popen("New_work_artium.py")





""" close the program """
def close():
    root.destroy()

   



""" check if mmeasge or key was good """
def Check(msg,key):
    

    """ check if text was digit and key was letter """
    if msg.isdigit() and key.isalpha():
        res["text"]= "erorr input was invalid ! text need letter and key need digit "
        return 0


    """ if len msseage was 0 and len key was 0 """
    if len(msg) == 0 and len(key) == 0:
        res["text"]= "don't have message and key please input !"
        return 0

    
    """ if key was letter """
    if key.isalpha():
        res["text"]= "your key was Letter ! not Good you need digit "
        return 0


    """ if len msseage was 0 """
    if len(msg) == 0:
        res["text"]= "don't have message please input !"
        return 0


    """ if len key was 0 """
    if len(key) == 0:
        res["text"]= "don't have key please input !"
        return 0


    """ if message was digit input """
    if msg.isdigit():
        res["text"]= "your message was Digit input ! need Letter "
        return 0





""" check input for brute fruce """
def Check_input_brute_fruce(msg,key):


    """ if len key was more 1 """
    if len(key) >= 1:
        res["text"]= "you don't need key for brute force  !"
        return 0
    
    """ if message was digit input """
    if msg.isdigit():
        res["text"]= "your message was Digit input ! need Letter "
        return 0

    """ if len msseage was 0 """
    if len(msg) == 0:
        res["text"]= "don't have message please input !"
        return 0



    

""" to do encrypt """
def encryptMessage(msg,key):
   
    rail = [['\n' for i in range(len(msg))]
                  for j in range(key)]
      
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(msg)):
          
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
          
        rail[row][col] = msg[i]
        col += 1
          
        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        
        for j in range(len(msg)):
            
            if rail[i][j] != '\n':
                result.append(rail[i][j])
                
    return("" . join(result))
      





""" to do decrypt """
def decryptMessage(cipher,key):

    rail = [['\n' for i in range(len(cipher))] 
                  for j in range(key)]
      
    dir_down = None
    row, col = 0, 0
      
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
          
        rail[row][col] = '*'
        col += 1
          
        if dir_down:
            row += 1
        else:
            row -= 1
              
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    
    for i in range(len(cipher)):
          
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
              
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
              
        if dir_down:
            row += 1
        else:
            row -= 1
            
    return("".join(result))




""" to do brute froce , show result in new window show in screen """
def brute_force_show_in_screen(msg):

    #msg = 'guvf vf zl frperg zrffntr.'

    """ create new window for to show the result """
    newWindow = Tk()
    newWindow.title("brute_force")
    newWindow.geometry("320x500")
    newWindow.resizable(width=FALSE, height=FALSE)
    newWindow.title("brute froce window")
    
    T = Text(newWindow, height = 26, width = 52)
    T.pack()

    """ button exit in new window """
    exit_btn = tk.Button(newWindow,bg="grey",fg="white",font="none 10",text = "Exit",command =newWindow.destroy).pack()
    
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for key in range(len(letters)):


        translated = ''

        for symbol in msg:

             if symbol in letters:

                num = letters.find(symbol) # get the number of the symbol

                num = num - key


                if num < 0:

                  num = num + len(letters)
              
              
                translated = translated + letters[num]


             else:
                translated = translated + symbol

        T.insert(tk.END, 'key #')
        T.insert(tk.END, key)
        T.insert(tk.END,' ' )
        T.insert(tk.END, translated)
        T.insert(tk.END,'\n')




""" brute froce , save in file the result """
def brute_force_save_file(message):
    
    """ save file """
    file_save_res=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
    f_r = open(file_save_res,'w')
 
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for key in range(len(letters)):

        translated = ''

        for symbol in message:

             if symbol in letters:

                num = letters.find(symbol) # get the number of the symbol

                num = num - key

                if num < 0:

                  num = num + len(letters)
                        
                translated = translated + letters[num]

             else:
                translated = translated + symbol
                
        f_r.write("key = " + str(key) + " " + str(translated + "\n"))

    f_r.close()
  



""" options to result for brute force """     
def Options_show_result_brute_force():

 
    msg = input_Text.get("1.0", "end-1c")
    key = input_Key.get("1.0", "end-1c")

    """ check input """
    check = Check_input_brute_fruce(msg,key)  
    if check == 0:
        return

    result=askquestion("TextEditor1.0","Show result in File(Yes) Or show in screen(No) ?")
    
    if (result=="yes"):
        brute_force_save_file(str(msg))
        
        """ show in label """
        res["text"]= "you save File now Decryption (brute_force) !( text )"
   
    if (result=="no"):
        messagebox.showinfo("showinfo", "open new window for show result brute force  !")
        brute_force_show_in_screen(msg)
        
        



""" create encryption , chiose where i want save result in file or show in screen """
def Options_show_result_EncryptMessage():

  
    """ return with function result """
    msg = input_Text.get("1.0", "end-1c")
    key = input_Key.get("1.0", "end-1c")
    
    """ check input """
    check = Check(msg,key)    
    if check == 0:
        return

    """ return result with fuction """
    show = encryptMessage(str(msg),int(key))

    """ message box yes or no """
    result=askquestion("TextEditor1.0","Show result in File(Yes) Or show in screen(No) ?")
    
    """ if we want save at file-result and key """
    if (result=="yes"):
        file_save_res=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
        f_r = open(file_save_res,'w')
        f_r.write(show)
        f_r.close()
        
        """ save key in file """
        save_key_to_file()

        """ show in label """
        res["text"]= "you save File now Encryption !( text , key )"

        
    """ if we chiose no , we show in screen the result """      
    if (result=="no"):
        res["text"]= show
        


  

""" create Decrypt , chiose where i want save result in file or show in screen """
def Options_show_result_DecryptMessage():


    """ return with function result """
    msg = input_Text.get("1.0", "end-1c")
    key = input_Key.get("1.0", "end-1c")

    """ check input """
    check = Check(msg,key) 
    if check == 0:
        return
    
    
    """ return result with fuction """
    show=decryptMessage(str(msg),int(key))
    

    """ message box yes or no """
    result=askquestion("TextEditor1.0","Show result in File(Yes) Or show in screen(No) ?")

    """ if we want save at file-result and key """
    if (result=="yes"):
        file_save_res=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
        f_r = open(file_save_res,'w')
        f_r.write(show)
        f_r.close()

        """ save key in file """
        save_key_to_file()

        """ show in label """
        res["text"]= "you save File now Decryption !( text , key )"

        
    """ if we chiose no , we show in screen the result """         
    if (result=="no"):
        res["text"]= show





""" here we save the key(string) in file, for when we wont to read from file and to do encrypt or decrypted we need key """
def save_key_to_file():
    
      messagebox.showinfo("showinfo", "you need save the Key for the following steps!! ")
      file_Save_Key=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
      f_k = open(file_Save_Key,'w')
      key = str(input_Key.get("1.0", "end-1c"))
      f_k.write(key)
      f_k.close()





""" read from file text and key and send to the function encrypt to see the result """
def Read_from_File_text_and_key_EncryptMessage():

    messagebox.showinfo("showinfo", "now you need take the Text from File ")

    """ read from file message """
    file_take_text=root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    f_t = open(file_take_text,'r')
    msg = f_t.read()

    messagebox.showinfo("showinfo", "now you need take the Key from File ")
    
    """ read from file key """
    file_take_key=root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    f_k = open(file_take_key,'r')
    key = f_k.read()

    """ check input """
    check = Check(msg,key)  
    if check == 0:
        return
    
    
    """ take the result from fuction encryptMessage_use_with_file and input to function key and text from file """
    e_result=encryptMessage(str(msg),int(key))

    """ message box yes or no """
    result=askquestion("TextEditor1.0","Show result in File(Yes) Or show in screen(No) ?")

    """ if we want save at file-result """
    if (result=="yes"):
        file_save_res=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
        f_r = open(file_save_res,'w')
        f_r.write(e_result)
        f_r.close()
        res["text"]= "you save File now Encryption !( text )"

    """ if we chiose no , we show in screen the result """         
    if (result=="no"):
        res["text"]= e_result





""" read from file text and key and send to the function encrypt to see the result """
def Read_from_File_text_and_key_DecryptMessage():
    
    messagebox.showinfo("showinfo", "now you need take the Text from File ")

    """ read from file message """
    file_take_text=root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    f_t = open(file_take_text,'r')
    msg = f_t.read()

    messagebox.showinfo("showinfo", "now you need take the Key from File ")
    
    """ read from file key """
    file_take_key=root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    f_k = open(file_take_key,'r')
    key = f_k.read()

    """ check input """
    check = Check(msg,key)    
    if check == 0:
        return

    
    """ take the result from fuction encryptMessage_use_with_file and input to function key and text from file """
    e_result=decryptMessage(str(msg),int(key))

    """ message box yes or no """
    result=askquestion("TextEditor1.0","Show result in File(Yes) Or show in screen(No) ?")

    """ if we want save at file-result """
    if (result=="yes"):
        file_save_res=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
        f_r = open(file_save_res,'w')
        f_r.write(e_result)
        f_r.close()
        res["text"]= "you save File now Decryption !( text )"

        
    """ if we chiose no , we show in screen the result """         
    if (result=="no"):
        res["text"]= e_result        





""" read from file text and key and send to the function brute_force to see the result """
def Read_from_File_text_brute_force():   

    messagebox.showinfo("showinfo", "now you need take the Text from File ")

    """ read from file message """
    file_take_text=root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    f_t = open(file_take_text,'r')
    msg = f_t.read()


    """ check input from file """
    if msg.isdigit() or len(msg)==0 :
        
        res["text"]= "text was digit or length text was null  !"
        return
    
    
    """ message box yes or no """
    result=askquestion("TextEditor1.0","Show result in File(Yes) Or show in screen(No) ?")

    """ if we want save at file-result """
    if (result=="yes"):
        brute_force_save_file(msg)
        res["text"]= "you save File now Decryption (brute_force) !( text )"

        
    """ if we chiose no , we show in screen the result """         
    if (result=="no"):
        messagebox.showinfo("showinfo", "open new window for show result brute force  !")
        brute_force_show_in_screen(msg)



    


""" actions with listBox """
def list_box_options(item):

    w = item.widget
    index = int(w.curselection()[0])
    
    
    if index == 0:
        options_Radio_Result_option_2()




   
""" actions with radio Button for option 2 """
def options_Radio_Result_option_2():
   
    strChoose2.set("some text")
    rb1=Radiobutton(root, text="Encryption ( Text , Key )", variable=strChoose2, value="Encryption",command=Options_show_result_EncryptMessage)#  הצפנה
    rb1.pack()
    rb2=Radiobutton(root, text="Deciphering ( Text , Key )", variable=strChoose2, value ="Deciphering",command=Options_show_result_DecryptMessage)# פענוח
    rb2.pack()
    rb3=Radiobutton(root, text="brute force (Not need Key)", variable=strChoose2, value ="brute force",command=Options_show_result_brute_force)# ניסיון לפענוח ללא מפתח
    rb3.pack()

    """ button to clear the screen when dont have place """
    button_Clean = tk.Button(root,bg="grey",fg="white",font="none 10",text = "Exit / Screen cleaning (for more place)",command = Exit_Screen_cleaning)
    button_Clean.pack()





""" actions with radio Button for option 1 take with file text and key """
def options_Radio_Result_option_1():
   
    strChoose1.set("some text")
    rb1=Radiobutton(root, text="Encryption ( Text , Key ) ( take File Deciphering )", variable=strChoose1, value="Encryption",command=Read_from_File_text_and_key_EncryptMessage)#  הצפנה
    rb1.pack()
    rb2=Radiobutton(root, text="Deciphering ( Text , Key ) ( take File Encryption )", variable=strChoose1, value ="Deciphering",command=Read_from_File_text_and_key_DecryptMessage)# פענוח
    rb2.pack()
    rb3=Radiobutton(root, text="brute force (Not need Key) ( take File Encryption )", variable=strChoose1, value ="brute force",command=Read_from_File_text_brute_force)# ניסיון לפענוח ללא מפתח
    rb3.pack()




""" title """
lbl_title_Option = tk.Label(root,pady=10,font="none 18",text='Select the option you need :')
lbl_title_Option.pack()

lbl_title_Option_1 = tk.Label(root,font="none 12",text='option 1  -  here you Take a Decrypted or Encrypted with File !')
lbl_title_Option_1.pack()

lbl_title_choise_1 = tk.Label(root,font="none 9",text='Choise what you need to do decrypted or encrypted  :')
lbl_title_choise_1.pack()

""" function radio button for option 1 read from file """
options_Radio_Result_option_1()

len_Space = tk.Label(root,font="none 12",text='________________________________________________________________________________')
len_Space.pack()

lbl_title_Option_2 = tk.Label(root,font="none 12",text='option 2  -  here you input text and key for your actions !')
lbl_title_Option_2.pack()





""" Title input text """
lbl = tk.Label(root,font="none 9",text='Please Enter Text  : ')
lbl.pack()

input_Text=tk.Text(root,height = 5, width=40)
input_Text.pack()

""" Title input key(string) """        
lbl1 = tk.Label(root,font="none 9",text='Please Enter Key  : ')
lbl1.pack()

input_Key=tk.Text(root,height = 5, width=40)
input_Key.pack()


lbl_title_choise_2 = tk.Label(root,font="none 9",text='Choise what you need  :')
lbl_title_choise_2.pack()

lb_options = Listbox(root,height=1,width=50,font="none 9")
lb_options.insert(0, '           (1)  performing encryption or decryption operations')
lb_options.pack()

lb_options.bind('<<ListboxSelect>>',list_box_options)



lb_title_result = tk.Label(root,font="none 12",pady=7,text='Result Screen  :')
lb_title_result.pack()


""" show result """
res=Label(root,bg="grey",fg="white",font="none 9", width=65,height = 1)
res.pack()



root.mainloop()
