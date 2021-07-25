import tkinter as tk 
from tkinter.messagebox import showinfo
import random as rn
import os 
import time
from PIL import ImageTk,Image

skor_counter=0
word_counter=0
clock=60

class Myapp(tk.Frame):
	def __init__(self,window):
		tk.Frame.__init__(self,master=window)
		self.skor_counter=skor_counter
		self.window=window
		self.window.title('Tenfinger App')
		self.window.iconbitmap("C:/Users/46mus/Desktop/icons/keyboard.ico")
		self.window.geometry("800x450+350+200")
		self.window.resizable(width=False,height=False)
		self.Username=tk.StringVar()
		self.Password=tk.StringVar()
		self.username='mustafa'
		self.password='kurt'
		self.window.config(bg='green')
		self.enter_page()
		self.window.mainloop()
	def login_button(self,event=''):
		
		if str(self.Username.get())==self.username and str(self.Password.get())==self.password:
			self.main_page()
		else:
			showinfo('Tenfinger App','Giris bilgileri yanlis')
	def update(self,ind):
		frame=self.frames[ind]
		global skor_counter
		global word_counter
		ind+=1
		if ind <30:
			self.label.configure(image=frame)
			self.window.after(10,self.update,ind)
		if ind>=30:
			self.skor_txt=tk.Label(self.mp_frame,bg='#aaffff',font='arial 12 bold')
			self.label.destroy()
			self.skor_txt.pack()
			#dogru yazilan kelime/topman yazilan kelime
			self.mp_girditxt.delete(1.0,'end')
			if skor_counter !=0 or word_counter!=0:
				skor=(skor_counter/(skor_counter+word_counter))
				skor=int(skor*100)
			else:
				skor=0
			#print('% '+str(skor))
			self.skor_txt['text']='Accuracy: %' + str(skor)
			self.skor_txt['text'] +='\nCorect Words: '+str(skor_counter)
			self.skor_txt['text'] +='\nWrong Words: '+str(word_counter)
			self.mp_yenilebutton.focus()
			self.mp_girditxt['state']='disabled'
			self.mp_yenilebutton['state']='normal'
			# self.mp_girditxt.bind('<control-r>,',self.main_page)
			# self.skor_txt.unpack()
	def update_clock(self):
		global clock
		if clock !=0:
			clock-=1
			self.window.after(1000,self.update_clock)
			print(clock)
			self.mp_clockLabel['text']="0:"+str(clock)
		else:
			self.mp_yenilebutton['state']='normal'
			self.mp_clockLabel['text']='1:00'
			self.label=tk.Label(self.mp_frame)
			self.label.pack()
			self.window.after(0,self.update,0)
			self.frames = [tk.PhotoImage(file='C:/Users/46mus/Desktop/Pyhtonworkstation/project_0/frames/frames9/frame-%i.png'%(i)) for i in range(30) ]
	def yenile(self,event=''):
		self.skor_txt.destroy()
		self.txt_insert()
		global clock
		global skor_counter
		global word_counter
		word_counter=0
		skor_counter=0
		clock=60
		self.mp_clockLabel['text']='1:00'
		self.window.after(0,self.update_clock)		# self.mp_girditxt.delete(1.0,'end')
		self.mp_girditxt['state']='normal'
		self.mp_girditxt.focus()
		
		
		self.mp_yenilebutton['state']='disabled'
	def txt_control(self,event):
		
		girdilist=self.mp_girditxt.get('1.0','end-1c').split(' ')
		txtboxlist=self.words
		counter=str(girdilist[-1])
		
		global skor_counter
		global word_counter
		global clock 
		if clock ==60:
			self.window.after(0,self.update_clock)
		print(skor_counter)

		flagBul='bulunmadi'
		for i in self.words:

			if  counter==i:
				print(i)
				print(counter)
				print('girdi')
				skor_counter+=1

				flagBul='bulundu'
				self.mp_wordtxt.config(fg='green')
			elif  i==txtboxlist[-1] and flagBul=='bulunmadi':
				word_counter+=1
				self.mp_wordtxt.config(fg='red')
				#print('yanlis',word_counter,skor_counter)
				self.mp_wordtxt.tag_configure("bu", foreground="#ff6666")
		if self.words[-1]==counter:
			self.txt_insert()
		# 	self.mp_yenilebutton['state']='normal'
		# 	print('elif')
		# 	self.label=tk.Label(self.mp_frame)
		# 	self.label.pack()
		# 	self.window.after(0,self.update,0)
		# 	self.frames = [tk.PhotoImage(file='C:/Users/46mus/Desktop/Pyhtonworkstation/project_0/frames/frames9/frame-%i.png'%(i)) for i in range(30) ]
	def txt_insert(self):

		print('tex ekle')
		self.wordsfile=open("D:/Desktop/MyPythonPrograms/Klavye/words.txt",'r')
		wordlist=self.wordsfile.read()
		wordlist=wordlist.split(' ')
		self.s=set()
		for i in range(0,50):
			self.s.add(wordlist[rn.randint(0,len(wordlist)-1)])
			# self.words.append(' ')
		self.wordsfile.close()	
		self.words=list(self.s)
		self.mp_wordtxt['state']='normal'
		self.mp_wordtxt.delete(1.0,'end')
		self.mp_wordtxt.insert('end',self.words)
		self.mp_wordtxt['state']='disabled'
	def main_page(self,event=''):

		global skor_counter
		global word_counter
		word_counter=0
		skor_counter=0
		self.mp_frame=tk.Frame(self.window,bg='#aaffff')
		self.mp_wordtxt=tk.Text(self.mp_frame,bg='black',fg='green',height=4,width=90,font='Arial 12 bold')
		self.txt_insert()
		
		self.mp_wordtxt['state']='disabled'
		
		self.mp_girditxt=tk.Text(self.mp_frame,bg='#dcdcdc',height=4,width=90,fg='black',font='Arial 12 bold')
		
		self.mp_girditxt.bind('<space>',self.txt_control)
		self.mp_girditxt.bind('<BackSpace>',lambda a :'break' )
		self.mp_girditxt.bind('<Control-w>',self.app_cikis)
		self.mp_girditxt.focus()
		self.photo=tk.PhotoImage(file="C:/Users/46mus/Desktop/icons/Button1.png")
		self.mp_yenilebutton=tk.Button(self.mp_frame,image=self.photo,width=60,height=60,command=self.yenile,bd=0,bg=self.mp_frame['bg'])
		self.mp_yenilebutton.bind('<Control-r>',self.yenile)
		self.mp_yenilebutton.bind('<Control-w>',self.app_cikis)
		self.mp_yenilebutton['state']='disabled'
		self.mp_clockLabel=tk.Label(self.mp_frame,font='Times 12 bold',
			width=6,height=2,bg='grey',text='1:00',fg='white')

		
		self.menubar=tk.Menu(self.window)
		dropdownmen=tk.Menu(self.menubar,tearoff=0)
		dropdownmen.add_command(label='Cikis',command=self.buton_cikis)

		dropdownmen1=tk.Menu(self.menubar,tearoff=0)
		dropdownmen1.add_command(label='text insert')
		self.menubar.add_cascade(label='File',menu=dropdownmen)
		self.menubar.add_cascade(label='Edit',menu=dropdownmen1)
		
		self.window.config(menu=self.menubar)



		#========================================================
		
		self.mp_wordtxt.pack(side='top',pady=10,padx=10)
		

		self.mp_girditxt.pack(padx=10)
		self.mp_yenilebutton.pack(anchor='e',padx=5)
		self.mp_clockLabel.pack(anchor='e',padx=10)
		#self.skor_txt.pack(side='top',pady=10,padx=10)
		# self.mp_wordtxt.grid(row=0,column=0,columnspan=2,padx=15,pady=10)
		# self.mp_girditxt.grid(row=1,column=0,columnspan=1)
		# self.mp_yenilebutton.grid(row=1,column=1,columnspan=1)
		self.mp_frame.pack(fill='both',expand=True)
		
		self.et_frame.destroy()
	def app_cikis(self,event=''):
		self.window.destroy()
	def buton_cikis(self,event=''):
		self.menubar.destroy()
		self.mp_yenilebutton.destroy()
		self.mp_frame.destroy()

		self.enter_page()
	def register_page(self):
		pass
	def enter_page(self):

		self.et_frame=tk.Frame(self.window,bg='black')
		self.et_welcome=tk.Label(self.et_frame,
			text='Welcome The Tenfinger App',fg='lime',bg='blue')
		
		#=======================================
		self.et_Username=tk.Label(self.et_frame,text="Username")
		self.et_username=tk.Entry(self.et_frame,textvariable=self.Username)
		self.et_username.delete(0,'end')
		self.et_username.insert(0,'mustafa')
		self.et_Password=tk.Label(self.et_frame,text="Password")
		self.et_password=tk.Entry(self.et_frame,textvariable=self.Password)
		self.et_password.delete(0,'end')
		self.et_password.insert(0,'kurt')
		self.et_username.bind('<Control-w>',self.app_cikis)
		self.et_password.bind('<Return>',self.login_button)

		#========================================
		self.et_loginbutton=tk.Button(self.et_frame,text='Login',padx=50,command=self.login_button)
		self.et_loginbutton.bind('<space>',lambda a:'break')
		self.et_registerbutton=tk.Button(self.et_frame,text='Register',padx=45)
		#========================================
		self.et_welcome.grid(row=0,columnspan=2,padx=10,pady=10)
		self.et_Username.grid(row=1,column=0,padx=5,pady=5)
		self.et_username.grid(row=1,column=1,padx=5)
		self.et_Password.grid(row=2,column=0,padx=5,pady=5)
		self.et_password.grid(row=2,column=1,padx=5)
		self.et_loginbutton.grid(row=3,columnspan=2,padx=15,pady=5)
		self.et_registerbutton.grid(row=4,columnspan=2,padx=15,pady=5)
		self.et_username.focus()
		self.et_frame.pack(pady=100)
def main():

	root=tk.Tk()
	app=Myapp(root)
if __name__=="__main__":
	main()





	
# from tkinter import *
# import time
# import os
# root = Tk()
# root.config(bg='green')
# myframe=Frame(root,bg='white')



# label = Label(myframe)
# label.pack(pady=100)
# myframe.pack(expand=True,fill='both')

# root.after(0, update, 0)
# root.mainloop()
# from tkinter import *
# import time
# import os
# root = Tk()

# frames = [PhotoImage(file='mygif.gif',format = 'gif -index %i' %(i)) for i in range(100)]

# def update(ind):

#     frame = frames[ind]
#     ind += 1
#     label.configure(image=frame)
#     root.after(100, update, ind)
# label = Label(root)
# label.pack()
# root.after(0, update, 0)
# root.mainloop()