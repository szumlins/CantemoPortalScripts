#!/usr/bin/env /usr/bin/python

import os
import sys
import subprocess
import collections
from Tkinter import *

#if something is passed, validate and build array
if len(sys.argv) > 1:
	test = []
	i = 1	
	#add all CLI args to a list
	while i < len(sys.argv):
		test.append(sys.argv[i])
		i = i+1		
	
	#make sure those files are visible to the client
	filelist = []
	badlist = []
	for file in test:
		if os.path.isfile(file):
			filelist.append(file)
		else:
			badlist.append(file)
	#eliminate duplicates for speed
	filelist = list(set(filelist))
	
				
#if no paths are passed, echo out expected syntax		
else:
	print ""
	print "Please pass the path or paths to file(s) as CLI arguments to use this script"
	print ""
	sys.exit(0)

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.title = Label(frame, text=str(len(filelist)) + " file(s)")
		self.title.pack(side=TOP)
		
		if(len(filelist) == 1):
			self.rf = Button(frame, text="Reveal In Finder", fg="blue", command=self.reveal)
			self.rf.pack(side=TOP)
		
		self.ps = Button(frame, text="Photoshop", fg="blue", command=self.ps_launch)
		self.ps.pack(side=TOP)

		self.ai = Button(frame, text="Illustrator", fg="blue", command=self.ai_launch)
		self.ai.pack(side=TOP)

		self.br = Button(frame, text="Bridge", fg="blue", command=self.br_launch)
		self.br.pack(side=TOP)

		self.idcc = Button(frame, text="InDesign", fg="blue", command=self.idcc_launch)
		self.idcc.pack(side=TOP)

		self.ae = Button(frame, text="After Effects", fg="blue", command=self.ae_launch)
		self.ae.pack(side=TOP)		

		self.c4d = Button(frame, text="Cinema4D", fg="blue", command=self.c4d_launch)
		self.c4d.pack(side=TOP)		

	def ps_launch(self):
		for item in filelist:	
			subprocess.check_output(['/usr/bin/open','-a','/Applications/Adobe Photoshop CC 2014/Adobe Photoshop CC 2014.app',item])
		sys.exit(0)

	def br_launch(self):
		for item in filelist:	
			subprocess.check_output(['/usr/bin/open','-a','/Applications/Adobe Bridge CC/Adobe Bridge CC.app',item])
		sys.exit(0)

	def ai_launch(self):
		for item in filelist:	
			subprocess.check_output(['/usr/bin/open','-a','/Applications/Adobe Illustrator CC 2014/Adobe Illustrator.app',item])
		sys.exit(0)

	def c4d_launch(self):
		for item in filelist:	
			subprocess.check_output(['/usr/bin/open','-a','/Applications/Preview.app',item])
		sys.exit(0)
		
	def ae_launch(self):
		for item in filelist:
			subprocess.check_output(['/usr/bin/open','-a','/Applications/Adobe After Effects CC 2015/Adobe After Effects CC 2015.app',item])
		sys.exit(0)		
		
	def idcc_launch(self):
		for item in filelist:
			subprocess.check_output(['/usr/bin/open','-a','/Applications/Adobe InDesign CC/Adobe InDesign CC.app',item])
		sys.exit(0)			
			
	def reveal(self):
		subprocess.check_output(['/usr/bin/open','-R',filelist])
		sys.exit(0)				

		
root = Tk()
root.wm_title("Open With...")
app = App(root)
root.mainloop()
root.destroy()