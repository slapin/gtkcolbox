#!/usr/bin/python

# http://python-gtk-3-tutorial.readthedocs.org/en/latest/button_widgets.html


from PIL import Image
from glob import glob
from gi.repository import Gtk

class Handler():
	def __init__(self, builder):
		self.builder = builder
		self.dlg_add_anim = builder.get_object("animation_add_dialog")
		self.new_anim_name = builder.get_object("new_anim_name")
		self.anim_list = []
		self.anim_cbox = builder.get_object("animation_box")
		self.anim_box = None

	#First dialog left button
	def new_animation_cb(self, st):
		self.dlg_add_anim.show_all()
		self.dlg_add_anim.run()
	def new_anim_go(self, button):
		print self.new_anim_name.get_text()
		self.anim_list.append(self.new_anim_name.get_text())
		if self.anim_box:
			self.anim_box.destroy()
		self.anim_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=len(self.anim_list))
		b = None
		for t in self.anim_list:
			b = Gtk.RadioButton.new_with_label_from_widget(b, t)
			self.anim_box.pack_start(b, False, False, 0)
			b.connect("toggled", self.select_anim, t)
		b.set_active(True)
		self.anim_cbox.pack_start(self.anim_box, False, False, 0)
		self.anim_cbox.show_all()
		self.dlg_add_anim.hide()
	def new_anim_cancel(self, button):
		self.dlg_add_anim.hide()
	def select_anim(self, b, anim):
		if b.get_active():
			self.current_anim = anim
			print "current anim", anim

builder = Gtk.Builder()
builder.add_from_file("animation.glade")
builder.connect_signals(Handler(builder))
main_window = builder.get_object("main_window")
main_window.connect("delete-event", Gtk.main_quit)
main_window.show_all()
Gtk.main()

def foo():
	for filename in glob("*.png"):
		myimage = Image.open(filename)
		print myimage.format, myimage.size, myimage.mode
		mypal = Image.open("palette.gif")
		background = Image.new("RGB", myimage.size, (252, 0, 255))
		background.paste(myimage, mask=myimage.split()[3])
		converted = background.quantize(palette=mypal)
		converted.save('converted/' + filename)
	
