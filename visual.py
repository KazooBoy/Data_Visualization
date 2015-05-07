try:
	import sys
	import os
	import numpy as np
	from astropy.io import fits as pf
	import ds9
	from Tkinter import *
except ImportError as error:
	print "You don't have module {0} installed".format(error.message[16:])
	if error.message[16:]=='ds9':
		print "See {0} documentation for installation details".format('SAO pyds9')
	if error.message[16:]=='fits':
		print "See {0} documentation for installation details".format('Astropy fits')
	sys.exit(1)

class Stripe82:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="Stripe 82 Title", command=self.onClick1)
		self.button1.pack()
		self.button2 = Button(frame, text="Radio", command=self.onClick2)
		self.button2.pack()
		self.button3 = Button(frame, text="FIR", command=self.onClick3)
		self.button3.pack()
		self.button4 = Button(frame, text="MIR", command=self.onClick4)
		self.button4.pack()
		self.button5 = Button(frame, text="Op/NIR", command=self.onClick5)
		self.button5.pack()
		self.button6 = Button(frame, text="UV", command=self.onClick6)
		self.button6.pack()
		self.button7 = Button(frame, text="X-Ray", command=self.onClick7)
		self.button7.pack()
		self.button8 = Button(frame, text="Save Image", command=self.onClick8)
		self.button8.pack()
		self.button0 = Button(frame, text="Clear All Footprints", command=self.onClick0)
		self.button0.pack()
		self.rad_exist, self.fir_exist, self.mir_exist, self.op_nir_exist, self.uv_exist, self.xray_exist, self.save_exist = ([None],[None],[None],[None],[None],[None],[None])

	def onClick1(self):
		d.set('regions stripe82_title.reg')
	
	def onClick2(self):
		newWindow("Radio Footprints","300x100+300+300",bands[1],self.rad_exist)

	def onClick3(self):
		newWindow("Far Infrared Footprints","300x75+300+300",bands[2],self.fir_exist)
	
	def onClick4(self):
		newWindow("Mid-Infrared Footprints","300x125+300+300",bands[3],self.mir_exist)
	
	def onClick5(self):
		newWindow("Optical/Near Infrared Footprints","300x150+300+300",bands[4],self.op_nir_exist)
		
	def onClick6(self):
		newWindow("Ultraviolet Footprints","300x75+300+300",bands[5],self.uv_exist)

	def onClick7(self):
		newWindow("X-Ray Footprints","300x100+300+300",bands[6],self.xray_exist)
	
	def onClick8(self):
		newWindow("Save Image","200x175+300+300",bands[7],self.save_exist)
	
	def onClick0(self):
		d.set('regions delete all')

class Radio:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="VLA (Hodge 2011)", command=self.onClick1)
		self.button1.pack()
		self.button2 = Button(frame, text="CNSS", command=self.onClick2)
		self.button2.pack()
		self.button0 = Button(frame, text="Clear All Footprints", command=self.onClick0)
		self.button0.pack()

	def onClick1(self):
		d.set('regions vla_foot.reg')

	def onClick2(self):
		d.set('regions CNSS_foot.reg')

	def onClick0(self):
		d.set('regions delete all')

class FIR:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="HeLMS and HeRS", command=self.onClick1)
		self.button1.pack()
		self.button0 = Button(frame, text="Clear All Footprints", command=self.onClick0)
		self.button0.pack()

	def onClick1(self):
		d.set('regions HeLMS_and_HeRS_only.reg')

	def onClick0(self):
		d.set('regions delete all')

class MIR:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="SHELA", command=self.onClick1)
		self.button1.pack()
		self.button2 = Button(frame, text="SpIES (Ch. 1)", command=self.onClick2)
		self.button2.pack()
		self.button3 = Button(frame, text="SpIES (Ch. 2)", command=self.onClick3)
		self.button3.pack()
		self.button0 = Button(frame, text="Clear All Footprints", command=self.onClick0)
		self.button0.pack()

	def onClick1(self):
		d.set('regions SHELA.reg')

	def onClick2(self):
		d.set('regions SpIES_regions_ch1.reg')
	
	def onClick3(self):
		d.set('regions SpIES_regions_ch2.reg')

	def onClick0(self):
		d.set('regions delete all')

class Op_NIR:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="SDSS S82", command=self.onClick1)
		self.button1.pack()
		self.button2 = Button(frame, text="HSC", command=self.onClick2)
		self.button2.pack()
		self.button3 = Button(frame, text="DES", command=self.onClick3)
		self.button3.pack()
		self.button4 = Button(frame, text="PRIMUS", command=self.onClick4)
		self.button4.pack()		
		self.button0 = Button(frame, text="Clear All Footprints", command=self.onClick0)
		self.button0.pack()
	
	def onClick1(self):
		d.set('regions stripe82.reg')
	
	def onClick2(self):
		d.set('regions HSC.reg')
	
	def onClick3(self):
		d.set('regions DES.reg')
	
	def onClick4(self):
		d.set('regions PRIMUS_stripe82.reg')
		d.set('regions PRIMUS_stripe82_masks.reg')
	
	def onClick0(self):
		d.set('regions delete all')

