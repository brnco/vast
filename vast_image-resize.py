from PIL import Image
import os

for f in os.listdir("S:/avlab/vast/images"):
	fullf = os.path.join("S:/avlab/vast/images",f)
	print f
	im = Image.open(fullf)
	w,h = im.size
	halfwidth = int(float(w/2))
	halfheight = int(float(w/2))
	ar = float(w) / float(h)
	ar = round(ar)
	if not ar == 1.75:
		nh = float(w) / 1.75
		nw = float(h) * 1.75
		if nh > h:
			print "old dims"
			print str(w) + "x" + str(h)
			print "new dims"
			print str(int(nw))+ "x" + str(h)
			cropdiff = w - int(nw)
			cdsides = .5 * cropdiff
			cdsides = int(cdsides)
			cds = (cdsides * 2) + int(nw)
			if cds < w:
				cropl = cdsides
				cropr = cdsides + 1
			elif cds > w:
				cropl = cdsides
				cropr = cdsides - 1
			else:
				cropl = cropr = cdsides
			print "cropl " + str(cropl)
			print "cropr " + str(cropr)
			croprect = (cropl,0,w - cropr,h) 
			print croprect
			img = im.crop(croprect)
			img.save(os.path.join("S:/avlab/vast/images_edited",f))
		elif nw > w:
			print "old dims"
			print str(w) + "x" + str(h)
			print "new dims"
			print str(w) + "x" + str(int(nh))
			cropdiff = h - int(nh)
			cdtop = 0.75 * cropdiff
			cdbtm = 0.25 * cropdiff
			cdtop = int(cdtop)
			cdbtm = int(cdbtm)
			cds = cdtop + cdbtm + int(nh)
			print cds
			if cds < h:
				croptop = cdtop + 1
				cropbtm = cdbtm
			elif cds > h:
				croptop = cdtop - 1
				cropbtm = cdbtm
			else:
				croptop = cdtop
				cropbtm = cdbtm
			print "croptop " + str(croptop)
			print "cropbtm " + str(cropbtm)
			croprect = (0,croptop,w,h-cropbtm)
			print croprect
			img = im.crop(croprect)
			img.save(os.path.join("S:/avlab/vast/images_edited",f))
		print ""
	
'''print "current ar " + str(ar)
print "current h " + str(h)
print "new h " + str(float(w) / 1.75)
print "current w " + str(w)
print "new w " + str(float(h) * 1.75)
if ar > 1.77:
print "foo"
elif ar < 1.77:
print "bar"'''