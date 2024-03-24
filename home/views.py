from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact, MumbaiCounselling, Aniket, Samkit, Swift, Others, PaymentRecords
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'colleges': [
            {
                "img": "vjti.jpg",
                "institute": "Veeramata Jijabai Technological Institute",
                "caption": "VJTI is the joint best engineering college in Maharashtra. It is located in Mumbai and is known for its campus, crowd, events, placements. VJTI has a strong alumni network and many famous people studied here.",
            },
            {
                "img": "coep.jpg",
                "institute": "COEP Technological University",
                "caption": "COEP is the joint best engineering college in Maharashtra. It is located in Pune and is best known for its campus, crowd and placements. The person after whom Engineering Day is observed, Sir M. Visvesvaraya, studied here.",
            },
            {
                "img": "ict.webp",
                "institute": "Institute of Chemical Technology",
                "caption": "ICT is the best college for Pharmacy in Maharashtra and the best college for Chemical Engineering in India. It is a deemed university which is best known for its research scope and academics.",
            },

        ],

        'services': [
            {
                "name": "Notes",
                "image": "notes.png",
                "color": "#99e6ff",
                "description": "Here you'll find notes related to MHT-CET, Engineering and Pharmacy.",
            },
            {
                "name": "Webinars",
                "image": "webinars.png",
                "color": "ffb399",
                "description": "We conduct various webinars to help students in their MHT-CET preparation and make them understand the admission process and provide them knowledge regarding colleges and areas of study.",
            },
            {
                "name": "Mock Tests",
                "image": "mocks.png",
                "color": "#99ff99",
                "description": "We conduct mock tests on our telegram channel. We have more than 50 mock tests subjectwise and chapterwise.",
            },
            {
                "name": "Personal Guidance",
                "image": "guidance.png",
                "color": "#cc99ff",
                "description": "Every child under our guidance gets personal support where they can share their doubts regarding their studies, admission process.",
            },
            {
                "name": "Option List Making",
                "image": "list.png",
                "color": "#ffff99",
                "description": "Every student who is a part of the counselling sessions is provided with a personal college list containing their desired college choices based on their score, location and many other factors.",
            },
            {
                "name": "Diverse Alumni Network",
                "image": "network.png",
                "color": "#ffcc99",
                "description": "We have a huge alumni network consisting of ex-students part of our sessions to whom students can reach out in case they get alloted with a college in the same area as them.",
            },
        ],

        'cards': [
            {
                "photo": "omkar.jpg",
                "title": "Messiahs",
                "description": "I had lost hopes due to my low score. But Swift UnderGrads came in at the right time and helped me to get admission!",
                "name": "OMKAR SHINDE",
                "college": "P.G. COLLEGE OF PHARMACEUTICAL SCIENCE AND RESEARCH",
            },
            {
                "photo": "prathamesh.jpg",
                "title": "Amazing experience",
                "description": "It was quiet a great experience with Swift UnderGrads which was much better than other paid guidance. Due to their team, I got admission in  a good government college and I am enjoying my college life!",
                "name": "PRATHAMESH BANNE",
                "college": "GOVERNMENT COLLEGE OF ENGINEERING, AMRAVATI",
            },
            {
                "photo": "pratik.jpg",
                "title": "Knowledgeable people",
                "description": "Swift Undergrads guided me till end in my admission process. They provided me information of various colleges in Maharashtra, their placement record, campus, faculties, cutoffs and much more . They personally answered my each and every query with detailed information, through great analysis. They also gave me information about various branches of engineering and guided me to choose them wisely. I am thankful to Swift Undergrads for their sincere efforts to help many students like me.",
                "name": "PRATIK MAGDUM",
                "college": "DKTE SOCIETY'S TEXTILE & ENGINEERING INSTITUTE",
            },
            {
                "photo": "ralph.jpg",
                "title": "Awesome service",
                "description": "We were provided guidance at every step of the admission process, advised on pros & cons regarding choice of college, choice of stream. Very patient and supportive Team Members for all our queries & clarifications. Thanks to the team, we were able to get the desired stream and desired college. They will always be our first recommendation. Fabulous experience!!",
                "name": "RALPH D'SOUZA",
                "college": "FR. CONCEICAO RODRIGUES COLLEGE OF ENGINEERING",
            },
            {
                "photo": "Vaibhav.jpg",
                "title": "Supportive mentors",
                "description": "I was ambiguous about what college and branch to choose based on my percentile and had doubts regarding what branch to go for and that's where Swift UnderGrads came in like a helping hand. Their sessions made me aware about the opportunities available in different engineering industries. I am grateful to the entire team for helping me make a wise decision regarding my college and branch.",
                "name": "VAIBHAV NANDEKAR",
                "college": "SMT. KISHORITAI BHOYAR COLLEGE OF PHARMACY",
            },
            # Add more dictionaries for additional cards as needed
        ]
    }  
    return render(request, 'home.html', context)
    # return HttpResponse("This is home page")

