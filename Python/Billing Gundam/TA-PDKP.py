from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib

#Part Function/event
    #fungsi numeric
def validate_entry(text):
    return text.isdecimal()
    #fungsi tombol hapus
def hapus():
    BarbatosEntry.delete(0,END) #penghapusan
    FreedomEntry.delete(0,END)
    RFreedomEntry.delete(0,END)
    ExiaEntry.delete(0,END)
    NuEntry.delete(0,END)
    RXEntry.delete(0,END)
    SazabiEntry.delete(0,END)

    PenelopeEntry.delete(0,END)
    AerialEntry.delete(0,END)
    CalibarnEntry.delete(0,END)
    DestinyEntry.delete(0,END)
    RX2Entry.delete(0,END)
    UnicornEntry.delete(0,END)
    PhenexEntry.delete(0,END)

    AstrayBEntry.delete(0,END)
    AileEntry.delete(0,END)
    EclipseEntry.delete(0,END)
    AssaultEntry.delete(0,END)
    ProvidenceEntry.delete(0,END)
    BarbatosMEntry.delete(0,END)
    ForceEntry.delete(0,END)

    BarbatosEntry.insert(0,0)   #pengisian ulang 0
    FreedomEntry.insert(0,0)
    RFreedomEntry.insert(0,0)
    ExiaEntry.insert(0,0)
    NuEntry.insert(0,0)
    RXEntry.insert(0,0)
    SazabiEntry.insert(0,0)

    PenelopeEntry.insert(0,0)
    AerialEntry.insert(0,0)
    CalibarnEntry.insert(0,0)
    DestinyEntry.insert(0,0)
    RX2Entry.insert(0,0)
    UnicornEntry.insert(0,0)
    PhenexEntry.insert(0,0)

    AstrayBEntry.insert(0,0)
    AileEntry.insert(0,0)
    EclipseEntry.insert(0,0)
    AssaultEntry.insert(0,0)
    ProvidenceEntry.insert(0,0)
    BarbatosMEntry.insert(0,0)
    ForceEntry.insert(0,0)

    SDtaxEntry.delete(0,END)    #penghapusan pajak
    HGtaxEntry.delete(0,END)
    MGtaxEntry.delete(0,END)

    SDpriceEntry.delete(0,END)  #penghapusan harga
    HGpriceEntry.delete(0,END)
    MGpriceEntry.delete(0,END)

    entryNama.delete(0,END) #penghapusan keterangan pembeli
    entryPhone.delete(0,END)
    entryBillnumber.delete(0,END)

    textarea.delete(1.0,END)

    #fungsi tombol email
