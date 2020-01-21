import hashlib, pickle, datetime, os
import Tkinter as tk

class backend():
    def pat(self, pname, page, pgender, prelation, prelative, paddress, pcomplaints, ptreatment, pmedhis, popco):
        e = []
        pnamecheck = str(pname.replace(" ", ""))
        if not pnamecheck.isalpha():
            e.append("pnameerr")
        if page == "":
            e.append("pageerr")
        if pgender == "":
            e.append("pgendererr")
        if prelative == "":
            e.append("prelativeerr")
        if paddress == "":
            e.append("paddresserr")
        if pcomplaints == "":
            e.append("pcomplaintserr")
        if ptreatment == "":
            ptreatment = "-"
        if pmedhis == "":
            pmedhis = "-"
        if popco == "":
            popco = "-"
        if e == []:
            doc = open("resources\\patients.det", "a")
            doc.write(str(pname) + "~" + str(page) + "~" + str(pgender) + "~" + str(prelation) + "~" + str(prelative) +
                      "~" + str(paddress) + "~" + str(pcomplaints) + "~" + str(ptreatment) + "~" + str(pmedhis) + "~" +
                      str(popco) + "~" + self.currentdate() + "~" + "-" + "~" + "Admitted"+"\n")
            doc.close()
        return e

    def doc(self, dname, dgender, dday, dmonth, dyear, dpaddress, dmaddress, dhighschool, dmbbs, dpgdegree,
            dpginstitute, dachievements):
        e = []
        ddob = str(dday + "/" + dmonth + "/" + dyear)
        dnamecheck = str(dname.replace(" ", ""))
        if not dnamecheck.isalpha():
            e.append("dnameerr")
        if dgender == "":
            e.append("dgendererr")
        if dpaddress == "":
            e.append("dpaddresserr")
        if dmaddress == "":
            e.append("dmaddresserr")
        if dhighschool == "":
            e.append("dhighschoolerr")
        if dmbbs == "":
            e.append("dmbbserr")
        if dpgdegree == "":
            e.append("dpgdegreeerr")
        if dpginstitute == "":
            e.append("dpginstituteerr")
        if dachievements == "":
            dachievements = "-"
        if e == []:
            doc = open("resources\\doctors.det", "a")
            doc.write(str(dname) + "~" + str(dgender) + "~" + str(ddob) + "~" + str(dpaddress) + "~" + str(dmaddress) +
                      "~" + str(dhighschool) + "~" + str(dmbbs) + "~" + str(dpgdegree) + "~" + str(dpginstitute) +
                      "~" + str(dachievements) + "~" + self.currentdate() + "~" + "-" + "~" + "Employed" + "\n")
            doc.close()
        return e

    def noofemployeddoctors(self):
        employed = 0
        data = []
        docdat = open("resources\\doctors.det", "r")
        for x in docdat:
            x = x.strip()
            data.append(x.split("~"))
        docdat.close()
        for i in range(len(data)):
            if "Employed" in data[i]:
                employed += 1
        return employed

    def noofadmittedpatients(self):
        admitted = 0
        data = []
        patdat = open("resources\\patients.det", "r")
        for x in patdat:
            x = x.strip()
            data.append(x.split("~"))
        patdat.close()
        for i in range(len(data)):
            if "Admitted" in data[i]:
                admitted += 1
        return admitted

    def currentdate(self):
        cdate = datetime.datetime.today()
        day = str(cdate.day)
        monthdict = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June",
                     "7": "July", "8": "August",
                     "9": "September", "10": "October", "11": "November", "12": "December"}
        month = monthdict[str(cdate.month)]
        year = str(cdate.year)
        return str(day + "/" + month + "/" + year)