def about(request):
    context = {
        'about': [
            {
                "image": "Sharath.jpg",
                "name": "Sharath Pai",
                "role": "Founder | Tech Lead",
                "linkedin": "sharathpai107",
                "twitter": "Sharath1072",
                "instagram": "sharath_1007",
                "github": "Sharath1036",
                "color": "bg-warning",
            },
            {
                "image": "Karan.jpg",
                "name": "Karan Chavan",
                "role": "Admin | Pharmacy Lead",
                "linkedin": "karan-chavan-66b273222",
                "twitter": "Karanch66992447",
                "instagram": "karanchavan0503",
                "color": "bg-light",
            },
            {
                "image": "Shreyas.jpeg",
                "name": "Shreyas Gosavi",
                "role": "Treasurer",
                "linkedin": "shreyas-gosavi-31b161215",
                "twitter": "SSG482",
                "instagram": "ssg_482",
                "color": "bg-warning",
            },
            {
                "image": "Chinmay.jpg",
                "name": "Chinmay Dalal",
                "role": "Public Relations Lead",
                "linkedin": "chinmay-dalal-79774b237",
                "instagram": "chinmay_0662",
                "color": "bg-light",
            },
            {
                "image": "Hemant.jpg",
                "name": "Hemant Chaudhari",
                "role": "Marketing Lead",
                "instagram": "h.chaudhari_45",
                "color": "bg-light",
            },
            {
                "image": "Vaishnavi.jpg",
                "name": "Vaishnavi Deshmukh",
                "role": "Engineering Team Member",
                "linkedin": "vaishnavi-deshmukh-a84329230",
                "instagram": "vaishnavid3112",
                "color": "bg-warning",
            },
            {
                "image": "Monika.jpg",
                "name": "Monika Adkine",
                "role": "Engineering Team Member",
                "linkedin": "monika_adkine",
                "instagram": "monika-adkine-27594b237",
                "color": "bg-light",
            },
            {
                "image": "meenal.jpg",
                "name": "Meenal Sharma",
                "role": "Engineering Team Member",
                "linkedin": "meenal-sharma-699a4a280",
                "instagram": "idlaiidlaiyoiyoi",
                "color": "bg-warning",
            },
            {
                "image": "divya.jpg",
                "name": "Divya Sakharwade",
                "role": "Engineering Team Member",
                "linkedin": "divya-sakharwade-59564922b",
                "instagram": "sona.s.__",
                "color": "bg-warning",
            },
            {
                "image": "Harshal.jpg",
                "name": "Harshal Chopkar",
                "role": "Pharmacy Team Member",
                "linkedin": "harshal-chopkar-711513251",
                "instagram": "harshalchopkar234",
                "color": "bg-light",
            },
            {
                "image": "Poonam.jpg",
                "name": "Poonam Dhomne",
                "role": "Pharmacy Team Member",
                "linkedin": "poonam-dhomne-a54a422b1",
                "instagram": "_chandrasoma_",
                "color": "bg-warning",
            },
            {
                "image": "nikita.jpg",
                "name": "Nikita Sayre",
                "role": "Pharmacy Team Member",
                "instagram": "drx_nikitasayre",
                "color": "bg-light",
            },
            {
                "image": "harshalP.jpg",
                "name": "Harshal Pise",
                "role": "Pharmacy Team Member",
                "instagram": "_harshal_pise_07",
                "color": "bg-warning",
            },
            {
                "image": "Rushikesh.jpg",
                "name": "Rushikesh Mali",
                "role": "Agriculture Team Member",
                "linkedin": "rushikesh-mali-16b26724a",
                "instagram": "malirushikesh1032",
                "color": "bg-light",
            },
        ],
    }    
    return render(request,'about.html', context)

