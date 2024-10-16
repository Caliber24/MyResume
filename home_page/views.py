from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = {
        "name": "Amirhossein Pishro",
        "job": "Backend Developer",
        "about me": "As a BackEnd Developer and Project Manager, I worked in a project that I can refer to and added to the quality of my work and my responsibility. Currently, most of my focus is on university and increasing my skills as a BackEnd Developer, and I am trying to increase my teamwork spirit. I am not currently working and just adding to my skills",
        "phone": "09164896609",
        "email": "amirhosseinpishroa2001@gmail.com",
        'address': 'Iran, Fars province, Lar city, Berak village',
        'github': 'https://github.com/Caliber24',
        'linkedin': 'www.linkedin.com/in/amirhossein-pishro-a323162a3',
        'soft_skills': ['Public Relations', 'TeamWork', 'Effective Management'],
        'hard_skills': {
            "DRF": "4 month",
            "Django": "6 month",
            "Python": '10 month',
            "Java": "2 year"},
        'language': ['English(basic)', 'Persian(mother tongue)'],
        "work_expriences": {
            'ISGAME': {
                "job": {
                'content_creator': "I worked in the response and post management department",
                'backend_developer': 'In the future, I am going to implement the back-end part of the site'
                },
                'start_time': '2024',
                'end_time': 'PRESENT'
                },
            
                "5+1 TEAM": {
                    'description':'This team was formed within the university and it is based on friends gathering together and working with each other, and these duties that are stated below are the duties of almost all members.',
                    'job':{
                        'founder':'',
                        'cordinator':'',
                        'backend_developer':'',
                        'project_manager':''
                        },
                    'start_time': '2024',
                    'end_time': 'PRESENT'
                }
        },
        'education': {
            'HIGH_SCHOOL':{
                'start_time': '2018',
                'end_time': '2022',
                'license': 'DIPLOMA OF MATHEMATICS',
                'institue':'SAMPAD'
            },
            'UNIVERSITY':{
                'start_time': '2022',
                'end_time': '2026',
                'degree': 'BACHELOR OF COMPUTER ENGINEERING',
                'institue':'PERSIAN GULF UNIVERSITY'
            }
        }


    }
    return render(request, 'index.html', context)