class UV:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="GALEX", command=self.onClick1)
		self.button1.pack()
		self.button0 = Button(frame, text="Clear All Footprints", command=self.onClick0)
		self.button0.pack()
		self.im_exist = [None]
		self.leg_exist = [None]
	
	def onClick1(self):
		if self.im_exist[0] is None:
			image = Toplevel()
			image.title('GALEX Survey(s)')
			image.geometry('+650+300')
			entry = Entry(image, bd=3)
			image.bind("<Return>", (lambda event, e=entry: self.survey(e,image)))
			label = Label(image, text="Please enter 'dis', 'mis', 'ais', or 'all' (separated by commas if multiple) for desired survey(s)")
			label.pack(side=LEFT)
			entry.pack(side=LEFT)
			self.im_exist[0] = 1
			image.protocol("WM_DELETE_WINDOW", lambda image=image: existance(image,self.im_exist))
		if self.leg_exist[0] is None:
			legend = Toplevel()
			legend.title('GALEX Survey Legend')
			legend.geometry('225x100+1645+300')
			legend.configure(background='grey20')
			Label(legend, text='AIS', fg='white', bg='grey20', font=('TkDefaultFont',24)).pack()
			Label(legend, text='MIS', fg='red', bg='grey20', font=('TkDefaultFont',24)).pack()
			Label(legend, text='DIS', fg='blue', bg='grey20', font=('TkDefaultFont',24)).pack()
			self.leg_exist[0] = 1
			legend.protocol("WM_DELETE_WINDOW", lambda legend=legend: existance(legend,self.leg_exist))
			
	
	def survey(self, entry, image):
		surveylist = ['dis','mis','ais']
		surveys = [x.strip() for x in entry.get().split(',')]
		if len(surveys)>1:
			if all((y in surveys for y in surveylist)):
				d.set('regions gr67.reg')
			elif all((y in surveys for y in [surveylist[0],surveylist[1]])):
				d.set('regions gr67_dis.reg')
				d.set('regions gr67_mis.reg')
			elif all((y in surveys for y in [surveylist[0],surveylist[2]])):
				d.set('regions gr67_dis.reg')
				d.set('regions gr67_ais.reg')
			elif all((y in surveys for y in [surveylist[2],surveylist[2]])):
				d.set('regions gr67_mis.reg')
				d.set('regions gr67_ais.reg')
		else:
			if surveys[0] == 'all':
				d.set('regions gr67.reg')
			if surveys[0] == surveylist[0]:
				d.set('regions gr67_dis.reg')
			if surveys[0] == surveylist[1]:
				d.set('regions gr67_mis.reg')
			if surveys[0] == surveylist[2]:
				d.set('regions gr67_ais.reg')			
		image.destroy()
	
	def onClick0(self):
		d.set('regions delete all')

class XRAY:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="Chandra", command=self.onClick1)
		self.button1.pack()
		self.button2 = Button(frame, text="XMM-Newton", command=self.onClick2)
		self.button2.pack()
		self.button0 = Button(frame, text="Clear All Footprints", command=self.onClick0)
		self.button0.pack()
		self.im_exist = [None]
		self.leg_exist = [None]

	def onClick1(self):
		if self.im_exist[0] is None:
			image = Toplevel()
			image.title('Chandra Camera(s)')
			image.geometry('+650+300')
			entry = Entry(image, bd=3)
			image.bind("<Return>", (lambda event, e=entry: self.camera(e,image)))
			label = Label(image, text="Please enter 'acis-s', 'acis-i', 'hrc-s', 'hrc-i', or 'all' (separated by commas if multiple) for desired survey(s)")
			label.pack(side=LEFT)
			entry.pack(side=LEFT)
			self.im_exist[0] = 1
			image.protocol("WM_DELETE_WINDOW", lambda image=image: existance(image,self.im_exist))
		if self.leg_exist[0] is None:
			legend = Toplevel()
			legend.title('Chandra Camera Legend')
			legend.geometry('225x135+1645+300')
			legend.configure(background='grey20')
			Label(legend, text='ACIS-S', fg='red', bg='grey20', font=('TkDefaultFont',24)).pack()
			Label(legend, text='ACIS-I', fg='blue', bg='grey20', font=('TkDefaultFont',24)).pack()
			Label(legend, text='HRC-S', fg='magenta', bg='grey20', font=('TkDefaultFont',24)).pack()
			Label(legend, text='HRC-I', fg='green2', bg='grey20', font=('TkDefaultFont',24)).pack()
			self.leg_exist[0] = 1
			legend.protocol("WM_DELETE_WINDOW", lambda legend=legend: existance(legend,self.leg_exist))
	
	def camera(self, entry, image):
		cameralist = ['acis-s','acis-i','hrc-s','hrc-i']
		cameras = [x.strip() for x in entry.get().split(',')]
		if len(cameras)>1:
			if all((y in cameras for y in cameralist)):
				d.set('regions chandra_foot.reg')
			elif all((y in cameras for y in [cameralist[0],cameralist[1]])):
				d.set('regions chandra_acis-s.reg')
				d.set('regions chandra_acis-i.reg')
			elif all((y in cameras for y in [cameralist[2],cameralist[3]])):
				d.set('regions chandra_hrc-s.reg')
				d.set('regions chandra_hrc-i.reg')
		else:
			if cameras[0] == 'all':
				d.set('regions chandra_foot.reg')
			if cameras[0] == cameralist[0]:
				d.set('regions chandra_acis-s.reg')
			if cameras[0] == cameralist[1]:
				d.set('regions chandra_acis-i.reg')
			if cameras[0] == cameralist[2]:
				d.set('regions chandra_hrc-s.reg')
			if cameras[0] == cameralist[3]:
				d.set('regions chandra_hrc-i.reg')	
		image.destroy()
	
	def onClick2(self):
		d.set('regions xmm_archival.reg')
		d.set('regions xmm_ao10.reg')
	
	def onClick0(self):
		d.set('regions delete all')