def mumbai(request):
    image_urls = {
        '480': 'qr480.jpg',
    }
    
    if request.method == "POST":
        studentName = request.POST.get('studentName')
        studentEmail = request.POST.get('studentEmail')
        studentPhone = request.POST.get('studentPhone')
        studentTelegram = request.POST.get('studentTelegram')
        studentGender = request.POST.get('studentGender')
        studentpcmscore = request.POST.get('studentpcmscore')
        studentjeescore = request.POST.get('studentjeescore')
        academy = request.POST.get('academy')

        if studentName and studentEmail and studentPhone and studentTelegram and studentGender and studentpcmscore and studentjeescore and academy:
            mumbai = MumbaiCounselling(studentName=studentName, studentEmail=studentEmail, studentPhone=studentPhone, studentTelegram=studentTelegram, studentGender=studentGender, studentpcmscore=studentpcmscore, studentjeescore=studentjeescore, academy=academy, date=datetime.today())
            mumbai.save()

            request.session['form_filled'] = True
            return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '480', 'discount': '0', 'final_amount': '480', 'image': image_urls['480']}))   

    return render(request,'mumbai.html')


def maharashtra(request):
    # Define image URLs dictionary
    image_urls = {
        '360': 'qr360.jpg',
        '480': 'qr480.jpg',
        '600': 'qr600.jpg',
        '800': 'qr800.jpg',
    }

    if request.method == "POST":
        # Form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        telegram = request.POST.get('telegram')
        gender = request.POST.get('gender')
        pcmscore = request.POST.get('pcmscore')
        pcbscore = request.POST.get('pcbscore')
        centralscore = request.POST.get('centralscore')
        preference = request.POST.get('preference')
        locations = request.POST.get('locations')
        source = request.POST.get('source')

        if source == 'ANI123':
            if name and email and phone and telegram and gender and pcmscore and pcbscore and centralscore and preference and locations:
                aniket = Aniket(name=name, email=email, phone=phone, telegram=telegram, gender=gender, pcmscore=pcmscore, pcbscore=pcbscore, centralscore=centralscore, preference=preference, locations=locations, date=datetime.today())
                aniket.save()
            if preference == 'engineering' or preference == 'pharmacy':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '480', 'discount': '120', 'final_amount': '360', 'image': image_urls['360']}))
            elif preference == 'both':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '800', 'discount': '200', 'final_amount': '600', 'image': image_urls['600']}))


        elif source == 'SAM123':
            if name and email and phone and telegram and gender and pcmscore and pcbscore and centralscore and preference and locations:
                samkit = Samkit(name=name, email=email, phone=phone, telegram=telegram, gender=gender, pcmscore=pcmscore, pcbscore=pcbscore, centralscore=centralscore, preference=preference, locations=locations, date=datetime.today())
                samkit.save()
            if preference == 'engineering' or preference == 'pharmacy':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '480', 'discount': '120', 'final_amount': '360', 'image': image_urls['360']}))
            elif preference == 'both':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '800', 'discount': '200', 'final_amount': '600', 'image': image_urls['600']}))

        elif source == 'SWIFT2024':
            if name and email and phone and telegram and gender and pcmscore and pcbscore and centralscore and preference and locations:
                swift = Swift(name=name, email=email, phone=phone, telegram=telegram, gender=gender, pcmscore=pcmscore, pcbscore=pcbscore, centralscore=centralscore, preference=preference, locations=locations, date=datetime.today())
                swift.save()
            if preference == 'engineering' or preference == 'pharmacy':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '480', 'discount': '120', 'final_amount': '360', 'image': image_urls['360']}))
            elif preference == 'both':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '800', 'discount': '200', 'final_amount': '600', 'image': image_urls['600']}))

        else:
            if name and email and phone and telegram and gender and pcmscore and pcbscore and centralscore and preference and locations:
                others = Others(name=name, email=email, phone=phone, telegram=telegram, gender=gender, pcmscore=pcmscore, pcbscore=pcbscore, centralscore=centralscore, preference=preference, locations=locations, date=datetime.today())
                others.save()
            if preference == 'engineering' or preference == 'pharmacy':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '480', 'discount': '0', 'final_amount': '480', 'image': image_urls['480']}))
            elif preference == 'both':
                request.session['form_filled'] = True
                return HttpResponseRedirect(reverse('payment', kwargs={'original_amount': '800', 'discount': '0', 'final_amount': '800', 'image': image_urls['800']}))

    return render(request, 'maharashtra.html')


def payment(request, original_amount, discount, final_amount, image):
    if not request.session.get('form_filled'):
        return HttpResponseForbidden("Access denied! Please fill the form first!")
    else:
        if request.method == "POST":
            upiname = request.POST.get('upiname')
            transactionid = request.POST.get('transactionid')
            if upiname and transactionid:
                payment = PaymentRecords(upiname=upiname, transactionid=transactionid)
                payment.save()
                del request.session['form_filled']
                request.session['payment_done'] = True
                return HttpResponseRedirect(reverse('success')) 

    return render(request, 'payment.html', {'original_amount': original_amount, 'discount': discount, 'final_amount': final_amount, 'image': image})