def send_email():   #define send email
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(EntryPengirim.get(),EntryPassword.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(EntryPengirim.get(),EntryPenerima.get(),message)
            ob.quit()
            messagebox.showinfo('Berhasil','Billing berhasil dikirim!',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Terjadi kesalahan, silakan coba lagi',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Billing Kosong!')
    else:
        root1=Toplevel() #untuk membuat window lagi
        root1.grab_set #untuk memfokuskan interaksi di window top level
        root1.title('Email Sender')
        root1.config(bg='snow')
        root1.resizable(0,0)
        #Bagian Pengirim
        FramePengirim=LabelFrame(root1,text='PENGIRIM',font=('arial',13,'bold'),bd=5,bg='snow')
        FramePengirim.grid(row=0,column=0,padx=40,pady=20)

        LabelPengirim=Label(FramePengirim,text="Email Pengirim",font=('arial',10),bg='snow')
        LabelPengirim.grid(row=0,column=0,padx=10,pady=8)

        EntryPengirim=Entry(FramePengirim,font=('arial',10),bd=2,width=23,relief=RIDGE)
        EntryPengirim.grid(row=0,column=1,padx=10,pady=8)

        LabelPassword=Label(FramePengirim,text="Password",font=('arial',10),bg='snow')
        LabelPassword.grid(row=1,column=0,padx=10,pady=8)

        EntryPassword=Entry(FramePengirim,font=('arial',10),bd=2,width=23,relief=RIDGE,show='*')
        EntryPassword.grid(row=1,column=1,padx=10,pady=8)
        #Bagian Penerima
        FramePenerima=LabelFrame(root1,text='PENERIMA',font=('arial',13,'bold'),bd=5,bg='snow')
        FramePenerima.grid(row=1,column=0,padx=40,pady=20)

        LabelPenerima=Label(FramePenerima,text="Email Penerima",font=('arial',10),bg='snow')
        LabelPenerima.grid(row=0,column=0,padx=10,pady=8)

        EntryPenerima=Entry(FramePenerima,font=('arial',10),bd=2,width=23,relief=RIDGE)
        EntryPenerima.grid(row=0,column=1,padx=10,pady=8)

        LabelMessage=Label(FramePenerima,text="Message",font=('arial',10),bg='snow')
        LabelMessage.grid(row=1,column=0,padx=10,pady=8)
        
        email_textarea=Text(FramePenerima,font=('arial',10),bd=2,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('_',''))

        TombolSend=Button(root1,text='SEND',font=('arial',11,'bold'),width=15,command=send_gmail)
        TombolSend.grid(row=2,column=0,pady=20)
        root1.mainloop()

    #fungsi buat tombol print
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Billing Kosong!')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

    #fungsi buat search nomor billing
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==entryBillnumber.get():
            f=open(f'bills/{i}','r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Nomor Billing Invalid!')

#fungsi buat bikin folder billing
if not os.path.exists('bills'):
    os.mkdir('bills')
#Fungsi buat save nomor billing
def save_bill():
    global nomorbilling
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{nomorbilling}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Berhasil',f'nomor billing {nomorbilling} telah berhasil disimpan')
        nomorbilling=random.randint(500,1000)

nomorbilling=random.randint(500,1000)

    #Bagian billing list
def billing_list():
    if entryNama.get()==''or entryPhone.get()=='':
        messagebox.showerror('Error','Keterangan Pembeli Harus Ada!')
    elif SDpriceEntry.get()=='' or HGpriceEntry.get()=='' or MGpriceEntry.get()=='':
        messagebox.showerror('Error', 'Pilih Minimal Satu Produk!')
    elif SDpriceEntry.get()=='Rp0' and HGpriceEntry.get()=='Rp0' and MGpriceEntry.get()=='Rp0':
        messagebox.showerror('Error','Pilih Minimal Satu Produk!')
    else:
        textarea.delete(1.0,END)

        textarea.insert(END,'\t**Selamat Datang Pembeli**\n')
        textarea.insert(END,f'\nNomor Billing: {nomorbilling}\n')
        textarea.insert(END,f'\nNama Pembeli: {entryNama.get()}\n')
        textarea.insert(END,f'\nNomor Hp/Telp: {entryPhone.get()}\n')
        textarea.insert(END,'\n=============================================')
        textarea.insert(END,'Produk\t\t\tQTY\tHarga')
        textarea.insert(END,'\n=============================================')
        if BarbatosEntry.get()!='0':    #SD
            textarea.insert(END,f'\nSD Gund. Barbatos\t\t\t{BarbatosEntry.get()}\tRp{hargabarbatos}' )
        if FreedomEntry.get()!='0':
            textarea.insert(END,f'\nSD Gund. Freedom\t\t\t{FreedomEntry.get()}\tRp{hargafreedom}' )
        if RFreedomEntry.get()!='0':
            textarea.insert(END,f'\nSD Gund. R Freedom\t\t\t{RFreedomEntry.get()}\tRp{hargarfreedom}' )
        if ExiaEntry.get()!='0':
            textarea.insert(END,f'\nSD Gund. Exia\t\t\t{ExiaEntry.get()}\tRp{hargaexia}' )
        if NuEntry.get()!='0':
            textarea.insert(END,f'\nSD Gund. Nu\t\t\t{NuEntry.get()}\tRp{harganu}' )
        if RXEntry.get()!='0':
            textarea.insert(END,f'\nSD Gund. RX-78-2\t\t\t{RXEntry.get()}\tRp{hargarx782}' )
        if SazabiEntry.get()!='0':
            textarea.insert(END,f'\nSD Sazabi\t\t\t{SazabiEntry.get()}\tRp{hargasazabi}' )

        if PenelopeEntry.get()!='0':  #HG
            textarea.insert(END,f'\nHG Gund. Penelope\t\t\t{PenelopeEntry.get()}\tRp{hargapenelope}' )
        if AerialEntry.get()!='0':  
            textarea.insert(END,f'\nHG Gund. Aerial\t\t\t{AerialEntry.get()}\tRp{hargaaerial}' )
        if CalibarnEntry.get()!='0':  
            textarea.insert(END,f'\nHG Gund. Calibarn\t\t\t{CalibarnEntry.get()}\tRp{hargacalibarn}' )
        if DestinyEntry.get()!='0':  
            textarea.insert(END,f'\nHG Gund. Destiny\t\t\t{DestinyEntry.get()}\tRp{hargadestiny}' )
        if RX2Entry.get()!='0':  
            textarea.insert(END,f'\nHG Gund. RX-78-2\t\t\t{RX2Entry.get()}\tRp{hargarx2}' )
        if UnicornEntry.get()!='0':  
            textarea.insert(END,f'\nHG Gund. RX-0 Unicorn\t\t\t{UnicornEntry.get()}\tRp{hargaunicorn}' )
        if PhenexEntry.get()!='0':  
            textarea.insert(END,f'\nHG Gund. RX-0 3 Phenex\t\t\t{PhenexEntry.get()}\tRp{hargaphenex}' )

        if AstrayBEntry.get()!='0':  #MG
            textarea.insert(END,f'\nMG Gund. Astray Blue SR\t\t\t{AstrayBEntry.get()}\tRp{hargaastrayb}' )
        if AileEntry.get()!='0':  
            textarea.insert(END,f'\nMG Gund. Aile Strike\t\t\t{AileEntry.get()}\tRp{hargaaile}' )
        if EclipseEntry.get()!='0':  
            textarea.insert(END,f'\nMG Gund. Eclipse\t\t\t{EclipseEntry.get()}\tRp{hargaeclipse}' )
        if AssaultEntry.get()!='0':  
            textarea.insert(END,f'\nMG Gund. Assaultshroud\t\t\t{AssaultEntry.get()}\tRp{hargaassault}' )
        if ProvidenceEntry.get()!='0':  
            textarea.insert(END,f'\nMG Gund. Providence\t\t\t{ProvidenceEntry.get()}\tRp{hargaprovidence}' )
        if BarbatosMEntry.get()!='0':  
            textarea.insert(END,f'\nMG Gund. Barbatos\t\t\t{BarbatosMEntry.get()}\tRp{hargabarbatosm}' )
        if ForceEntry.get()!='0':  
            textarea.insert(END,f'\nMG Gund. Force Impulse\t\t\t{ForceEntry.get()}\tRp{hargaforce}' )
        textarea.insert(END,'\n_____________________________________________')

        if SDtaxEntry.get()!='Rp0.0':
            textarea.insert(END,f'\nPajak SD\t\t\t\t{SDtaxEntry.get()}')
        if HGtaxEntry.get()!='Rp0.0':
            textarea.insert(END,f'\nPajak HG\t\t\t\t{HGtaxEntry.get()}')
        if MGtaxEntry.get()!='Rp0.0':
            textarea.insert(END,f'\nPajak MG\t\t\t\t{MGtaxEntry.get()}')
        textarea.insert(END,f'\nTotal Tagihan \t\t\t\tRp{totaltagihan}')
        textarea.insert(END,'\n_____________________________________________')
        save_bill()

def total():
    global hargabarbatos,hargafreedom,hargarfreedom,hargaexia,harganu,hargarx782,hargasazabi
    global hargapenelope,hargaaerial,hargacalibarn,hargadestiny,hargarx2,hargaunicorn,hargaphenex
    global hargaastrayb,hargaaile,hargaeclipse,hargaassault,hargaprovidence,hargabarbatosm,hargaforce
    global totaltagihan

    #Harga SD
    hargabarbatos=int(BarbatosEntry.get())*210000
    hargafreedom=int(FreedomEntry.get())*99000
    hargarfreedom=int(RFreedomEntry.get())*125000
    hargaexia=int(ExiaEntry.get())*100000
    harganu=int(NuEntry.get())*100000
    hargarx782=int(RXEntry.get())*129000
    hargasazabi=int(SazabiEntry.get())*99000

    totalhargaSD=hargabarbatos+hargafreedom+hargarfreedom+hargaexia+harganu+hargarx782+hargasazabi
    SDpriceEntry.delete(0,END)
    SDpriceEntry.insert(0,'Rp'+str(totalhargaSD))
    pajakSD=totalhargaSD*0.03
    SDtaxEntry.delete(0,END)
    SDtaxEntry.insert(0,'Rp'+str(pajakSD))

    #Harga HG
    hargapenelope=int(PenelopeEntry.get())*830000
    hargaaerial=int(AerialEntry.get())*375000
    hargacalibarn=int(CalibarnEntry.get())*620000
    hargadestiny=int(DestinyEntry.get())*475000
    hargarx2=int(RX2Entry.get())*170000
    hargaunicorn=int(UnicornEntry.get())*429000
    hargaphenex=int(PhenexEntry.get())*660000

    totalhargaHG=hargapenelope+hargaaerial+hargacalibarn+hargadestiny+hargarx2+hargaunicorn+hargaphenex
    HGpriceEntry.delete(0,END)
    HGpriceEntry.insert(0,'Rp'+str(totalhargaHG))
    pajakHG=totalhargaHG*0.02
    HGtaxEntry.delete(0,END)
    HGtaxEntry.insert(0,'Rp'+str(pajakHG))

    #Harga MG
    hargaastrayb=int(AstrayBEntry.get())*720000
    hargaaile=int(AileEntry.get())*720000
    hargaeclipse=int(EclipseEntry.get())*800000
    hargaassault=int(AssaultEntry.get())*693000
    hargaprovidence=int(ProvidenceEntry.get())*969000
    hargabarbatosm=int(BarbatosMEntry.get())*850000
    hargaforce=int(ForceEntry.get())*742500

    totalhargaMG=hargaastrayb+hargaaile+hargaeclipse+hargaassault+hargaprovidence+hargabarbatosm+hargaforce
    MGpriceEntry.delete(0,END)
    MGpriceEntry.insert(0,'Rp'+str(totalhargaMG))
    pajakMG=totalhargaMG*0.01
    MGtaxEntry.delete(0,END)
    MGtaxEntry.insert(0,'Rp'+str(pajakMG))

    totaltagihan=totalhargaSD+totalhargaHG+totalhargaMG+pajakSD+pajakHG+pajakMG
    

#Part GUI
root=Tk()
root.title('GUNPLA Store Bill System')
root.geometry('1280x720')
root.iconbitmap('F:\KULIAH\DKP\TA\Python\Billing Gundam\icon.ico')
headingLabel=Label(root,text='GUNPLA Store Billing System',font=('franklin gothic',20,'bold','italic'),bg='snow',bd=10,relief=FLAT)
headingLabel.pack(fill=X)

#Bagian Data Pembeli
frame_data_pembeli=LabelFrame(root,text='Keterangan Pembeli',font=('franklin gothic',12,'bold'),fg='gold',bd=8,relief=FLAT,bg='dodgerblue2')
frame_data_pembeli.pack(fill=X)

labelNama=Label(frame_data_pembeli,text='Nama',font=('franklin gothic',10),bg='dodgerblue2',fg='snow')
labelNama.grid(row=0,column=0,padx=20)

entryNama=Entry(frame_data_pembeli,font=('arial',10),bd=2,width=18)
entryNama.grid(row=0,column=1)

labelPhone=Label(frame_data_pembeli,text='No.Hp/Telp',font=('franklin gothic',10),bg='dodgerblue2',fg='snow')
labelPhone.grid(row=0,column=2,padx=20,pady=2)

entryPhone=Entry(frame_data_pembeli,font=('arial',10),bd=2,width=18,validate="key",validatecommand=(root.register(validate_entry), "%S"))
entryPhone.grid(row=0,column=3)

labelBillnumber=Label(frame_data_pembeli,text='Nomor Billing',font=('franklin gothic',10),bg='dodgerblue2',fg='snow')
labelBillnumber.grid(row=0,column=4,padx=20,pady=2)

entryBillnumber=Entry(frame_data_pembeli,font=('arial',10),bd=2,width=18,validate="key",validatecommand=(root.register(validate_entry), "%S"))
entryBillnumber.grid(row=0,column=5)

tombolSearch=Button(frame_data_pembeli,text='SEARCH',bd=2,command=search_bill)
tombolSearch.grid(row=0,column=6,padx=20,pady=8)

#Bagian Seleksi Produk
frameProduk=Frame(root)
frameProduk.pack()

#SD Grade
SDFrame=LabelFrame(frameProduk,text='SD',font=('franklin gothic',12,'bold'),fg='gold',bd=2,relief='ridge',bg='gray22')
SDFrame.grid(row=0,column=0)

BarbatosLabel=Label(SDFrame,text='SD Gund. Barbatos',font=('franklin gothic',10),bg='gray22',fg='snow')
BarbatosLabel.grid(row=0,column=0,pady=9,padx=10)

BarbatosEntry=Entry(SDFrame,font=('arial',10),width=10,bd=2)
BarbatosEntry.grid(row=0,column=1,pady=9,padx=10)
BarbatosEntry.insert(0,0)

FreedomLabel=Label(SDFrame,text='SD Gund. S Freedom',font=('franklin gothic',10),bg='gray22',fg='snow')
FreedomLabel.grid(row=1,column=0,pady=9,padx=10)

FreedomEntry=Entry(SDFrame,font=('arial',10),width=10,bd=2)
FreedomEntry.grid(row=1,column=1,pady=9,padx=10)
FreedomEntry.insert(0,0)

RFreedomLabel=Label(SDFrame,text='SD Gund. R Freedom',font=('franklin gothic',10),bg='gray22',fg='snow')
RFreedomLabel.grid(row=2,column=0,pady=9,padx=10)

RFreedomEntry=Entry(SDFrame,font=('arial',10),width=10,bd=2)
RFreedomEntry.grid(row=2,column=1,pady=9,padx=10)
RFreedomEntry.insert(0,0)

ExiaLabel=Label(SDFrame,text='SD Gund. Exia',font=('franklin gothic',10),bg='gray22',fg='snow')
ExiaLabel.grid(row=3,column=0,pady=9,padx=10)

ExiaEntry=Entry(SDFrame,font=('arial',10),width=10,bd=2)
ExiaEntry.grid(row=3,column=1,pady=9,padx=10)
ExiaEntry.insert(0,0)

NuLabel=Label(SDFrame,text='SD Gund. Nu',font=('franklin gothic',10),bg='gray22',fg='snow')
NuLabel.grid(row=4,column=0,pady=9,padx=10)

NuEntry=Entry(SDFrame,font=('arial',10),width=10,bd=2)
NuEntry.grid(row=4,column=1,pady=9,padx=10)
NuEntry.insert(0,0)

RXLabel=Label(SDFrame,text='SD Gund. RX-78-2',font=('franklin gothic',10),bg='gray22',fg='snow')
RXLabel.grid(row=5,column=0,pady=9,padx=10)

RXEntry=Entry(SDFrame,font=('arial',10),width=10,bd=2)
RXEntry.grid(row=5,column=1,pady=9,padx=10)
RXEntry.insert(0,0)

sazabiLabel=Label(SDFrame,text='SD Sazabi',font=('franklin gothic',10),bg='gray22',fg='snow')
sazabiLabel.grid(row=6,column=0,pady=9,padx=10)

SazabiEntry=Entry(SDFrame,font=('arial',10),width=10,bd=2)
SazabiEntry.grid(row=6,column=1,pady=9,padx=10)
SazabiEntry.insert(0,0)

#HG grade
HGFrame=LabelFrame(frameProduk,text='HG',font=('franklin gothic',12,'bold'),fg='gold',bd=2,relief='ridge',bg='gray22')
HGFrame.grid(row=0,column=1)

PenelopeLabel=Label(HGFrame,text='HG Gund. Penelope',font=('franklin gothic',10),bg='gray22',fg='snow')
PenelopeLabel.grid(row=0,column=0,pady=9,padx=10)

PenelopeEntry=Entry(HGFrame,font=('arial',10),width=10,bd=2)
PenelopeEntry.grid(row=0,column=1,pady=9,padx=10)
PenelopeEntry.insert(0,0)

AerialLabel=Label(HGFrame,text='HG Gund. Aerial',font=('franklin gothic',10),bg='gray22',fg='snow')
AerialLabel.grid(row=1,column=0,pady=9,padx=10)

AerialEntry=Entry(HGFrame,font=('arial',10),width=10,bd=2)
AerialEntry.grid(row=1,column=1,pady=9,padx=10)
AerialEntry.insert(0,0)

CalibarnLabel=Label(HGFrame,text='HG Gund. Calibarn',font=('franklin gothic',10),bg='gray22',fg='snow')
CalibarnLabel.grid(row=2,column=0,pady=9,padx=10)

CalibarnEntry=Entry(HGFrame,font=('arial',10),width=10,bd=2)
CalibarnEntry.grid(row=2,column=1,pady=9,padx=10)
CalibarnEntry.insert(0,0)

DestinyLabel=Label(HGFrame,text='HG Gund. ZGMF-X42S Destiny',font=('franklin gothic',10),bg='gray22',fg='snow')
DestinyLabel.grid(row=3,column=0,pady=9,padx=10)

DestinyEntry=Entry(HGFrame,font=('arial',10),width=10,bd=2)
DestinyEntry.grid(row=3,column=1,pady=9,padx=10)
DestinyEntry.insert(0,0)

RX2Label=Label(HGFrame,text='HG Gund. RX-7-2',font=('franklin gothic',10),bg='gray22',fg='snow')
RX2Label.grid(row=4,column=0,pady=9,padx=10)

RX2Entry=Entry(HGFrame,font=('arial',10),width=10,bd=2)
RX2Entry.grid(row=4,column=1,pady=9,padx=10)
RX2Entry.insert(0,0)

UnicornLabel=Label(HGFrame,text='HG Gund. RX-0 Unicorn',font=('franklin gothic',10),bg='gray22',fg='snow')
UnicornLabel.grid(row=5,column=0,pady=9,padx=10)

UnicornEntry=Entry(HGFrame,font=('arial',10),width=10,bd=2)
UnicornEntry.grid(row=5,column=1,pady=9,padx=10)
UnicornEntry.insert(0,0)

PhenexLabel=Label(HGFrame,text='HG Gund. RX-0 03 Phenex',font=('franklin gothic',10),bg='gray22',fg='snow')
PhenexLabel.grid(row=6,column=0,pady=9,padx=10)

PhenexEntry=Entry(HGFrame,font=('arial',10),width=10,bd=2)
PhenexEntry.grid(row=6,column=1,pady=9,padx=10)
PhenexEntry.insert(0,0)

#MG Grade
MGFrame=LabelFrame(frameProduk,text='MG',font=('franklin gothic',12,'bold'),fg='gold',bd=2,relief='ridge',bg='gray22')
MGFrame.grid(row=0,column=2)

AstrayBLabel=Label(MGFrame,text='MG Gund. Astray Blue F SR',font=('franklin gothic',10),bg='gray22',fg='snow')
AstrayBLabel.grid(row=0,column=0,pady=9,padx=10)

AstrayBEntry=Entry(MGFrame,font=('arial',10),width=10,bd=2)
AstrayBEntry.grid(row=0,column=1,pady=9,padx=10)
AstrayBEntry.insert(0,0)

AileLabel=Label(MGFrame,text='MG Gund. Aile Strike',font=('franklin gothic',10),bg='gray22',fg='snow')
AileLabel.grid(row=1,column=0,pady=9,padx=10)

AileEntry=Entry(MGFrame,font=('arial',10),width=10,bd=2)
AileEntry.grid(row=1,column=1,pady=9,padx=10)
AileEntry.insert(0,0)

EclipseLabel=Label(MGFrame,text='MG Gund. Eclipse',font=('franklin gothic',10),bg='gray22',fg='snow')
EclipseLabel.grid(row=2,column=0,pady=9,padx=10)

EclipseEntry=Entry(MGFrame,font=('arial',10),width=10,bd=2)
EclipseEntry.grid(row=2,column=1,pady=9,padx=10)
EclipseEntry.insert(0,0)

AssaultLabel=Label(MGFrame,text='MG Gund. Assaultshroud',font=('franklin gothic',10),bg='gray22',fg='snow')
AssaultLabel.grid(row=3,column=0,pady=9,padx=10)

AssaultEntry=Entry(MGFrame,font=('arial',10),width=10,bd=2)
AssaultEntry.grid(row=3,column=1,pady=9,padx=10)
AssaultEntry.insert(0,0)

ProvidenceLabel=Label(MGFrame,text='MG Gund. Providence',font=('franklin gothic',10),bg='gray22',fg='snow')
ProvidenceLabel.grid(row=4,column=0,pady=9,padx=10)

ProvidenceEntry=Entry(MGFrame,font=('arial',10),width=10,bd=2)
ProvidenceEntry.grid(row=4,column=1,pady=9,padx=10)
ProvidenceEntry.insert(0,0)

BarbatosMLabel=Label(MGFrame,text='MG Gund. Barbatos',font=('franklin gothic',10),bg='gray22',fg='snow')
BarbatosMLabel.grid(row=5,column=0,pady=9,padx=10)

BarbatosMEntry=Entry(MGFrame,font=('arial',10),width=10,bd=2)
BarbatosMEntry.grid(row=5,column=1,pady=9,padx=10)
BarbatosMEntry.insert(0,0)

ForceLabel=Label(MGFrame,text='MG Gund. Force Impulse',font=('franklin gothic',10),bg='gray22',fg='snow')
ForceLabel.grid(row=6,column=0,pady=9,padx=10)

ForceEntry=Entry(MGFrame,font=('arial',10),width=10,bd=2)
ForceEntry.grid(row=6,column=1,pady=9,padx=10)
ForceEntry.insert(0,0)

#Bill Frame
billFrame=Frame(frameProduk,bd=3,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billLabel=Label(billFrame,text='Billing List',font=('franklin gothic',10),bd=7,relief=GROOVE)
billLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame, height=17,width=45,yscrollcommand=scrollbar.set) #scrollbar.set untuk set scrollbar dalam textarea
textarea.pack()
scrollbar.config(command=textarea.yview)

#Frame billmenu
billmenuFrame=LabelFrame(root,text='Bill Menu',font=('franklin gothic',12,'bold'),fg='RoyalBlue4',bd=2,relief='ridge',bg='gold')
billmenuFrame.pack(fill=X)

SDpriceLabel=Label(billmenuFrame,text='Harga Grade SD',font=('franklin gothic',10,'bold'),bg='gold',fg='SkyBlue4')
SDpriceLabel.grid(row=0,column=0,pady=9,padx=10)

SDpriceEntry=Entry(billmenuFrame,font=('arial',10),width=10,bd=2)
SDpriceEntry.grid(row=0,column=1,pady=9,padx=10)

HGpriceLabel=Label(billmenuFrame,text='Harga Grade HG',font=('franklin gothic',10,'bold'),bg='gold',fg='SkyBlue4')
HGpriceLabel.grid(row=1,column=0,pady=9,padx=10)

HGpriceEntry=Entry(billmenuFrame,font=('arial',10),width=10,bd=2)
HGpriceEntry.grid(row=1,column=1,pady=9,padx=10)

MGpriceLabel=Label(billmenuFrame,text='Harga Grade MG',font=('franklin gothic',10,'bold'),bg='gold',fg='SkyBlue4')
MGpriceLabel.grid(row=2,column=0,pady=9,padx=10)

MGpriceEntry=Entry(billmenuFrame,font=('arial',10),width=10,bd=2)
MGpriceEntry.grid(row=2,column=1,pady=9,padx=10)

SDtaxLabel=Label(billmenuFrame,text='Pajak Grade SD',font=('franklin gothic',10,'bold'),bg='gold',fg='SkyBlue4')
SDtaxLabel.grid(row=0,column=2,pady=9,padx=10)

SDtaxEntry=Entry(billmenuFrame,font=('arial',10),width=10,bd=2)
SDtaxEntry.grid(row=0,column=3,pady=9,padx=10)

HGtaxLabel=Label(billmenuFrame,text='Pajak Grade HG',font=('franklin gothic',10,'bold'),bg='gold',fg='SkyBlue4')
HGtaxLabel.grid(row=1,column=2,pady=9,padx=10)

HGtaxEntry=Entry(billmenuFrame,font=('arial',10),width=10,bd=2)
HGtaxEntry.grid(row=1,column=3,pady=9,padx=10)

MGtaxLabel=Label(billmenuFrame,text='Pajak Grade MG',font=('franklin gothic',10,'bold'),bg='gold',fg='SkyBlue4')
MGtaxLabel.grid(row=2,column=2,pady=9,padx=10)

MGtaxEntry=Entry(billmenuFrame,font=('arial',10),width=10,bd=2)
MGtaxEntry.grid(row=2,column=3,pady=9,padx=10)

frameButton=Frame(billmenuFrame,bd=2,relief=GROOVE)
frameButton.grid(row=0,column=4,rowspan=3)

tombolTotal=Button(frameButton,text='Total',font=('arial',11,'bold'),bg='red',fg='snow',bd=5,width=8,pady=7,command=total)
tombolTotal.grid(row=0,column=0,pady=10,padx=5)

tombolBill=Button(frameButton,text='Bill',font=('arial',11,'bold'),bg='red',fg='snow',bd=5,width=8,pady=7,command=billing_list)
tombolBill.grid(row=0,column=1,pady=10,padx=5)

tombolemail=Button(frameButton,text='Email',font=('arial',11,'bold'),bg='red',fg='snow',bd=5,width=8,pady=7,command=send_email)
tombolemail.grid(row=0,column=2,pady=10,padx=5)

tombolprint=Button(frameButton,text='Print',font=('arial',11,'bold'),bg='red',fg='snow',bd=5,width=8,pady=7,command=print_bill)
tombolprint.grid(row=0,column=3,pady=10,padx=5)

tombolhapus=Button(frameButton,text='Hapus',font=('arial',11,'bold'),bg='red',fg='snow',bd=5,width=8,pady=7,command=hapus)
tombolhapus.grid(row=0,column=4,pady=10,padx=5)

root.mainloop()