class frontend:
    def __init__(self, mainframe = None):
        if mainframe is not None:
            topmenu = tk.Menu(mainframe)
            mainframe.config(menu=topmenu)
            mainlogo = tk.PhotoImage(file="resources/mainlogo.gif")
            global patlogo, doclogo, datlogo, patlogo2, doclogo2, datlogo2
            patlogo = tk.PhotoImage(file="resources/patient.gif")
            doclogo = tk.PhotoImage(file="resources/doctor.gif")
            datlogo = tk.PhotoImage(file="resources/database.gif")
            patlogo2 = tk.PhotoImage(file="resources/patient2.gif")
            doclogo2 = tk.PhotoImage(file="resources/doctor2.gif")
            datlogo2 = tk.PhotoImage(file="resources/database2.gif")
            filemenu = tk.Menu(topmenu)
            topmenu.add_cascade(label="File", menu=filemenu)
            filemenu.add_command(label="Logout", command=self.logout)
            filemenu.add_command(label="Exit")
            self.patlocation = ""
            self.doclocation = ""

            # Frames
            global loginform, mainmenu, patmenu, docmenu, datmenu, patsubmenua, patsubmenub, patsubmenuc, docsubmenua, \
                docsubmenub, docsubmenuc, datsubmenua, datsubmenub, datsubmenuc, datsubmenud
            loginform = tk.Frame(mainframe, bg="#FFFFFF", width=1024, height=576)
            mainmenu = tk.Frame(mainframe, bg="#1E1E1E", width=1024, height=576)
            patmenu = tk.Frame(mainframe, bg="#1E1E1E", width=1024, height=576)
            docmenu = tk.Frame(mainframe, bg="#1E1E1E", width=1024, height=576)
            datmenu = tk.Frame(mainframe, bg="#1E1E1E", width=1024, height=576)
            patsubmenua = tk.Frame(mainframe, bg="#1E1E1E")
            patsubmenub = tk.Frame(mainframe, bg="#1E1E1E")
            patsubmenuc = tk.Frame(mainframe, bg="#1E1E1E")
            docsubmenua = tk.Frame(mainframe, bg="#1E1E1E")
            docsubmenub = tk.Frame(mainframe, bg="#1E1E1E")
            docsubmenuc = tk.Frame(mainframe, bg="#1E1E1E")
            datsubmenua = tk.Frame(mainframe, bg="#1E1E1E")
            datsubmenub = tk.Frame(mainframe, bg="#1E1E1E")
            datsubmenuc = tk.Frame(mainframe, bg="#1E1E1E")
            datsubmenud = tk.Frame(mainframe, bg="#1E1E1E")
            framelist = (loginform, mainmenu, patmenu, docmenu, datmenu, patsubmenua, patsubmenub, patsubmenuc,
                         docsubmenua, docsubmenub, docsubmenuc, datsubmenua, datsubmenub, datsubmenuc, datsubmenud)
            self.insertFrame(framelist)

            # Login
            self.mainlogol = tk.Label(loginform, image=mainlogo, bg="#FFFFFF")
            self.mainlogol.photo = mainlogo
            self.loginlabelu = tk.Label(loginform, text="Username: ", bg="#FFFFFF")
            self.loginlabelp = tk.Label(loginform, text="Password: ", bg="#FFFFFF")
            self.loginuser = tk.Entry(loginform, bg="#FFFFFF")
            self.loginpass = tk.Entry(loginform, show="+", bg="#FFFFFF")
            self.loginbutton = tk.Button(loginform, text="Login", relief="groove", command=self.auth, bg="#1996D7",
                                         fg="#FFFFFF")
            self.mainlogol.grid(columnspan=2, row=0, pady=40)
            self.loginlabelu.grid(row=1, pady=10, ipady=2, sticky=tk.E)
            self.loginlabelp.grid(row=2, pady=10, ipady=2, sticky=tk.E)
            self.loginuser.grid(row=1, column=1, pady=10, ipady=2, sticky=tk.W)
            self.loginpass.grid(row=2, column=1, pady=10, ipady=2, sticky=tk.W)
            self.loginbutton.grid(columnspan=2, row=3, pady=10, ipadx=30, ipady=5)

            # Main Menu
            self.blackbackground = tk.Label(mainmenu, bg="#111111", height=6, width=200)
            self.patlogol = tk.Button(mainmenu, image=patlogo, highlightthickness=0, bd=0, relief=tk.FLAT,
                                      command=self.patmenu)
            self.patlogol.photo = patlogo
            self.doclogol = tk.Button(mainmenu, image=doclogo, highlightthickness=0, bd=0, relief=tk.FLAT,
                                      command=self.docmenu)
            self.doclogol.photo = doclogo
            self.datlogol = tk.Button(mainmenu, image=datlogo, highlightthickness=0, bd=0, relief=tk.FLAT,
                                      command=self.datmenu)
            self.datlogol.photo = datlogo
            self.patlogol.bind("<Enter>", self.patenter)
            self.patlogol.bind("<Leave>", self.patleave)
            self.doclogol.bind("<Enter>", self.docenter)
            self.doclogol.bind("<Leave>", self.docleave)
            self.datlogol.bind("<Enter>", self.datenter)
            self.datlogol.bind("<Leave>", self.datleave)
            self.mainbutton_pat = tk.Label(mainmenu, text="Manage Patients", bg="#1E1E1E", fg="#FFFFFF",
                                           relief=tk.FLAT, font=("Tw Cen MT Condensed", 16))
            self.mainbutton_doc = tk.Label(mainmenu, text="Manage Doctors", bg="#1E1E1E", fg="#FFFFFF", relief=tk.FLAT,
                                           font=("Tw Cen MT Condensed", 16))
            self.mainbutton_dat = tk.Label(mainmenu, text="View Database", bg="#1E1E1E", fg="#FFFFFF", relief=tk.FLAT,
                                           font=("Tw Cen MT Condensed", 16))
            self.mainstatusreport = tk.Label(mainmenu, text="Status\nReport", bg="#111111", fg="#FFFFFF",
                                             relief=tk.FLAT, font=("Tw Cen MT Condensed", 24))
            self.mainpatientsadmitted = tk.Label(mainmenu, text="Patients Admitted", bg="#111111", fg="#FFFFFF",
                                                 relief=tk.FLAT, font=("Calibri", 12))
            self.maindoctorsemployed = tk.Label(mainmenu, text="Doctors Employed", bg="#111111", fg="#FFFFFF",
                                                relief=tk.FLAT, font=("Calibri", 12))
            self.mainpatientsadmittednumber = tk.Label(mainmenu, text=str(backend().noofadmittedpatients()),
                                                       bg="#111111", fg="#CC0000", relief=tk.FLAT,
                                                       font=("Tw Cen MT Condensed", 28))
            self.maindoctorsemployednumber = tk.Label(mainmenu, text=str(backend().noofemployeddoctors()),
                                                      bg="#111111", fg="#00CC17", relief=tk.FLAT,
                                                      font=("Tw Cen MT Condensed", 28))
            self.blackbackground.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
            self.mainbutton_back = tk.Button(mainmenu, text="Logout", command=self.logout, width=50, height=2,
                                             bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patlogol.place(relx=0.25, rely=0.25, anchor=tk.CENTER)
            self.mainbutton_pat.place(relx=0.25, rely=0.50, anchor=tk.CENTER)
            self.doclogol.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            self.mainbutton_doc.place(relx=0.5, rely=0.50, anchor=tk.CENTER)
            self.datlogol.place(relx=0.75, rely=0.25, anchor=tk.CENTER)
            self.mainbutton_dat.place(relx=0.75, rely=0.50, anchor=tk.CENTER)
            self.mainstatusreport.place(relx=0.25, rely=0.70, anchor=tk.CENTER)
            self.mainpatientsadmitted.place(relx=0.50, rely=0.66, anchor=tk.CENTER)
            self.maindoctorsemployed.place(relx=0.75, rely=0.66, anchor=tk.CENTER)
            self.mainpatientsadmittednumber.place(relx=0.50, rely=0.725, anchor=tk.CENTER)
            self.maindoctorsemployednumber.place(relx=0.75, rely=0.725, anchor=tk.CENTER)
            self.mainbutton_back.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

            # Patient Menu
            self.patbutton_1 = tk.Button(patmenu, text="Admit a Patient", command=self.patsubmenua, width=50, height=2,
                                         bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patbutton_2 = tk.Button(patmenu, text="Discharge a Patient", command=self.patsubmenub, width=50,
                                         height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patbutton_3 = tk.Button(patmenu, text="Search or Modify Existing Patient's Details",
                                         command=self.patsubmenuc, width=50, height=2, bg="#333333", fg="#FFFFFF",
                                         relief=tk.FLAT)
            self.patbutton_back = tk.Button(patmenu, text="Back to Main Menu", command=self.mainmenu, width=50,
                                            height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patbutton_1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
            self.patbutton_2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            self.patbutton_3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.patbutton_back.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

            # Patient Sub Menu A
            self.padmit = tk.Label(patsubmenua, text="Enter Patient's Details", bg="#1E1E1E", fg="#FFFFFF")
            self.pnamelabel = tk.Label(patsubmenua, text="Name", bg="#1E1E1E", fg="#FFFFFF")
            self.pagelabel = tk.Label(patsubmenua, text="Age", bg="#1E1E1E", fg="#FFFFFF")
            self.pgenderlabel = tk.Label(patsubmenua, text="Gender", bg="#1E1E1E", fg="#FFFFFF")
            self.prelation = tk.StringVar()
            self.prelation.set("S/o")
            self.prelationopt = tk.OptionMenu(patsubmenua, self.prelation, "S/o", "D/o", "W/o")
            self.prelationopt.config(bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0,
                                     activebackground="#333333", activeforeground="#FFFFFF")
            self.prelationopt["menu"].config(bg="#333333", fg="#FFFFFF", bd=0, activebackground="#1E1E1E")
            self.paddresslabel = tk.Label(patsubmenua, text="Address", bg="#1E1E1E", fg="#FFFFFF")
            self.pcomplaintslabel = tk.Label(patsubmenua, text="Complaints", bg="#1E1E1E", fg="#FFFFFF")
            self.ptreatmentlabel = tk.Label(patsubmenua, text="Treatment (if taken any)", bg="#1E1E1E", fg="#FFFFFF")
            self.pmedhislabel = tk.Label(patsubmenua, text="Medical History", bg="#1E1E1E", fg="#FFFFFF")
            self.popcolabel = tk.Label(patsubmenua, text="Past Operations or Medical Condition (if any)", bg="#1E1E1E",
                                       fg="#FFFFFF")
            self.pname = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.page = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.pgender = tk.StringVar()
            self.pgenderm = tk.Radiobutton(patsubmenua, text="Male", variable=self.pgender, value="Male",
                                           relief=tk.FLAT, indicatoron=0, bg="#333333", fg="#FFFFFF",
                                           selectcolor="#1E1E1E")
            self.pgenderf = tk.Radiobutton(patsubmenua, text="Female", variable=self.pgender, value="Female",
                                           relief=tk.FLAT, indicatoron=0, bg="#333333", fg="#FFFFFF",
                                           selectcolor="#1E1E1E")
            self.pgendero = tk.Radiobutton(patsubmenua, text="Other", variable=self.pgender, value="Other",
                                           relief=tk.FLAT, indicatoron=0, bg="#333333", fg="#FFFFFF",
                                           selectcolor="#1E1E1E")
            self.prelative = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.paddress = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.pcomplaints = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.ptreatment = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.pmedhis = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.popco = tk.Entry(patsubmenua, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.psubmit = tk.Button(patsubmenua, text="Submit", command=self.patsubmenuacom, bg="#333333",
                                     fg="#FFFFFF", relief=tk.FLAT)
            self.patsubmenuaback = tk.Button(patsubmenua, text="< Back", relief=tk.FLAT, command=self.patmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.padmit.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
            self.pnamelabel.place(relx=0.49, rely=0.21, anchor=tk.E)
            self.pagelabel.place(relx=0.49, rely=0.28, anchor=tk.E)
            self.pgenderlabel.place(relx=0.49, rely=0.35, anchor=tk.E)
            self.prelationopt.place(relx=0.49, rely=0.42, anchor=tk.E)
            self.paddresslabel.place(relx=0.49, rely=0.49, anchor=tk.E)
            self.pcomplaintslabel.place(relx=0.49, rely=0.56, anchor=tk.E)
            self.ptreatmentlabel.place(relx=0.49, rely=0.63, anchor=tk.E)
            self.pmedhislabel.place(relx=0.49, rely=0.7, anchor=tk.E)
            self.popcolabel.place(relx=0.49, rely=0.77, anchor=tk.E)
            self.pname.place(relx=0.51, rely=0.21, anchor=tk.W)
            self.page.place(relx=0.51, rely=0.28, anchor=tk.W)
            self.pgenderm.place(relx=0.51, rely=0.35, anchor=tk.W)
            self.pgenderf.place(relx=0.55, rely=0.35, anchor=tk.W)
            self.pgendero.place(relx=0.60, rely=0.35, anchor=tk.W)
            self.prelative.place(relx=0.51, rely=0.42, anchor=tk.W)
            self.paddress.place(relx=0.51, rely=0.49, anchor=tk.W)
            self.pcomplaints.place(relx=0.51, rely=0.56, anchor=tk.W)
            self.ptreatment.place(relx=0.51, rely=0.63, anchor=tk.W)
            self.pmedhis.place(relx=0.51, rely=0.7, anchor=tk.W)
            self.popco.place(relx=0.51, rely=0.77, anchor=tk.W)
            self.psubmit.place(relx=0.50, rely=0.9, anchor=tk.CENTER)
            self.patsubmenuaback.place(relx=0.05, rely=0.05, anchor=tk.CENTER)

            # Patient Sub Menu B
            self.patbsearchitems = []
            self.patbsearchbox = tk.Entry(patsubmenub, width=50, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patbsearchbutton = tk.Button(patsubmenub, text="Search", command=self.patbsearch, bg="#333333",
                                              fg="#FFFFFF", relief=tk.FLAT)
            self.patresignbutton = tk.Button(patsubmenub, text="Discharge", command=self.patdischarge, bg="#333333",
                                             fg="#FFFFFF", relief=tk.FLAT)
            self.patsubmenubback = tk.Button(patsubmenub, text="< Back", relief=tk.FLAT, command=self.patmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.patbsearchbox.place(relx=0.45, rely=0.05, anchor=tk.CENTER)
            self.patbsearchbutton.place(relx=0.65, rely=0.05, anchor=tk.CENTER)
            self.patresignbutton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
            self.patsubmenubback.place(relx=0.05, rely=0.05, anchor=tk.CENTER)
            self.patselected = tk.StringVar()

            # Patient Sub Menu C
            self.patcsearchitems = []
            self.patcsearchbox = tk.Entry(patsubmenuc, width=50, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patcsearchbutton = tk.Button(patsubmenuc, text="Search", command=self.patcsearch, bg="#333333",
                                              fg="#FFFFFF", relief=tk.FLAT)
            self.patmodinfo = tk.Label(patsubmenuc, text="Select the Fields to Modify", bg="#1E1E1E", fg="#FFFFFF")
            self.patmodname = tk.IntVar()
            self.patmodnamebutton = tk.Checkbutton(patsubmenuc, text="Name", variable=self.patmodname, bg="#1E1E1E",
                                                   fg="#FFFFFF", activebackground="#1E1E1E",
                                                   activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.patmodnamebutton.deselect()
            self.patmodage = tk.IntVar()
            self.patmodagebutton = tk.Checkbutton(patsubmenuc, text="Age", variable=self.patmodage, bg="#1E1E1E",
                                                  fg="#FFFFFF", activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                  selectcolor="#1E1E1E")
            self.patmodagebutton.deselect()
            self.patmodgender = tk.IntVar()
            self.patmodgenderbutton = tk.Checkbutton(patsubmenuc, text="Gender", variable=self.patmodgender,
                                                     bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                     activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.patmodgenderbutton.deselect()
            self.patmodrelation = tk.IntVar()
            self.patmodrelationbutton = tk.Checkbutton(patsubmenuc, text="Relation", variable=self.patmodrelation,
                                                       bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                       activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.patmodrelationbutton.deselect()
            self.patmodrelative = tk.IntVar()
            self.patmodrelativebutton = tk.Checkbutton(patsubmenuc, text="Relative", variable=self.patmodrelative,
                                                       bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                       activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.patmodrelativebutton.deselect()
            self.patmodaddress = tk.IntVar()
            self.patmodaddressbutton = tk.Checkbutton(patsubmenuc, text="Address", variable=self.patmodaddress,
                                                      bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                      activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.patmodaddressbutton.deselect()
            self.patmodcomplaints = tk.IntVar()
            self.patmodcomplaintsbutton = tk.Checkbutton(patsubmenuc, text="Complaints",
                                                         variable=self.patmodcomplaints, bg="#1E1E1E", fg="#FFFFFF",
                                                         activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                         selectcolor="#1E1E1E")
            self.patmodcomplaintsbutton.deselect()
            self.patmodtreatment = tk.IntVar()
            self.patmodtreatmentbutton = tk.Checkbutton(patsubmenuc, text="Treatment (if taken any)",
                                                        variable=self.patmodtreatment, bg="#1E1E1E", fg="#FFFFFF",
                                                        activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                        selectcolor="#1E1E1E")
            self.patmodtreatmentbutton.deselect()
            self.patmodmedhis = tk.IntVar()
            self.patmodmedhisbutton = tk.Checkbutton(patsubmenuc, text="Medical History", variable=self.patmodmedhis,
                                                     bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                     activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.patmodmedhisbutton.deselect()
            self.patmodopco = tk.IntVar()
            self.patmodopcobutton = tk.Checkbutton(patsubmenuc, text="Past Operations or Medical Condition (if any)",
                                                   variable=self.patmodopco, bg="#1E1E1E", fg="#FFFFFF",
                                                   activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                   selectcolor="#1E1E1E")
            self.patmodopcobutton.deselect()
            self.patmodnameentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodageentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodgenderentry = tk.StringVar()
            self.patmodgendermentry = tk.Radiobutton(patsubmenuc, text="Male", variable=self.patmodgenderentry,
                                                     value="Male", indicatoron=0, bg="#333333", fg="#FFFFFF",
                                                     selectcolor="#1E1E1E")
            self.patmodgenderfentry = tk.Radiobutton(patsubmenuc, text="Female", variable=self.patmodgenderentry,
                                                     value="Female", indicatoron=0, bg="#333333", fg="#FFFFFF",
                                                     selectcolor="#1E1E1E")
            self.patmodgenderoentry = tk.Radiobutton(patsubmenuc, text="Other", variable=self.patmodgenderentry,
                                                     value="Other", indicatoron=0, bg="#333333", fg="#FFFFFF",
                                                     selectcolor="#1E1E1E")
            self.patmodrelationentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodrelativeentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodaddressentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodcomplaintsentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodtreatmententry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodmedhisentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodopcoentry = tk.Entry(patsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.patmodifybutton = tk.Button(patsubmenuc, text="Modify", command=self.patmod, bg="#333333",
                                             fg="#FFFFFF", relief=tk.FLAT)
            self.patsubmenucback = tk.Button(patsubmenuc, text="< Back", relief=tk.FLAT, command=self.patmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.patcsearchbox.place(relx=0.45, rely=0.05, anchor=tk.CENTER)
            self.patcsearchbutton.place(relx=0.65, rely=0.05, anchor=tk.CENTER)
            self.patmodinfo.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
            self.patmodnamebutton.place(relx=0.05, rely=0.6, anchor=tk.W)
            self.patmodagebutton.place(relx=0.2, rely=0.6, anchor=tk.W)
            self.patmodgenderbutton.place(relx=0.35, rely=0.6, anchor=tk.W)
            self.patmodrelationbutton.place(relx=0.51, rely=0.6, anchor=tk.W)
            self.patmodrelativebutton.place(relx=0.66, rely=0.6, anchor=tk.W)
            self.patmodaddressbutton.place(relx=0.81, rely=0.6, anchor=tk.W)
            self.patmodcomplaintsbutton.place(relx=0.1, rely=0.75, anchor=tk.W)
            self.patmodtreatmentbutton.place(relx=0.28, rely=0.75, anchor=tk.W)
            self.patmodmedhisbutton.place(relx=0.47, rely=0.75, anchor=tk.W)
            self.patmodopcobutton.place(relx=0.63, rely=0.75, anchor=tk.W)
            self.patmodnameentry.place(relx=0.05, rely=0.65, anchor=tk.W)
            self.patmodageentry.place(relx=0.2, rely=0.65, anchor=tk.W)
            self.patmodgendermentry.place(relx=0.35, rely=0.65, anchor=tk.W)
            self.patmodgenderfentry.place(relx=0.39, rely=0.65, anchor=tk.W)
            self.patmodgenderoentry.place(relx=0.44, rely=0.65, anchor=tk.W)
            self.patmodrelationentry.place(relx=0.51, rely=0.65, anchor=tk.W)
            self.patmodrelativeentry.place(relx=0.66, rely=0.65, anchor=tk.W)
            self.patmodaddressentry.place(relx=0.81, rely=0.65, anchor=tk.W)
            self.patmodcomplaintsentry.place(relx=0.1, rely=0.8, anchor=tk.W)
            self.patmodtreatmententry.place(relx=0.28, rely=0.8, anchor=tk.W)
            self.patmodmedhisentry.place(relx=0.47, rely=0.8, anchor=tk.W)
            self.patmodopcoentry.place(relx=0.63, rely=0.8, anchor=tk.W)
            self.patmodifybutton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
            self.patsubmenucback.place(relx=0.05, rely=0.05, anchor=tk.CENTER)
            self.patselected = tk.StringVar()

            # Doctor Menu
            self.docbutton_1 = tk.Button(docmenu, text="Employ a Doctor", command=self.docsubmenua, width=50, height=2,
                                         bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docbutton_2 = tk.Button(docmenu, text="Resign a Doctor", command=self.docsubmenub, width=50, height=2,
                                         bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docbutton_3 = tk.Button(docmenu, text="Search or Modify Existing Doctor's Details",
                                         command=self.docsubmenuc, width=50, height=2, bg="#333333", fg="#FFFFFF",
                                         relief=tk.FLAT)
            self.docbutton_back = tk.Button(docmenu, text="Back to Main Menu", command=self.mainmenu, width=50,
                                            height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docbutton_1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
            self.docbutton_2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            self.docbutton_3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.docbutton_back.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

            # Doctor Sub Menu A
            self.demploylabel = tk.Label(docsubmenua, text="Enter Doctor's Details", bg="#1E1E1E", fg="#FFFFFF")
            self.dnamelabel = tk.Label(docsubmenua, text="Name", bg="#1E1E1E", fg="#FFFFFF")
            self.dgenderlabel = tk.Label(docsubmenua, text="Gender", bg="#1E1E1E", fg="#FFFFFF")
            self.ddoblabel = tk.Label(docsubmenua, text="DOB", bg="#1E1E1E", fg="#FFFFFF")
            self.dpaddresslabel = tk.Label(docsubmenua, text="Permanent Address", bg="#1E1E1E", fg="#FFFFFF")
            self.dmaddresslabel = tk.Label(docsubmenua, text="Mailing Address", bg="#1E1E1E", fg="#FFFFFF")
            self.dhighschoollabel = tk.Label(docsubmenua, text="High School", bg="#1E1E1E", fg="#FFFFFF")
            self.dmbbslabel = tk.Label(docsubmenua, text="M.B.B.S. from", bg="#1E1E1E", fg="#FFFFFF")
            self.dpgdegreelabel = tk.Label(docsubmenua, text="Post Graduate in", bg="#1E1E1E", fg="#FFFFFF")
            self.dpginstitutelabel = tk.Label(docsubmenua, text="Post Graduated from", bg="#1E1E1E", fg="#FFFFFF")
            self.dachievementslabel = tk.Label(docsubmenua, text="Achievements", bg="#1E1E1E", fg="#FFFFFF")
            self.dname = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dgender = tk.StringVar()
            self.dgenderm = tk.Radiobutton(docsubmenua, text="Male", variable=self.dgender, value="Male",
                                           relief=tk.FLAT, indicatoron=0, bg="#333333", fg="#FFFFFF",
                                           selectcolor="#1E1E1E")
            self.dgenderf = tk.Radiobutton(docsubmenua, text="Female", variable=self.dgender, value="Female",
                                           relief=tk.FLAT, indicatoron=0, bg="#333333", fg="#FFFFFF",
                                           selectcolor="#1E1E1E")
            self.dgendero = tk.Radiobutton(docsubmenua, text="Other", variable=self.dgender, value="Other",
                                           relief=tk.FLAT, indicatoron=0, bg="#333333", fg="#FFFFFF",
                                           selectcolor="#1E1E1E")
            self.day = tk.StringVar()
            days = []
            for z in range(1, 32):
                days.append(z)
            self.day.set(days[0])
            self.dday = tk.OptionMenu(docsubmenua, self.day, *days)
            self.dday.config(bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#333333",
                             activeforeground="#FFFFFF")
            self.dday["menu"].config(bg="#333333", fg="#FFFFFF", bd=0, activebackground="#1E1E1E")
            self.month = tk.StringVar()
            self.month.set("January")
            self.dmonth = tk.OptionMenu(docsubmenua, self.month, "January", "February", "March", "April", "May",
                                        "June", "July", "August", "September", "October", "November", "December")
            self.dmonth.config(bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#333333",
                               activeforeground="#FFFFFF")
            self.dmonth["menu"].config(bg="#333333", fg="#FFFFFF", bd=0, activebackground="#1E1E1E")
            self.year = tk.StringVar()
            self.year.set("2000")
            years = []
            for z in range(1900, 2001):
                years.append(z)
            self.dyear = tk.OptionMenu(docsubmenua, self.year, *years)
            self.dyear.config(bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#333333",
                              activeforeground="#FFFFFF")
            self.dyear["menu"].config(bg="#333333", fg="#FFFFFF", bd=0, activebackground="#1E1E1E")
            self.dpaddress = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dmaddress = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dhighschool = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dmbbs = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dpgdegree = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dpginstitute = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dachievements = tk.Entry(docsubmenua, relief=tk.FLAT, bg="#333333", fg="#FFFFFF")
            self.dsubmit = tk.Button(docsubmenua, text="Submit", relief=tk.FLAT, command=self.docsubmenuacom,
                                     bg="#333333", fg="#FFFFFF")
            self.docsubmenuaback = tk.Button(docsubmenua, text="< Back", relief=tk.FLAT, command=self.docmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.demploylabel.place(relx=0.50, rely=0.05, anchor=tk.CENTER)
            self.dnamelabel.place(relx=0.49, rely=0.21, anchor=tk.E)
            self.dgenderlabel.place(relx=0.49, rely=0.28, anchor=tk.E)
            self.ddoblabel.place(relx=0.49, rely=0.35, anchor=tk.E)
            self.dpaddresslabel.place(relx=0.49, rely=0.42, anchor=tk.E)
            self.dmaddresslabel.place(relx=0.49, rely=0.49, anchor=tk.E)
            self.dhighschoollabel.place(relx=0.49, rely=0.56, anchor=tk.E)
            self.dmbbslabel.place(relx=0.49, rely=0.63, anchor=tk.E)
            self.dpgdegreelabel.place(relx=0.49, rely=0.7, anchor=tk.E)
            self.dpginstitutelabel.place(relx=0.49, rely=0.77, anchor=tk.E)
            self.dachievementslabel.place(relx=0.49, rely=0.84, anchor=tk.E)
            self.dname.place(relx=0.51, rely=0.21, anchor=tk.W)
            self.dgenderm.place(relx=0.51, rely=0.28, anchor=tk.W)
            self.dgenderf.place(relx=0.55, rely=0.28, anchor=tk.W)
            self.dgendero.place(relx=0.60, rely=0.28, anchor=tk.W)
            self.dday.place(relx=0.51, rely=0.35, anchor=tk.W)
            self.dmonth.place(relx=0.54, rely=0.35, anchor=tk.W)
            self.dyear.place(relx=0.61, rely=0.35, anchor=tk.W)
            self.dpaddress.place(relx=0.51, rely=0.42, anchor=tk.W)
            self.dmaddress.place(relx=0.51, rely=0.49, anchor=tk.W)
            self.dhighschool.place(relx=0.51, rely=0.56, anchor=tk.W)
            self.dmbbs.place(relx=0.51, rely=0.63, anchor=tk.W)
            self.dpgdegree.place(relx=0.51, rely=0.7, anchor=tk.W)
            self.dpginstitute.place(relx=0.51, rely=0.77, anchor=tk.W)
            self.dachievements.place(relx=0.51, rely=0.84, anchor=tk.W)
            self.dsubmit.place(relx=0.50, rely=0.92, anchor=tk.CENTER)
            self.docsubmenuaback.place(relx=0.05, rely=0.05, anchor=tk.CENTER)

            # Doctor Sub Menu B
            self.docbsearchitems = []
            self.docbsearchbox = tk.Entry(docsubmenub, width=50, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docbsearchbutton = tk.Button(docsubmenub, text="Search", command=self.docbsearch, bg="#333333",
                                              fg="#FFFFFF", relief=tk.FLAT)
            self.docresignbutton = tk.Button(docsubmenub, text="Resign", command=self.docresign, bg="#333333",
                                             fg="#FFFFFF", relief=tk.FLAT)
            self.docsubmenubback = tk.Button(docsubmenub, text="< Back", relief=tk.FLAT, command=self.docmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.docbsearchbox.place(relx=0.45, rely=0.05, anchor=tk.CENTER)
            self.docbsearchbutton.place(relx=0.65, rely=0.05, anchor=tk.CENTER)
            self.docresignbutton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
            self.docsubmenubback.place(relx=0.05, rely=0.05, anchor=tk.CENTER)
            self.docselected = tk.StringVar()

            # Doctor Sub Menu C
            self.doccsearchitems = []
            self.doccsearchbox = tk.Entry(docsubmenuc, width=50, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.doccsearchbutton = tk.Button(docsubmenuc, text="Search", command=self.doccsearch, bg="#333333",
                                              fg="#FFFFFF", relief=tk.FLAT)
            self.docmodinfo = tk.Label(docsubmenuc, text="Select the Fields to Modify", bg="#1E1E1E", fg="#FFFFFF")
            self.docmodname = tk.IntVar()
            self.docmodnamebutton = tk.Checkbutton(docsubmenuc, text="Name", variable=self.docmodname, bg="#1E1E1E",
                                                   fg="#FFFFFF", activebackground="#1E1E1E",
                                                   activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.docmodnamebutton.deselect()
            self.docmodgender = tk.IntVar()
            self.docmodgenderbutton = tk.Checkbutton(docsubmenuc, text="Gender", variable=self.docmodgender,
                                                     bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                     activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.docmodgenderbutton.deselect()
            self.docmoddob = tk.IntVar()
            self.docmoddobbutton = tk.Checkbutton(docsubmenuc, text="Date of Birth", variable=self.docmoddob,
                                                  bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                  activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.docmoddobbutton.deselect()
            self.docmodpaddress = tk.IntVar()
            self.docmodpaddressbutton = tk.Checkbutton(docsubmenuc, text="Permanent Address",
                                                       variable=self.docmodpaddress, bg="#1E1E1E", fg="#FFFFFF",
                                                       activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                       selectcolor="#1E1E1E")
            self.docmodpaddressbutton.deselect()
            self.docmodmaddress = tk.IntVar()
            self.docmodmaddressbutton = tk.Checkbutton(docsubmenuc, text="Mailing Address",
                                                       variable=self.docmodmaddress, bg="#1E1E1E", fg="#FFFFFF",
                                                       activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                       selectcolor="#1E1E1E")
            self.docmodmaddressbutton.deselect()
            self.docmodhighschool = tk.IntVar()
            self.docmodhighschoolbutton = tk.Checkbutton(docsubmenuc, text="High School",
                                                         variable=self.docmodhighschool, bg="#1E1E1E", fg="#FFFFFF",
                                                         activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                         selectcolor="#1E1E1E")
            self.docmodhighschoolbutton.deselect()
            self.docmodmbbs = tk.IntVar()
            self.docmodmbbsbutton = tk.Checkbutton(docsubmenuc, text="M.B.B.S. from", variable=self.docmodmbbs,
                                                   bg="#1E1E1E", fg="#FFFFFF", activebackground="#1E1E1E",
                                                   activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.docmodmbbsbutton.deselect()
            self.docmodpgdegree = tk.IntVar()
            self.docmodpgdegreebutton = tk.Checkbutton(docsubmenuc, text="Post Graduate in",
                                                       variable=self.docmodpgdegree, bg="#1E1E1E", fg="#FFFFFF",
                                                       activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                       selectcolor="#1E1E1E")
            self.docmodpgdegreebutton.deselect()
            self.docmodpginstitute = tk.IntVar()
            self.docmodpginstitutebutton = tk.Checkbutton(docsubmenuc, text="Post Graduated from",
                                                          variable=self.docmodpginstitute, bg="#1E1E1E", fg="#FFFFFF",
                                                          activebackground="#1E1E1E", activeforeground="#FFFFFF",
                                                          selectcolor="#1E1E1E")
            self.docmodpginstitutebutton.deselect()
            self.docmodachievements = tk.IntVar()
            self.docmodachievementsbutton = tk.Checkbutton(docsubmenuc, text="Achievements",
                                                           variable=self.docmodachievements, bg="#1E1E1E",
                                                           fg="#FFFFFF", activebackground="#1E1E1E",
                                                           activeforeground="#FFFFFF", selectcolor="#1E1E1E")
            self.docmodachievementsbutton.deselect()
            self.docmodnameentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodgenderentry = tk.StringVar()
            self.docmodgendermentry = tk.Radiobutton(docsubmenuc, text="Male", variable=self.docmodgenderentry,
                                                     value="Male", indicatoron=0, bg="#333333", fg="#FFFFFF",
                                                     selectcolor="#1E1E1E")
            self.docmodgenderfentry = tk.Radiobutton(docsubmenuc, text="Female", variable=self.docmodgenderentry,
                                                     value="Female", indicatoron=0, bg="#333333", fg="#FFFFFF",
                                                     selectcolor="#1E1E1E")
            self.docmodgenderoentry = tk.Radiobutton(docsubmenuc, text="Other", variable=self.docmodgenderentry,
                                                     value="Other", indicatoron=0, bg="#333333", fg="#FFFFFF",
                                                     selectcolor="#1E1E1E")
            self.docmoddobday = tk.StringVar()
            days = []
            for z in range(1, 32):
                days.append(z)
            self.docmoddobday.set(days[0])
            self.docmoddobdayentry = tk.OptionMenu(docsubmenuc, self.docmoddobday, *days)
            self.docmoddobdayentry.config(bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0,
                                          activebackground="#333333", activeforeground="#FFFFFF")
            self.docmoddobdayentry["menu"].config(bg="#333333", fg="#FFFFFF", bd=0, activebackground="#1E1E1E")
            self.docmoddobmonth = tk.StringVar()
            self.docmoddobmonth.set("January")
            self.docmoddobmonthentry = tk.OptionMenu(docsubmenuc, self.docmoddobmonth, "January", "February", "March",
                                                     "April", "May", "June", "July", "August", "September", "October",
                                                     "November", "December")
            self.docmoddobmonthentry.config(bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0,
                                            activebackground="#333333", activeforeground="#FFFFFF")
            self.docmoddobmonthentry["menu"].config(bg="#333333", fg="#FFFFFF", bd=0, activebackground="#1E1E1E")
            self.docmoddobyear = tk.StringVar()
            self.docmoddobyear.set("2000")
            years = []
            for z in range(1900, 2001):
                years.append(z)
            self.docmoddobyearentry = tk.OptionMenu(docsubmenuc, self.docmoddobyear, *years)
            self.docmoddobyearentry.config(bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0,
                                           activebackground="#333333", activeforeground="#FFFFFF")
            self.docmoddobyearentry["menu"].config(bg="#333333", fg="#FFFFFF", bd=0, activebackground="#1E1E1E")
            self.docmodpaddressentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodmaddressentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodhighschoolentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodmbbsentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodpgdegreeentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodpginstituteentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodachievementsentry = tk.Entry(docsubmenuc, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.docmodifybutton = tk.Button(docsubmenuc, text="Modify", command=self.docmod, bg="#333333",
                                             fg="#FFFFFF", relief=tk.FLAT)
            self.docsubmenucback = tk.Button(docsubmenuc, text="< Back", relief=tk.FLAT, command=self.docmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.doccsearchbox.place(relx=0.45, rely=0.05, anchor=tk.CENTER)
            self.doccsearchbutton.place(relx=0.65, rely=0.05, anchor=tk.CENTER)
            self.docmodinfo.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
            self.docmodnamebutton.place(relx=0.05, rely=0.6, anchor=tk.W)
            self.docmodgenderbutton.place(relx=0.2, rely=0.6, anchor=tk.W)
            self.docmoddobbutton.place(relx=0.36, rely=0.6, anchor=tk.W)
            self.docmodpaddressbutton.place(relx=0.61, rely=0.6, anchor=tk.W)
            self.docmodmaddressbutton.place(relx=0.77, rely=0.6, anchor=tk.W)
            self.docmodhighschoolbutton.place(relx=0.14, rely=0.75, anchor=tk.W)
            self.docmodmbbsbutton.place(relx=0.29, rely=0.75, anchor=tk.W)
            self.docmodpgdegreebutton.place(relx=0.44, rely=0.75, anchor=tk.W)
            self.docmodpginstitutebutton.place(relx=0.59, rely=0.75, anchor=tk.W)
            self.docmodachievementsbutton.place(relx=0.74, rely=0.75, anchor=tk.W)
            self.docmodnameentry.place(relx=0.05, rely=0.65, anchor=tk.W)
            self.docmodgendermentry.place(relx=0.2, rely=0.65, anchor=tk.W)
            self.docmodgenderfentry.place(relx=0.24, rely=0.65, anchor=tk.W)
            self.docmodgenderoentry.place(relx=0.29, rely=0.65, anchor=tk.W)
            self.docmoddobdayentry.place(relx=0.36, rely=0.65, anchor=tk.W)
            self.docmoddobmonthentry.place(relx=0.42, rely=0.65, anchor=tk.W)
            self.docmoddobyearentry.place(relx=0.51, rely=0.65, anchor=tk.W)
            self.docmodpaddressentry.place(relx=0.61, rely=0.65, anchor=tk.W)
            self.docmodmaddressentry.place(relx=0.77, rely=0.65, anchor=tk.W)
            self.docmodhighschoolentry.place(relx=0.14, rely=0.8, anchor=tk.W)
            self.docmodmbbsentry.place(relx=0.29, rely=0.8, anchor=tk.W)
            self.docmodpgdegreeentry.place(relx=0.44, rely=0.8, anchor=tk.W)
            self.docmodpginstituteentry.place(relx=0.59, rely=0.8, anchor=tk.W)
            self.docmodachievementsentry.place(relx=0.74, rely=0.8, anchor=tk.W)
            self.docmodifybutton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
            self.docsubmenucback.place(relx=0.05, rely=0.05, anchor=tk.CENTER)
            self.docselected = tk.StringVar()

            # Database Menu
            self.datbutton_1 = tk.Button(datmenu, text="View All Patients' Database", command=self.datsubmenua,
                                         width=50, height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.datbutton_2 = tk.Button(datmenu, text="View All Doctors' Database", command=self.datsubmenub,
                                         width=50, height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.datbutton_3 = tk.Button(datmenu, text="View Currently Admitted Patients", command=self.datsubmenuc,
                                         width=50, height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.datbutton_4 = tk.Button(datmenu, text="View Currently Employed Doctors", command=self.datsubmenud,
                                         width=50, height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.datbutton_back = tk.Button(datmenu, text="Back to Main Menu", command=self.mainmenu, width=50,
                                            height=2, bg="#333333", fg="#FFFFFF", relief=tk.FLAT)
            self.datbutton_1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
            self.datbutton_2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            self.datbutton_3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.datbutton_4.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            self.datbutton_back.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

            # Database Sub Menu A
            self.datsubmenuaback = tk.Button(datsubmenua, text="< Back", relief=tk.FLAT, command=self.datmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.toppname = tk.Label(datsubmenua, text="Name", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                     font=("Arial Black", 8))
            self.toppage = tk.Label(datsubmenua, text="Age", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(1),
                                    font=("Arial Black", 8))
            self.toppgender = tk.Label(datsubmenua, text="Gender", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                       font=("Arial Black", 8))
            self.topprelation = tk.Label(datsubmenua, text="Relation", relief=tk.FLAT, bg="#1E1E1E",
                                         fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topprelative = tk.Label(datsubmenua, text="Relative", relief=tk.FLAT, bg="#1E1E1E",
                                         fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.toppaddress = tk.Label(datsubmenua, text="Address", relief=tk.FLAT, bg="#1E1E1E",
                                        fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppcomplaints = tk.Label(datsubmenua, text="Complaints", relief=tk.FLAT, bg="#1E1E1E",
                                           fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topptreatment = tk.Label(datsubmenua, text="Treatment Taken", relief=tk.FLAT, bg="#1E1E1E",
                                          fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppmedhis = tk.Label(datsubmenua, text="Medical History", relief=tk.FLAT, bg="#1E1E1E",
                                       fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.toppopco = tk.Label(datsubmenua, text="Past Medical Condition", relief=tk.FLAT, bg="#1E1E1E",
                                     fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppadmitdate = tk.Label(datsubmenua, text="Admitted on", relief=tk.FLAT, bg="#1E1E1E",
                                          fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.toppdischargedate = tk.Label(datsubmenua, text="Discharged on", relief=tk.FLAT, bg="#1E1E1E",
                                              fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppstatus = tk.Label(datsubmenua, text="Status", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                       font=("Arial Black", 8))
            self.datsubmenuaback.grid(row=0)
            self.toppname.grid(row=1, column=0)
            self.toppage.grid(row=1, column=1)
            self.toppgender.grid(row=1, column=2)
            self.topprelation.grid(row=1, column=3)
            self.topprelative.grid(row=1, column=4)
            self.toppaddress.grid(row=1, column=5)
            self.toppcomplaints.grid(row=1, column=6)
            self.topptreatment.grid(row=1, column=7)
            self.toppmedhis.grid(row=1, column=8)
            self.toppopco.grid(row=1, column=9)
            self.toppadmitdate.grid(row=1, column=10)
            self.toppdischargedate.grid(row=1, column=11)
            self.toppstatus.grid(row=1, column=12)

            # Database Sub Menu B
            self.datsubmenubback = tk.Button(datsubmenub, text="< Back", relief=tk.FLAT, command=self.datmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.topdname = tk.Label(datsubmenub, text="Name", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                     font=("Arial Black", 8))
            self.topdgender = tk.Label(datsubmenub, text="Gender", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(1),
                                       font=("Arial Black", 8))
            self.topddob = tk.Label(datsubmenub, text="Date Of Birth", relief=tk.FLAT, bg="#1E1E1E",
                                    fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdpaddress = tk.Label(datsubmenub, text="Permanent Address", relief=tk.FLAT, bg="#1E1E1E",
                                         fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdmaddress = tk.Label(datsubmenub, text="Mailing Address", relief=tk.FLAT, bg="#1E1E1E",
                                         fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdhighschool = tk.Label(datsubmenub, text="High School", relief=tk.FLAT, bg="#1E1E1E",
                                           fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdmbbs = tk.Label(datsubmenub, text="M.B.B.S. from", relief=tk.FLAT, bg="#1E1E1E",
                                     fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdpgdegree = tk.Label(datsubmenub, text="Post Graduate in", relief=tk.FLAT, bg="#1E1E1E",
                                         fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdpginstitute = tk.Label(datsubmenub, text="Post Graduated from", relief=tk.FLAT, bg="#1E1E1E",
                                            fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdachievements = tk.Label(datsubmenub, text="Achievements", relief=tk.FLAT, bg="#1E1E1E",
                                             fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topddoj = tk.Label(datsubmenub, text="Joined on", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                    font=("Arial Black", 8))
            self.topddor = tk.Label(datsubmenub, text="Resigned on", relief=tk.FLAT, bg="#1E1E1E",
                                    fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdstatus = tk.Label(datsubmenub, text="Status", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                       font=("Arial Black", 8))
            self.datsubmenubback.grid(row=0)
            self.topdname.grid(row=1, column=0)
            self.topdgender.grid(row=1, column=1)
            self.topddob.grid(row=1, column=2)
            self.topdpaddress.grid(row=1, column=3)
            self.topdmaddress.grid(row=1, column=4)
            self.topdhighschool.grid(row=1, column=5)
            self.topdmbbs.grid(row=1, column=6)
            self.topdpgdegree.grid(row=1, column=7)
            self.topdpginstitute.grid(row=1, column=8)
            self.topdachievements.grid(row=1, column=9)
            self.topddoj.grid(row=1, column=10)
            self.topddor.grid(row=1, column=11)
            self.topdstatus.grid(row=1, column=12)

            # Database Sub Menu C
            self.datsubmenucback = tk.Button(datsubmenuc, text="< Back", relief=tk.FLAT, command=self.datmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.toppnamec = tk.Label(datsubmenuc, text="Name", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                      font=("Arial Black", 8))
            self.toppagec = tk.Label(datsubmenuc, text="Age", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(1),
                                     font=("Arial Black", 8))
            self.toppgenderc = tk.Label(datsubmenuc, text="Gender", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                        font=("Arial Black", 8))
            self.topprelationc = tk.Label(datsubmenuc, text="Relation", relief=tk.FLAT, bg="#1E1E1E",
                                          fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topprelativec = tk.Label(datsubmenuc, text="Relative", relief=tk.FLAT, bg="#1E1E1E",
                                          fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.toppaddressc = tk.Label(datsubmenuc, text="Address", relief=tk.FLAT, bg="#1E1E1E",
                                         fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppcomplaintsc = tk.Label(datsubmenuc, text="Complaints", relief=tk.FLAT, bg="#1E1E1E",
                                            fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topptreatmentc = tk.Label(datsubmenuc, text="Treatment Taken", relief=tk.FLAT, bg="#1E1E1E",
                                           fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppmedhisc = tk.Label(datsubmenuc, text="Medical History", relief=tk.FLAT, bg="#1E1E1E",
                                        fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.toppopcoc = tk.Label(datsubmenuc, text="Past Medical Condition", relief=tk.FLAT, bg="#1E1E1E",
                                      fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppadmitdatec = tk.Label(datsubmenuc, text="Admitted on", relief=tk.FLAT, bg="#1E1E1E",
                                           fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.toppdischargedatec = tk.Label(datsubmenuc, text="Discharged on", relief=tk.FLAT, bg="#1E1E1E",
                                               fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.toppstatusc = tk.Label(datsubmenuc, text="Status", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                        font=("Arial Black", 8))
            self.datsubmenucback.grid(row=0, column=0)
            self.toppnamec.grid(row=1, column=0)
            self.toppagec.grid(row=1, column=1)
            self.toppgenderc.grid(row=1, column=2)
            self.topprelationc.grid(row=1, column=3)
            self.topprelativec.grid(row=1, column=4)
            self.toppaddressc.grid(row=1, column=5)
            self.toppcomplaintsc.grid(row=1, column=6)
            self.topptreatmentc.grid(row=1, column=7)
            self.toppmedhisc.grid(row=1, column=8)
            self.toppopcoc.grid(row=1, column=9)
            self.toppadmitdatec.grid(row=1, column=10)
            self.toppdischargedatec.grid(row=1, column=11)
            self.toppstatusc.grid(row=1, column=12)

            # Database Sub Menu D
            self.datsubmenudback = tk.Button(datsubmenud, text="< Back", relief=tk.FLAT, command=self.datmenu,
                                             bg="#333333", fg="#FFFFFF")
            self.topdnamed = tk.Label(datsubmenud, text="Name", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                      font=("Arial Black", 8))
            self.topdgenderd = tk.Label(datsubmenud, text="Gender", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(1),
                                        font=("Arial Black", 8))
            self.topddobd = tk.Label(datsubmenud, text="Date Of Birth", relief=tk.FLAT, bg="#1E1E1E",
                                     fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdpaddressd = tk.Label(datsubmenud, text="Permanent Address", relief=tk.FLAT, bg="#1E1E1E",
                                          fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdmaddressd = tk.Label(datsubmenud, text="Mailing Address", relief=tk.FLAT, bg="#1E1E1E",
                                          fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdhighschoold = tk.Label(datsubmenud, text="High School", relief=tk.FLAT, bg="#1E1E1E",
                                            fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdmbbsd = tk.Label(datsubmenud, text="M.B.B.S. from", relief=tk.FLAT, bg="#1E1E1E",
                                      fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdpgdegreed = tk.Label(datsubmenud, text="Post Graduate in", relief=tk.FLAT, bg="#1E1E1E",
                                          fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdpginstituted = tk.Label(datsubmenud, text="Post Graduated from", relief=tk.FLAT, bg="#1E1E1E",
                                             fg=self.bnwstripes(0), font=("Arial Black", 8))
            self.topdachievementsd = tk.Label(datsubmenud, text="Achievements", relief=tk.FLAT, bg="#1E1E1E",
                                              fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topddojd = tk.Label(datsubmenud, text="Joined on", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                     font=("Arial Black", 8))
            self.topddord = tk.Label(datsubmenud, text="Resigned on", relief=tk.FLAT, bg="#1E1E1E",
                                     fg=self.bnwstripes(1), font=("Arial Black", 8))
            self.topdstatusd = tk.Label(datsubmenud, text="Status", relief=tk.FLAT, bg="#1E1E1E", fg=self.bnwstripes(0),
                                        font=("Arial Black", 8))
            self.datsubmenudback.grid(row=0)
            self.topdnamed.grid(row=1, column=0)
            self.topdgenderd.grid(row=1, column=1)
            self.topddobd.grid(row=1, column=2)
            self.topdpaddressd.grid(row=1, column=3)
            self.topdmaddressd.grid(row=1, column=4)
            self.topdhighschoold.grid(row=1, column=5)
            self.topdmbbsd.grid(row=1, column=6)
            self.topdpgdegreed.grid(row=1, column=7)
            self.topdpginstituted.grid(row=1, column=8)
            self.topdachievementsd.grid(row=1, column=9)
            self.topddojd.grid(row=1, column=10)
            self.topddord.grid(row=1, column=11)
            self.topdstatusd.grid(row=1, column=12)

            # Loop Start
            mainframe.mainloop()

    def auth(self):
        __huser, __hpass = hashlib.sha512(str(self.loginuser.get())), hashlib.sha512(str(self.loginpass.get()))
        __hashuser, __hashpass = __huser.hexdigest(), __hpass.hexdigest()
        __thefile = open("resources\\config.pkl", "rb")
        __thestring = pickle.load(__thefile)
        __thefile.close()
        __thelist = __thestring.split(",")
        if __hashuser == __thelist[0] and __hashpass == __thelist[1]:
            self.raiseFrame(mainmenu)
            self.loginuser.delete(0, tk.END)
            self.loginpass.delete(0, tk.END)
            
    def insertFrame(self, frameList):
        for frame in frameList:
            frame.grid(row=0, column=0, sticky="nsew")
            self.raiseFrame(loginform)
            
    def raiseFrame(self, f):
        f.tkraise()
        
    def patsubmenuacom(self):
        patadmitted = backend().pat(self.pname.get(), self.page.get(), self.pgender.get(), self.prelation.get(),
                                    self.prelative.get(), self.paddress.get(), self.pcomplaints.get(),
                                    self.ptreatment.get(), self.pmedhis.get(), self.popco.get())
        if "pnameerr" in patadmitted:
            self.pname.config(bg="#7F0000")
        if "pageerr" in patadmitted:
            self.page.config(bg="#7F0000")
        if "pgendererr" in patadmitted:
            self.pgenderm.config(bg="#7F0000")
            self.pgenderf.config(bg="#7F0000")
            self.pgendero.config(bg="#7F0000")
        if "prelativeerr" in patadmitted:
            self.prelative.config(bg="#7F0000")
        if "paddresserr" in patadmitted:
            self.paddress.config(bg="#7F0000")
        if "pcomplaintserr" in patadmitted:
            self.pcomplaints.config(bg="#7F0000")
        if len(patadmitted) == 0:
            self.pname.delete(0, tk.END)
            self.page.delete(0, tk.END)
            self.prelative.delete(0, tk.END)
            self.paddress.delete(0, tk.END)
            self.pcomplaints.delete(0, tk.END)
            self.ptreatment.delete(0, tk.END)
            self.pmedhis.delete(0, tk.END)
            self.popco.delete(0, tk.END)
        
    def docsubmenuacom(self):
        docemployed = backend().doc(self.dname.get(), self.dgender.get(), self.day.get(), self.month.get(),
                                    self.year.get(), self.dpaddress.get(), self.dmaddress.get(),
                                    self.dhighschool.get(), self.dmbbs.get(), self.dpgdegree.get(),
                                    self.dpginstitute.get(), self.dachievements.get())
        if "dnameerr" in docemployed:
            self.dname.config(bg="#7F0000")
        if "dgendererr" in docemployed:
            self.dgenderm.config(bg="#7F0000")
            self.dgenderf.config(bg="#7F0000")
            self.dgendero.config(bg="#7F0000")
        if "dpaddresserr" in docemployed:
            self.dpaddress.config(bg="#7F0000")
        if "dmaddresserr" in docemployed:
            self.dmaddress.config(bg="#7F0000")
        if "dhighschoolerr" in docemployed:
            self.dhighschool.config(bg="#7F0000")
        if "dmbbserr" in docemployed:
            self.dmbbs.config(bg="#7F0000")
        if "dpgdegreeerr" in docemployed:
            self.dpgdegree.config(bg="#7F0000")
        if "dpginstituteerr" in docemployed:
            self.dpginstitute.config(bg="#7F0000")
        if len(docemployed) == 0:
            self.dname.delete(0, tk.END)
            self.day.set("1")
            self.month.set("January")
            self.year.set("2000")
            self.dpaddress.delete(0, tk.END)
            self.dmaddress.delete(0, tk.END)
            self.dhighschool.delete(0, tk.END)
            self.dmbbs.delete(0, tk.END)
            self.dpgdegree.delete(0, tk.END)
            self.dpginstitute.delete(0, tk.END)
            self.dachievements.delete(0, tk.END)
            
    def logout(self):
        self.raiseFrame(loginform)
        
    # Frame Raisers
    def mainmenu(self):
        self.raiseFrame(mainmenu)
        self.mainpatientsadmittednumber.config(text=str(backend().noofadmittedpatients()))
        self.maindoctorsemployednumber.config(text=str(backend().noofemployeddoctors()))
        
    def patmenu(self):
        self.raiseFrame(patmenu)
        
    def patsubmenua(self):
        self.raiseFrame(patsubmenua)
        
    def patsubmenub(self):
        self.raiseFrame(patsubmenub)
        
    def patsubmenuc(self):
        self.raiseFrame(patsubmenuc)
        
    def docmenu(self):
        self.raiseFrame(docmenu)
        
    def docsubmenua(self):
        self.raiseFrame(docsubmenua)
        
    def docsubmenub(self):
        self.raiseFrame(docsubmenub)
        
    def docsubmenuc(self):
        self.raiseFrame(docsubmenuc)
        
    def datmenu(self):
        self.raiseFrame(datmenu)
        
    def datsubmenua(self):
        self.raiseFrame(datsubmenua)
        self.datsubmenuafunc()
        
    def datsubmenub(self):
        self.raiseFrame(datsubmenub)
        self.datsubmenubfunc()

    def datsubmenuc(self):
        self.raiseFrame(datsubmenuc)
        self.datsubmenucfunc()

    def datsubmenud(self):
        self.raiseFrame(datsubmenud)
        self.datsubmenudfunc()
        
    # Functions for Functioning
    def patbsearch(self):
        self.patadmittedsearch(patsubmenub, self.patbsearchbox)

    def patcsearch(self):
        self.patsearch(patsubmenuc, self.patcsearchbox)

    def patsearch(self, location, searchbox):
        self.patselected = tk.StringVar()
        for item in self.patbsearchitems:
            item.destroy()
        data = []
        self.patbsearchitems = []
        patdat = open("resources\\patients.det", "r")
        for x in patdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            item = data[i][0]
            if searchbox.get().lower() in item.lower():
                self.patbsearchitem = tk.Radiobutton(location, value=str(data[i][0]),
                                                     text=str(data[i][0]+"\t"+data[i][1]+"\t"+data[i][2]),
                                                     variable=self.patselected, width=50, bg="#333333", fg="#FFFFFF",
                                                     indicatoron=0, selectcolor="#1E1E1E")
                self.patbsearchitems.append(self.patbsearchitem)
                self.patbsearchitem.place(relx=0.5, rely=(0.25+0.05*i), anchor=tk.CENTER)

    def patadmittedsearch(self, location, searchbox):
        self.patselected = tk.StringVar()
        for item in self.patbsearchitems:
            item.destroy()
        data = []
        self.patbsearchitems = []
        patdat = open("resources\\patients.det", "r")
        for x in patdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            item = data[i][0]
            if searchbox.get().lower() in item.lower() and "Admitted" in data[i]:
                self.patbsearchitem = tk.Radiobutton(location, value=str(data[i][0]),
                                                     text=str(data[i][0]+"\t"+data[i][1]+"\t"+data[i][2]),
                                                     variable=self.patselected, width=50, bg="#333333", fg="#FFFFFF",
                                                     indicatoron=0, selectcolor="#1E1E1E")
                self.patbsearchitems.append(self.patbsearchitem)
                self.patbsearchitem.place(relx=0.5, rely=(0.25+0.05*i), anchor=tk.CENTER)

    def patdischarge(self):
        dischargelist = []
        patdat = open("resources\\patients.det", "r")
        temp = open("resources\\temp.det", "w")
        for x in patdat:
            x.strip()
            dischargelist.append(x.split("~"))
        patdat.close()
        patdat = open("resources\\patients.det", "r")
        count = 0
        for line in patdat:
            if self.patselected.get() in dischargelist[count]:
                temp.write(dischargelist[count][0]+"~"+dischargelist[count][1]+"~"+dischargelist[count][2]+"~"+
                           dischargelist[count][3]+"~"+dischargelist[count][4]+"~"+dischargelist[count][5]+"~"+
                           dischargelist[count][6]+"~"+dischargelist[count][7]+"~"+dischargelist[count][8]+"~"+
                           dischargelist[count][9]+"~"+dischargelist[count][10]+"~"+backend().currentdate()+"~"+
                           "Discharged"+"\n")
                count += 1
            else:
                temp.write(line)
                count += 1
        patdat.close()
        temp.close()
        os.remove("resources\\patients.det")
        os.rename("resources\\temp.det", "resources\\patients.det")

    def patmod(self):
        modlist = []
        patdat = open("resources\\patients.det", "r")
        for x in patdat:
            x.strip()
            modlist.append(x.split("~"))
        patdat.close()
        patdat = open("resources\\doctors.det", "r")
        for x in range(len(modlist)):
            if self.patselected.get() in modlist[x]:
                patmodname = modlist[x][0]
                patmodage = modlist[x][1]
                patmodgender = modlist[x][2]
                patmodrelation = modlist[x][3]
                patmodrelative = modlist[x][4]
                patmodaddress = modlist[x][5]
                patmodcomplaints = modlist[x][6]
                patmodtreatment = modlist[x][7]
                patmodmedhis = modlist[x][8]
                patmodopco = modlist[x][9]
                patmodadmitdate = modlist[x][10]
                patmoddischargedate = modlist[x][11]
                patmodstatus = modlist[x][12]
                break
        patdat.close()
        if self.patmodname.get()==1:
            patmodname = str(self.patmodnameentry.get())
        if self.patmodage.get()==1:
            patmodage = str(self.patmodageentry.get())
        if self.patmodgender.get()==1:
            patmodgender = str(self.patmodgenderentry.get())
        if self.patmodrelation.get()==1:
            patmodrelation = str(self.patmodrelationentry.get())
        if self.patmodrelative.get()==1:
            patmodrelative = str(self.patmodrelativeentry.get())
        if self.patmodaddress.get()==1:
            patmodaddress = str(self.patmodaddressentry.get())
        if self.patmodcomplaints.get()==1:
            patmodcomplaints = str(self.patmodcomplaintsentry.get())
        if self.patmodtreatment.get()==1:
            patmodtreatment = str(self.patmodtreatmententry.get())
        if self.patmodmedhis.get()==1:
            patmodmedhis = str(self.patmodmedhisentry.get())
        if self.patmodopco.get()==1:
            patmodopco = str(self.patmodopcoentry.get())
        patdat = open("resources\\patients.det", "r")
        temp = open("resources\\temp.det", "w")
        count = 0
        for line in patdat:
            if self.patselected.get() in modlist[count]:
                temp.write(patmodname+"~"+patmodage+"~"+patmodgender+"~"+patmodrelation+"~"+patmodrelative+"~"+
                           patmodaddress+"~"+patmodcomplaints+"~"+patmodtreatment+"~"+patmodmedhis+"~"+
                           patmodopco+"~"+patmodadmitdate+"~"+patmoddischargedate+"~"+patmodstatus)
                count += 1
            else:
                temp.write(line)
                count += 1
        patdat.close()
        temp.close()

    def docbsearch(self):
        self.docemployedsearch(docsubmenub, self.docbsearchbox)

    def doccsearch(self):
        self.docsearch(docsubmenuc, self.doccsearchbox)

    def docsearch(self, location, searchbox):
        self.docselected = tk.StringVar()
        for item in self.docbsearchitems:
            item.destroy()
        data = []
        self.docbsearchitems = []
        self.tobesearched = searchbox.get()
        docdat = open("resources\\doctors.det", "r")
        for x in docdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            item = data[i][0]
            if self.tobesearched.lower() in item.lower():
                self.docbsearchitem = tk.Radiobutton(location, value=str(data[i][0]),
                                                     text=str(data[i][0]+"\t"+data[i][1]+"\t"+data[i][2]),
                                                     variable=self.docselected, width=50, bg="#333333", fg="#FFFFFF",
                                                     indicatoron=0, selectcolor="#1E1E1E")
                self.docbsearchitems.append(self.docbsearchitem)
                self.docbsearchitem.place(relx=0.5, rely=(0.25+0.05*i), anchor=tk.CENTER)

    def docemployedsearch(self, location, searchbox):
        self.docselected = tk.StringVar()
        for item in self.docbsearchitems:
            item.destroy()
        data = []
        self.docbsearchitems = []
        self.tobesearched = searchbox.get()
        docdat = open("resources\\doctors.det", "r")
        for x in docdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            item = data[i][0]
            if self.tobesearched.lower() in item.lower() and "Employed" in data[i]:
                self.docbsearchitem = tk.Radiobutton(location, value=str(data[i][0]),
                                                     text=str(data[i][0]+"\t"+data[i][1]+"\t"+data[i][2]),
                                                     variable=self.docselected, width=50, bg="#333333", fg="#FFFFFF",
                                                     indicatoron=0, selectcolor="#1E1E1E")
                self.docbsearchitems.append(self.docbsearchitem)
                self.docbsearchitem.place(relx=0.5, rely=(0.25+0.05*i), anchor=tk.CENTER)

    def docresign(self):
        resignlist = []
        docdat = open("resources\\doctors.det", "r")
        temp = open("resources\\temp.det", "w")
        for x in docdat:
            x.strip()
            resignlist.append(x.split("~"))
        docdat.close()
        docdat = open("resources\\doctors.det", "r")
        count = 0
        for line in docdat:
            if self.docselected.get() in resignlist[count]:
                temp.write(resignlist[count][0]+"~"+resignlist[count][1]+"~"+resignlist[count][2]+"~"+
                           resignlist[count][3]+"~"+resignlist[count][4]+"~"+resignlist[count][5]+"~"+
                           resignlist[count][6]+"~"+resignlist[count][7]+"~"+resignlist[count][8]+"~"+
                           resignlist[count][9]+"~"+resignlist[count][10]+"~"+backend().currentdate()+"~"+
                           "Resigned"+"\n")
                count += 1
            else:
                temp.write(line)
                count += 1
        docdat.close()
        temp.close()
        os.remove("resources\\doctors.det")
        os.rename("resources\\temp.det", "resources\\doctors.det")

    def docmod(self):
        modlist = []
        docdat = open("resources\\doctors.det", "r")
        for x in docdat:
            x.strip()
            modlist.append(x.split("~"))
        docdat.close()
        docdat = open("resources\\doctors.det", "r")
        count = 0
        for x in range(len(modlist)):
            if self.docselected.get() in modlist[x]:
                docmodname = modlist[x][0]
                docmodgender = modlist[x][1]
                docmoddob = modlist[x][2]
                docmodpaddress = modlist[x][3]
                docmodmaddress = modlist[x][4]
                docmodhighschool = modlist[x][5]
                docmodmbbs = modlist[x][6]
                docmodpgdegree = modlist[x][7]
                docmodpginstitute = modlist[x][8]
                docmodachievements = modlist[x][9]
                docmodjoindate = modlist[x][10]
                docmodresigndate = modlist[x][11]
                docmodstatus = modlist[x][12]
                break
        docdat.close()
        if self.docmodname.get()==1:
            docmodname = str(self.docmodnameentry.get())
        if self.docmodgender.get()==1:
            docmodgender = str(self.docmodgenderentry.get())
        if self.docmoddob.get()==1:
            docmoddob = str(self.docmoddobday.get()+"/"+self.docmoddobmonth.get()+"/"+self.docmoddobyear.get())
        if self.docmodpaddress.get()==1:
            docmodpaddress = str(self.docmodpaddressentry.get())
        if self.docmodmaddress.get()==1:
            docmodmaddress = str(self.docmodmaddressentry.get())
        if self.docmodhighschool.get()==1:
            docmodhighschool = str(self.docmodhighschoolentry.get())
        if self.docmodmbbs.get()==1:
            docmodmbbs = str(self.docmodmbbsentry.get())
        if self.docmodpgdegree.get()==1:
            docmodpgdegree = str(self.docmodpgdegreeentry.get())
        if self.docmodpginstitute.get()==1:
            docmodpginstitute = str(self.docmodpginstituteentry.get())
        if self.docmodachievements.get()==1:
            docmodachievements = str(self.docmodachievementsentry.get())
        docdat = open("resources\\doctors.det", "r")
        temp = open("resources\\temp.det", "w")
        count2 = 0
        for line in docdat:
            if self.docselected.get() in modlist[count2]:
                temp.write(docmodname+"~"+docmodgender+"~"+docmoddob+"~"+docmodpaddress+"~"+docmodmaddress+"~"+
                           docmodhighschool+"~"+docmodmbbs+"~"+docmodpgdegree+"~"+docmodpginstitute+"~"+
                           docmodachievements+"~"+docmodjoindate+"~"+docmodresigndate+"~"+docmodstatus)
                count2 += 1
            else:
                temp.write(line)
                count2 += 1
        docdat.close()
        temp.close()
        os.remove("resources\\doctors.det")
        os.rename("resources\\temp.det", "resources\\doctors.det")

    def datsubmenuafunc(self):
        data = []
        patdat = open("resources\\patients.det", "r")
        for x in patdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            for j in range(len(data[i])):
                datalabel = tk.Label(datsubmenua, text=data[i][j], relief=tk.FLAT, bg="#1E1E1E", fg=self.stripes(j))
                datalabel.grid(row=i+2, column=j)
                
    def datsubmenubfunc(self):
        data = []
        docdat = open("resources\\doctors.det", "r")
        for x in docdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            for j in range(len(data[i])):
                datalabel = tk.Label(datsubmenub, text=data[i][j], relief=tk.FLAT, bg="#1E1E1E", fg=self.stripes(j))
                datalabel.grid(row=i+2, column=j)

    def datsubmenucfunc(self):
        data = []
        patdat = open("resources\\patients.det", "r")
        for x in patdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            for j in range(len(data[i])):
                if "Admitted" in data[i]:
                    datalabel = tk.Label(datsubmenuc, text=data[i][j], relief=tk.FLAT, bg="#1E1E1E", fg=self.stripes(j))
                    datalabel.grid(row=i+2, column=j)

    def datsubmenudfunc(self):
        data = []
        docdat = open("resources\\doctors.det", "r")
        for x in docdat:
            x = x.strip()
            data.append(x.split("~"))
        for i in range(len(data)):
            for j in range(len(data[i])):
                if "Employed" in data[i]:
                    datalabel = tk.Label(datsubmenud, text=data[i][j], relief=tk.FLAT, bg="#1E1E1E", fg=self.stripes(j))
                    datalabel.grid(row=i+2, column=j)
                
    # Decorative Functions!!! YAAAAAAAAAAAAAAAAAAY.
    def bnwstripes(self, n):
        colors = ["#FFFFFF", "#BBBBBB"]
        return colors[n]

    def stripes(self, n):
        colors = ["#0094FF","#FF6A00"]
        return colors[n%2]

    def patenter(self, event):
        self.patlogol.configure(image=patlogo2)
        self.patlogol.photo = patlogo2
        
    def patleave(self, event):
        self.patlogol.configure(image=patlogo)
        self.patlogol.photo = patlogo
        
    def docenter(self, event):
        self.doclogol.configure(image=doclogo2)
        self.doclogol.photo = doclogo2
        
    def docleave(self, event):
        self.doclogol.configure(image=doclogo)
        self.doclogol.photo = doclogo
        
    def datenter(self, event):
        self.datlogol.configure(image=datlogo2)
        self.datlogol.photo = datlogo2
        
    def datleave(self, event):
        self.datlogol.configure(image=datlogo)
        self.datlogol.photo = datlogo

# Starter
window = tk.Tk()
window.title("Hospital Management System")
window.geometry("1024x576")
window.configure(background="#0E0E0E")
interface = frontend(window)