def success(request):
    if not request.session.get('payment_done'):
        return HttpResponseForbidden("Access denied! Please fill the form first!")
    return render(request,'success.html')

def cetnotes(request):
    context = {
        'physics': [
            {
                "image": "targetPhy11.jpg",
                "title": "PHYSICS 11TH STD",
                "publication": "TARGET PUBLICATIONS",
                "link": "https://drive.google.com/drive/folders/17zHYO0oifdhjOTyuD42q29QpDE6U7H97",
            },
            {
                "image": "targetPhy12.webp",
                "title": "PHYSICS 12TH STD",
                "publication": "TARGET PUBLICATIONS",
                "link": "https://drive.google.com/drive/folders/17zHYO0oifdhjOTyuD42q29QpDE6U7H97",
            },
            {
                "image": "sbPhy.jpg",
                "title": "PHYSICS SCORE BOOSTER",
                "publication": "CET SCORE BOOSTER",
                "link": "",
            },
        ],

        'chemistry': [
            {
                "image": "targetChem11.jpg",
                "title": "CHEMISTRY 11TH STD",
                "publication": "TARGET PUBLICATIONS",
                "link": "https://drive.google.com/drive/folders/184LCZH1uCGQgk7aFxvLyVG9V-SgT6xkd",
            },
            {
                "image": "targetChem12.webp",
                "title": "CHEMISTRY 12TH STD",
                "publication": "TARGET PUBLICATIONS",
                "link": "https://drive.google.com/drive/folders/184LCZH1uCGQgk7aFxvLyVG9V-SgT6xkd",
            },
            {
                "image": "sbChem.jpeg",
                "title": "CHEMISTRY SCORE BOOSTER",
                "publication": "CET SCORE BOOSTER",
                "link": "https://drive.google.com/drive/folders/1OQM-yEJYjfacG_rdm1-xl4VC5WoDGwAd",
            },
        ],

        'mathematics': [
            {
                "image": "targetMath11.jpg",
                "title": "MATHS 11TH STD",
                "publication": "TARGET PUBLICATIONS",
                "link": "https://drive.google.com/drive/folders/18CvF6u0VFQfDuxb_TY3Qfsw0kmhDRZBt",
            },
            {
                "image": "targetMath12.jpg",
                "title": "MATHS 12TH STD",
                "publication": "TARGET PUBLICATIONS",
                "link": "https://drive.google.com/drive/folders/18CvF6u0VFQfDuxb_TY3Qfsw0kmhDRZBt",
            },
            {
                "image": "sbMath1.webp",
                "title": "MATHS 12TH STD PART-1",
                "publication": "CET SCORE BOOSTER",
                "link": "https://drive.google.com/drive/folders/1S62OCmLuV30U5prHfcPALPKx4qv7JWdU",
            },
            {
                "image": "sbMath2.webp",
                "title": "MATHS 12TH STD PART-II",
                "publication": "CET SCORE BOOSTER",
                "link": "https://drive.google.com/drive/folders/1S62OCmLuV30U5prHfcPALPKx4qv7JWdU",
            },
        ],

        'biology': [
            {
                "image": "sbBio.webp",
                "title": "BIOLOGY SCORE BOOSTER",
                "publication": "CET SCORE BOOSTER",
                "link": "https://drive.google.com/drive/folders/1xwlkG-Z-7AFsounCVUqFlv8WFmkB5Dyw",
            },
        ],
    }
    return render(request,'cetnotes.html',context)

