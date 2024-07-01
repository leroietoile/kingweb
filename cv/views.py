from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Profile, Block, PortfolioType, Portfolio, VisitorMessage, Section


def base(request):
    blocks = Block.objects.all()
    sections = Section.objects.all()

    profiles = Profile.objects.all()
    my_profile = profiles[0]

    right_footer_elements = Block.objects.filter(section__title='right footer')

    try:
        f_profile_img = right_footer_elements.first().picture.url
    except:
        f_profile_img = 'no image'

    try:
        f_initials_img = right_footer_elements.last().picture.url
    except:
        f_initials_img = 'no image'

    return {'my_profile': my_profile, 'blocks': blocks, 'sections': sections, 'f_profile_img': f_profile_img, 'f_initials_img': f_initials_img}


def index(request):
    profiles = Profile.objects.all()
    my_profile = profiles[0]

    blocks = Block.objects.all()
    sections = Section.objects.all()


    # ========== SERVICES BLOCKS ==============
    my_services = []
    for block in blocks:
        if block.section.recollect_key == 'services':
            my_services.append(block)
    # ===========================================

    portf_types_list = PortfolioType.objects.all()
    portf_types = sorted(portf_types_list, key=lambda x: x.pos_index)
    portfs_list = Portfolio.objects.all()
    portfs = sorted(portfs_list, key=lambda x: x.pos_index)
    portf_dict = {}
    for p_type in portf_types:
        portf_list = []
        for portf in portfs:
            if portf.type.name == p_type.name:
                portf_list.append(portf)
        if len(portf_list) > 0:
            portf_dict[p_type.name] = list(portf_list)

    my_full_name = my_profile.firstname + ' ' + my_profile.surname

    context = {'my_full_name': my_full_name, 'blocks': blocks, 'sections': sections,
               'portf_dict': portf_dict, 'services': my_services}
    base_context = base(request)
    context.update(base_context)

    return render(request, 'cv/index.html', context)


def send_message(request):
    if request.POST.get('action') == 'post':
        response_msg = 'PLease fill all the fields or check the email.'
        # _________GET INFORMATIONS______________
        name = request.POST.get('name').strip()
        mail = request.POST.get('mail').strip()
        obj = request.POST.get('object').strip()
        message = request.POST.get('message').strip()
        # ______________MANAGE EMPTY FIELD ISSUE_____________
        if name == '' or mail == '' or obj == '' or message == '' or '@gmail.com' not in mail:
            return JsonResponse({'response_msg': response_msg})

        # ____________ SEND MESSAGE TO MY EMAIL __________________
        mail_msg = f'From: {name}\nEmail: {mail}\n\n{message}'
        profiles = Profile.objects.all()
        my_profile = profiles[0]
        my_email = my_profile.email.strip()

        try:
            send_mail('Message from your Web Site', mail_msg, settings.DEFAULT_FROM_EMAIL, [my_email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Sorry, dad header detected.')
        except Exception as e:
            return HttpResponse('Sorry, something went wrong during the process. Try later.')
        # _________________________________________________________

        # ___________PUT INFORMATIONS IN MODEL_____________
        try:
            message_obj = VisitorMessage(name=name, email=mail, object=obj, text=message)
            message_obj.save()
            response_msg = 'Message sent successfully.'
        except:
            pass
        response = JsonResponse({'response_msg': response_msg})
        return response


def portfolio(request, id):
    current_portfolio = get_object_or_404(Portfolio, id=id)
    wb_ad = ''
    if current_portfolio.web_address:
        _list = current_portfolio.web_address.split('/')
        wb_ad = _list[-1]

    context = {'current_portfolio': current_portfolio, 'wb_ad': wb_ad}
    base_context = base(request)
    context.update(base_context)
    return render(request, 'cv/portfolio.html', context)


