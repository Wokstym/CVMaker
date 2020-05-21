import json
from datetime import datetime
from django.utils.http import urlquote

import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template

from home.models import UserData


def is_contact_info(inf):
    return inf.country != "" or \
           inf.city != "" or \
           inf.phone != "" or \
           inf.email != "" or \
           inf.github != "" or \
           inf.linkedin != "" or \
           inf.personal_website != ""


def generate_pdf(template_path, context, pdf_title):
    template = get_template(template_path)
    html = template.render(context)
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'margin-top': "0",
        'margin-left': "0",
        'margin-right': "0",
        'margin-bottom': "0",
        'title': pdf_title
    }

    css = [
        'static/css/to_pdf/bootstrap.min.css',
        'static/css/to_pdf/ldbtn.min.css',
        'static/css/to_pdf/fontawesome.min.css']

    pdf = pdfkit.from_string(html, False, options, css=css)
    response = HttpResponse(pdf, content_type='application/pdf')
    content = f"inline; filename={urlquote(pdf_title + '.pdf')}"
    response['Content-Disposition'] = content
    return response


def get_context_data(user_id, cv_number):
    user_data = UserData.objects.get(user_id=user_id)
    cv = user_data.current_cvs[cv_number]
    if is_contact_info(cv.contact_info):
        contact_info = cv.contact_info
    else:
        contact_info = None

    return {'cv_number': cv_number,
            'name': user_data.name,
            'surname': user_data.surname,
            'contact_info': contact_info,
            'education': cv.education,
            'experience': cv.experience,
            'skills': cv.skills,
            'languages': cv.languages,
            'interests': cv.interests,
            'projects': cv.projects,
            'organizations': cv.organizations,
            'description': cv.description
            }


def pretty_print_json(json_string):
    print(json.dumps(json_string, indent=4))


def datetime_to_string():
    return datetime.now().strftime("%d/%m/%Y, %H:%M")


def string_to_datetime(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y, %H:%M")
