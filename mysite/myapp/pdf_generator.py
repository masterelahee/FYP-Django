import firebase_admin
from firebase_admin import credentials
import pyrebase 
import json
import pdfrw
from math import ceil


def pdf_generator(url_tofirebase,login_email_rn):
    
    config={
        "apiKey": "AIzaSyARTOEGZOikzGrk6f0jSkhCiXBx2FAKg78",
        "authDomain": "fyptheboyes.firebaseapp.com",
        "databaseURL": "https://fyptheboyes.firebaseio.com",
        "projectId": "fyptheboyes",
        "storageBucket": "fyptheboyes.appspot.com",
        "messagingSenderId": "1073113067983",
        "appId": "1:1073113067983:web:7564efc27471e46f65e2ba",
        "measurementId": "G-R0SJYKDBMZ",
        
    }
    print("IAFTER CONFIG")
    firebase=pyrebase.initialize_app(config)
    db=firebase.database()
 

    cred=credentials.Certificate('C:/Users/maste/OneDrive/Desktop/FYP/FYP-Django/mysite/myapp/firebasesdk.json')
    print("IAFTER CRED")
    
    print("AFTER THIS")
   
    PDF_OUTPUT_PATH = 'C:/Users/maste/OneDrive/Desktop/FYP/FYP-Django/mysite/myapp/pdf_reports/'+url_tofirebase +'.pdf'
    print("IAFTER PATH")
    f=[]

    extract = db.child(login_email_rn.replace(".","_")).child("scans").child(url_tofirebase)# rickyteama_tk or https___guthib_com
    for x in extract.get():
        f.append(x.val())

    json_fixed=json.dumps(f,indent=2)
    print(json_fixed)
    raw_data = json.loads(json_fixed)#raw_data is list

    data_dict = raw_data[2]#ip_info
    data_dict['ip']=raw_data[1]
    for key, value in raw_data[0].items():#head_found #value= sub dict
        if key=='server':
            data_dict[key]=value['contents']
        elif value['defined']==False:
            data_dict[key]='disabled'
        elif value['defined']==True:
            data_dict[key]='enabled'
        if len(value) !=3 :  
            for key2, value2 in raw_data[0][key].items():
                if key2=='discription':
                    data_dict[key+"desc"]=value2
        else:
            data_dict[key + "desc"]="none"

    
    print("pdfpath")
    PDF_TEMPLATE_PATH = 'C:/Users/maste/OneDrive/Desktop/FYP/FYP-Django/mysite/myapp/pdf_reports/templates/format_deep1.pdf'
    
    data_dict['port_open']=raw_data[4]#port_open

    #links_found
    links=raw_data[5]
    print('\n'.join(map(str, links)))
    data_dict['links_found']= ('\n'.join(map(str, links)))
        
    template_pdf = pdfrw.PdfReader(PDF_TEMPLATE_PATH)
    print(raw_data[3])
   
    issues=[]
    for key, value in raw_data[3].items():
        print(raw_data[3][key])
        if raw_data[3][key]=="Issues listed above.":
            data_dict['found_issue']=raw_data[3][key]
            
        elif raw_data[3][key]== "None":
            data_dict['found_issue']=raw_data[3][key]
        else:
            for key2, value2 in raw_data[3][key].items():
                issues.append(f'{key2.upper()} : {value2}')
            issues.append('\n--')
            print('\n'.join(issues))
            data_dict['found_issue']= ('\n'.join(issues))
    template_pdf = pdfrw.PdfReader(PDF_TEMPLATE_PATH)

    for page in range(len(template_pdf.pages)):
        annotations = template_pdf.pages[page]['/Annots']
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/T']:
                    key = annotation['/T'][1:-1]

                    if key in data_dict.keys():
                        annotation.update(pdfrw.PdfDict(AP=f'{key}', V=f'{data_dict[key]}'))

    pdfrw.PdfWriter().write(PDF_OUTPUT_PATH, template_pdf)
    print("pdf done")