def enggnotes(request):
    context = {
        'engineering': [
            {
                "image": "avadhanulu.jpg",
                "title": "ENGINEERING PHYSICS",
                "publication": "M.N. AVADHANULU",
                "link": "https://drive.google.com/file/d/1T-jGVlZALNEfaCN2ZmbM1rtTfdC26JWa/view",
            },
            {
                "image": "jainjain.jpeg",
                "title": "ENGINEERING CHEMISTRY",
                "publication": "JAIN & JAIN",
                "link": "https://drive.google.com/file/d/1S00JxPqeMWBTjRNa0ygpk05VGdyTDNiX/view",
            },
            {
                "image": "bsgrewal.jpg",
                "title": "ENGINEERING MATHEMATICS",
                "publication": "B.S. GREWAL",
                "link": "https://drive.google.com/file/d/1GHImp8K43V72PL0D0P4K3hwYQbiIkZBV/view",
            },
            {
                "image": "hughes.jpg",
                "title": "BASIC ELECTRICAL ENGINEERING",
                "publication": "EDWARD HUGHES",
                "link": "https://drive.google.com/file/d/17lH8WjcOglTw2zYy43ORn1DLlVrIJoRt/view",
            },
            {
                "image": "bxe.png",
                "title": "BASIC ELECTRONICS ENGINEERING",
                "publication": "PUNE UNIVERSITY",
                "link": "https://drive.google.com/file/d/1fvXLpEVn4PBb9u_EGtL2dDKz6x5DTp7L/view",
            },
            {
                "image": "hibbeler.jpg",
                "title": "ENGINEERING MECHANICS",
                "publication": "R.C. HIBBELER",
                "link": "https://drive.google.com/file/d/16clLtahhrKZc6PP1Hi18wo3B5mOrtkJY/view",
            },
            {
                "image": "bhatt.png",
                "title": "ENGINEERING GRAPHICS",
                "publication": "N.D. BHATT",
                "link": "https://drive.google.com/file/d/1u2Pv2Jwfx2jYUVjGZXlizPmgj_wlQcv4/view",
            },
            {
                "image": "letUsC.jpg",
                "title": "C PROGRAMMING",
                "publication": "YASHAVANT KANETKAR",
                "link": "https://drive.google.com/file/d/1wcJDaIzLT0nM8XAQNaM_0xlOX1UhjDvN/view",
            },
            {
                "image": "communication.jpg",
                "title": "COMMUNICATION SKILLS",
                "publication": "SHIRLEY MATHEW",
                "link": "https://drive.google.com/file/d/1yEnkhFMvI3Gqy2eMiKJybv3L-yzbxx0L/view",
            },
            {
                "image": "pythonBook.jpeg",
                "title": "PYTHON PROGRAMMING",
                "publication": "PUNE UNIVERSITY",
                "link": "https://drive.google.com/file/d/1gAb6ouZO_hFtgfSBY6Z-f2UruXhddcLo/view",
            },
        ]    
    }
    return render(request,'enggnotes.html', context)

def pharmnotes(request):
    context = {
        'pharmacy': [
            {
                "image": "pharmaceutics1.webp",
                "title": "PHARMACEUTICS-I",
                "publication": "NIRALI PRAKASHAN",
                "link": "https://drive.google.com/file/d/1dzDceVMkhPKLptUb0c-IQZNscPvZfZgL/view",
            },
            {
                "image": "phAnalysis.jpeg",
                "title": "PHARMACEUTICAL ANALYSIS",
                "publication": "NIRALI PRAKASHAN",
                "link": "https://drive.google.com/file/d/1eAZdi3dqzHD7YGx7sU8nBDCZfndYOGyC/view",
            },
            {
                "image": "hap1.jpeg",
                "title": "HUMAN ANATOMY AND PHYSIOLOGY-I",
                "publication": "NIRALI PRAKASHAN",
                "link": "https://drive.google.com/file/d/1dtmZ995DCO-JmEagCnf0No9Qlu4F129e/view",
            },
            {
                "image": "inorganic.webp",
                "title": "INORGANIC CHEMISTRY",
                "publication": "NIRALI PRAKASHAN",
                "link": "https://drive.google.com/file/d/1e9nXu8hLd0Y75sAzR2uF45rtV0kvSz9-/view",
            },
            {
                "image": "remedialBio.jpg",
                "title": "REMEDIAL BIOLOGY",
                "publication": "NIRALI PRAKASHAN",
                "link": "https://drive.google.com/file/d/1eAuae42LPBEV1uE0NGgvtbg34VTMi_nQ/view",
            },
            {
                "image": "remedialMaths.jpg",
                "title": "REMEDIAL MATHS",
                "publication": "NIRALI PRAKASHAN",
                "link": "https://drive.google.com/file/d/1eBOM8AQnCi1F1LdFBPr7dUX663fb1FlS/view",
            },
            {
                "image": "communication.jpg",
                "title": "COMMUNICATION SKILLS",
                "publication": "CAREWELL PHARMA",
                "link": "https://drive.google.com/file/d/1E0jB72Xfs7UwXpxIlzJVCOBRp01XTXBE/view",
            },
        ]
    }
    return render(request,'pharmnotes.html', context)

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        comment = request.POST.get('comment')

        if fname and lname and email and contactno and comment:
            contact = Contact(fname=fname, lname=lname, email=email, contactno=contactno, comment=comment, date=datetime.today())
            contact.save()

    return render(request,'contact.html')