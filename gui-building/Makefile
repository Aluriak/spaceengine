
OUTDIR=output
SPLASHS=splash/*.png
OUTMENU=eng-menu.png
MENUDIR=menu/*.png
MENUFONT=menu/*.pak
SPLASHFONT=splash/*.pak


make_all: make_output

make_output: clean_output make_struct make_splash make_texts make_menu
	mkdir -p $(OUTDIR)/textures/common/

make_struct:
	mkdir -p $(OUTDIR)/textures/common/
	mkdir -p $(OUTDIR)/data/locale/
make_splash:
	cp $(SPLASHS) $(OUTDIR)/textures/common/
make_texts:
	cp $(MENUFONT) $(OUTDIR)/data/locale/
	cp $(SPLASHFONT) $(OUTDIR)/textures/common/
make_menu:
	$(PYTHON) make-menu.py $(MENUDIR) $(OUTMENU)
	cp $(OUTMENU) $(OUTDIR)/data/locale/


clean_output:
	- rm -r $(OUTDIR)/*