class Save:
	
	def __init__(self, master):
		frame = Frame(master) 
		frame.pack()
		self.button1 = Button(frame, text="PNG", command=lambda x=self.onClick0: x('png'))
		self.button1.pack()
		self.button2 = Button(frame, text="EPS", command=lambda x=self.onClick0: x('eps'))
		self.button2.pack()
		self.button3 = Button(frame, text="JPEG", command=lambda x=self.onClick0: x('jpeg'))
		self.button3.pack()
		self.button4 = Button(frame, text="FITS", command=lambda x=self.onClick0: x('fits'))
		self.button4.pack()
		self.button5 = Button(frame, text="GIF", command=lambda x=self.onClick0: x('gif'))
		self.button5.pack()
		self.button6 = Button(frame, text="TIFF", command=lambda x=self.onClick0: x('tiff'))
		self.button6.pack()
		self.im_exist = [None]
	
	def onClick0(self,type):
		if self.im_exist[0] is None:
			image = Toplevel()
			image.title('Save as {0} Image'.format(type.upper()))
			image.geometry('+550+300')
			entry = Entry(image, bd=3)
			image.bind("<Return>", (lambda event, e=entry: self.saveimage(e,image,type)))
			label = Label(image, text='.{0}'.format(type))
			entry.pack(side=LEFT)
			label.pack(side=LEFT)
			self.im_exist[0] = 1
			image.protocol("WM_DELETE_WINDOW", lambda image=image: existance(image,self.im_exist))
		
	def saveimage(self, entry, image, type):
		if def_dir=="D":
			d.set('saveimage {0}.{1}'.format(entry.get(),type))
		else:
			d.set('saveimage {0}/{1}.{2}'.format(def_dir,entry.get(),type))
		image.destroy()

def newWindow(Title,geo,band,ex):
	if ex[0]==None:
		wdw = Toplevel()
		wdw.title(Title)
		wdw.geometry(geo)
		if band=='T':
			app = Stripe82(wdw)
		if band=='r':
			app = Radio(wdw)
		if band=='far':
			app = FIR(wdw)
		if band=='mid':
			app = MIR(wdw)
		if band=='op':
			app = Op_NIR(wdw)
		if band=='uv':
			app = UV(wdw)
		if band=='x':
			app = XRAY(wdw)
		if band=='save':
			app = Save(wdw)	
		windows.append(wdw)
		ex[0]=1
		wdw.protocol('WM_DELETE_WINDOW', lambda wdw=wdw: closeWindow(wdw,ex))

def closeWindow(wdw, ex):
	ex[0]=None
	wdw.destroy()
	if wdw in windows: windows.remove(wdw)
	if not windows: root.quit()

def existance(wdw,ex):
	ex[0] = None
	wdw.destroy()

def visual():
	global windows,bands,root,d,def_dir
	
	def_dir = raw_input("Name of directory to save images in (Current Working Directory: D): ")
	while os.path.isdir(def_dir)==False:
		if def_dir=="D":
			break
		print "{0} does not exist".format(def_dir)
		def_dir=raw_input("Try another directory:  ")
	
	d = ds9.ds9(wait=10)
	d.set('regions delete all')
	d.set('mosaic wcs stripe82_60_2.fits')
	d.set('mosaic wcs stripe82_300_2.fits')
	d.set('zoom to fit')
	d.set('grid yes')
	d.set('grid axes no')
	d.set('wcs skyformat degrees')

	d.set('regions stripe82_title.reg')
	
	root = Tk()
	root.withdraw()
	s82_exist = [None]
	windows=[]
	bands=['T','r','far','mid','op','uv','x','save']
	newWindow("Stripe 82","200x260+50+300",bands[0],s82_exist)
	root.mainloop()

if __name__ == '__main__':
	visual()
