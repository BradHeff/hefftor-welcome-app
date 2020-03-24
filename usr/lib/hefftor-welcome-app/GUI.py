# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================


def GUI(self, Gtk, GdkPixbuf, subprocess, fn):

    autostart = eval(self.load_settings())

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    self.cc = Gtk.Label()

    label = Gtk.Label(xalign=0)
    standard = fn.keycode("w5DDisOMw4zDqMOew6Q=",
                         "wrPCl8KtwqvCp8OKwrTCucOawqPDp8KpwpHDgcK-woXCs8KYwo_ChcOcwpvCqsK4w5jDpW_CksObwp3DrsKtw6DCu8KLwpTDmXTCjWzDmcKewqvCgg==")  # noqa
    label.set_markup(standard)
    label.set_line_wrap(True)

    # pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    # image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    if fn.username == fn.user:

        label2.set_markup(
            "We advise to clean the computer with Gparted before installing. During the Calamares installation many options will be open to you. You have the freedom of choice. " +  # noqa
            "The links below will take you to Hefftor Edition content. We supply much content for you to learn and grow with the use of Hefftor Edition. Do join us to learn the latest news, ask questions or for casual talk. \n\n" +  # noqa
            "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +  # noqa
            "Brad Heffernan")
    else:
        label2.set_markup("The links below will take you to Hefftor Edition content. We supply much content for you to learn and grow with the use of Hefftor Edition. Do join us to learn the latest news, ask questions or for casual talk. \n\n" +  # noqa
                          "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +  # noqa
                          "Brad Heffernan")
    # label2.connect( "size-allocate", self.cb_allocate )
    # vbox1.pack_start(image, False, False, 0)
    # vbox2.pack_start(label, False, False, 0)
    # vbox2.pack_start(label2, False, False, 0)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)
    # hbox4.set_homogeneous(False)
    hbox4.pack_start(label2, False, False, 0)

    grid = Gtk.Grid()

    # ======================================================================
    #                   MAIN BUTTONS
    # ======================================================================

    button1 = Gtk.Button(label="")
    button1_label = button1.get_child()
    button1_label.set_markup("<span size='large'><b>Run GParted</b></span>")
    button1.connect("clicked", self.on_gp_clicked)
    button1.set_size_request(0, 100)

    button2 = Gtk.Button(label="")
    button2_label = button2.get_child()
    button2_label.set_markup("<span size='large'><b>Run Calamares</b></span>")

    button2.connect("clicked", self.on_ai_clicked)
    button2.set_size_request(0, 100)

    # grid.add(button1)
    grid.attach(button1, 0, 0, 1, 2)
    grid.attach(button2, 1, 0, 1, 2)
    grid.set_column_homogeneous(True)
    # grid.set_row_homogeneous(True)

    # ======================================================================
    #                   NOTICE
    # ======================================================================

    self.label3 = Gtk.Label(xalign=0)
    self.label3.set_markup(
                    "<big><b><u>News</u></b></big>")
    self.label3.set_line_wrap(True)
    # label3.set_justify(Gtk.Justification.CENTER)

    self.label4 = Gtk.Label()
    self.label4.set_line_wrap(True)
    self.label4.set_justify(Gtk.Justification.CENTER)

    self.vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    self.vbox2.pack_start(self.label3, False, False, 0)
    self.vbox2.pack_start(self.label4, False, False, 0)

    # ======================================================================
    #                   USER INFO
    # ======================================================================

    lblusrname = Gtk.Label(xalign=0)
    lblusrname.set_text("User:")

    lblpassword = Gtk.Label(xalign=0)
    lblpassword.set_text("Pass:")

    lblusr = Gtk.Label(xalign=0)
    lblusr.set_text("liveuser  |")

    lblpass = Gtk.Label(xalign=0)
    lblpass.set_markup("<i>No Password</i>")

    hboxUser = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hboxUser.pack_start(lblusrname, False, False, 0)
    hboxUser.pack_start(lblusr, False, False, 0)

    hboxUser.pack_start(lblpassword, False, False, 0)
    hboxUser.pack_start(lblpass, False, False, 0)

    # ======================================================================
    #                   FOOTER BUTTON LINKS
    # ======================================================================
    button8 = Gtk.Button(label="")
    button8_label = button8.get_child()
    button8_label.set_markup("<b>Donate</b>")
    button8.connect("clicked", self.on_link_clicked,
                    "https://streamlabs.com/bradheffernan1/tip")

    button9 = Gtk.Button(label="Twitch")
    button9.connect("clicked", self.on_link_clicked,
                    "https://www.twitch.tv/bradheffernan")

    button10 = Gtk.Button(label="Github")
    button10.connect("clicked", self.on_link_clicked,
                     "https://github.com/bradheff")

    button11 = Gtk.Button(label="Youtube")
    button11.connect("clicked", self.on_link_clicked,
                     "https://www.youtube.com/c/bradheffernan")

    hbox5.pack_start(button8, True, True, 0)
    hbox5.pack_start(button10, True, True, 0)
    hbox5.pack_start(button9, True, True, 0)
    hbox5.pack_start(button11, True, True, 0)

    # ======================================================================
    #                   Add to startup
    # ======================================================================

    check = Gtk.CheckButton(label="Start on Startup")
    check.connect("toggled", self.statup_toggle)
    check.set_active(autostart)
    hbox3.pack_end(check, False, False, 0)

    # ======================================================================
    #                   SOCIAL LINKS
    # ======================================================================
    tE = Gtk.EventBox()
    liE = Gtk.EventBox()
    pE = Gtk.EventBox()
    dE = Gtk.EventBox()
    tgE = Gtk.EventBox()

    pbt = GdkPixbuf.Pixbuf().new_from_file_at_size(
        fn.os.path.join(fn.working_dir, 'images/twitter.png'), 28, 28)
    timage = Gtk.Image().new_from_pixbuf(pbt)

    pbli = GdkPixbuf.Pixbuf().new_from_file_at_size(
        fn.os.path.join(fn.working_dir, 'images/linkedin.png'), 28, 28)
    liimage = Gtk.Image().new_from_pixbuf(pbli)

    pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
        fn.os.path.join(fn.working_dir, 'images/patreon.png'), 28, 28)
    pimage = Gtk.Image().new_from_pixbuf(pbp)

    pbd = GdkPixbuf.Pixbuf().new_from_file_at_size(
        fn.os.path.join(fn.working_dir, 'images/discord.png'), 28, 28)
    dimage = Gtk.Image().new_from_pixbuf(pbd)

    pbtg = GdkPixbuf.Pixbuf().new_from_file_at_size(
        fn.os.path.join(fn.working_dir, 'images/tg.png'), 28, 28)
    tgimage = Gtk.Image().new_from_pixbuf(pbtg)

    tE.add(timage)
    liE.add(liimage)
    pE.add(pimage)
    dE.add(dimage)
    tgE.add(tgimage)

    tE.connect("button_press_event", self.on_social_clicked,
               "https://twitter.com/BradHeffernan")
    liE.connect("button_press_event", self.on_social_clicked,
                "https://www.linkedin.com/in/brad-heffernan83/")
    pE.connect("button_press_event", self.on_social_clicked,
               "https://www.patreon.com/hefftor")
    dE.connect("button_press_event", self.on_social_clicked,
               "https://discord.gg/e9bA7X")
    tgE.connect("button_press_event", self.on_social_clicked,
                "https://t.me/hefftorofficial")

    tE.set_property("has-tooltip", True)
    liE.set_property("has-tooltip", True)
    pE.set_property("has-tooltip", True)
    dE.set_property("has-tooltip", True)
    tgE.set_property("has-tooltip", True)

    tE.connect("query-tooltip", self.tooltip_callback, "Twitter")
    liE.connect("query-tooltip", self.tooltip_callback, "LinkedIn")
    pE.connect("query-tooltip", self.tooltip_callback, "Patreon")
    dE.connect("query-tooltip", self.tooltip_callback, "Discord")
    tgE.connect("query-tooltip", self.tooltip_callback, "Telegram")

    hbox3.pack_start(tE, False, False, 0)
    hbox3.pack_start(liE, False, False, 0)
    hbox3.pack_start(pE, False, False, 0)

    hbox6.pack_start(dE, False, False, 0)
    hbox6.pack_start(tgE, False, False, 0)
    if fn.username == fn.user:
        hbox3.pack_start(hboxUser, True, False, 0)
    hbox3.pack_start(hbox6, True, False, 0)

    # ======================================================================
    #                   Start Arcolinux Tweak Tool
    # ======================================================================
    launchBox = Gtk.EventBox()
    pblaunch = GdkPixbuf.Pixbuf().new_from_file_at_size(
        fn.os.path.join(fn.working_dir, 'images/hefftor.svg'), 40, 40)
    launchimage = Gtk.Image().new_from_pixbuf(pblaunch)

    launchBox.add(launchimage)
    launchBox.connect("button_press_event", self.on_launch_clicked, "")

    launchBox.set_property("has-tooltip", True)
    launchBox.connect("query-tooltip",
                      self.tooltip_callback,
                      "Run Arcolinux Tweak Tool")

    hbox6.pack_start(launchBox, False, False, 0)

    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================
    label5 = Gtk.Label()
    p = subprocess.run(["lsb_release", "-r"],
                       shell=False,
                       stdout=subprocess.PIPE)
    version = p.stdout.decode().split(":")[-1].strip()
    label5.set_text(fn.keycode("w5DDisOMw4zDqMOew6Q=",
                              "wr_CmsKqwqrDncOiw4FtwrzCmMOjwrjDmsK8wr3ChQ==") + version)  # noqa

    label3 = Gtk.Label("v20.3.23")
    hbox7.pack_start(label5, False, False, 0)
    hbox7.pack_end(label3, False, False, 0)
    if self.is_connected():
        self.get_message()

    self.vbox.pack_start(hbox1, False, False, 7)  # Logo
    self.vbox.pack_start(hbox4, False, False, 7)  # welcome Label

    if fn.username == fn.user:
        self.vbox.pack_start(grid, True, False, 7)  # Run GParted/Calamares

    self.vbox.pack_end(hbox3, False, False, 0)  # Footer
    self.vbox.pack_end(hbox7, False, False, 0)  # Version
    self.vbox.pack_end(hbox5, False, False, 7)  # Buttons
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
    # if self.is_connected():
    #     self.vbox.pack_end(self.vbox2, False, False, 0)  # Notice
