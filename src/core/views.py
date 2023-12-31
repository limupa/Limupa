from django.shortcuts import render, redirect

# Create your views here.
from django.db.models import Sum
from django.views.generic import ListView
from product.models import Product_version
from django.db.models import Q



class HomePage(ListView):
    template_name = 'core/index.html'
    model = Product_version
    context_object_name = 'products'

    # def get_queryset(self):
    #     return Product_version.objects.order_by("-date").all()[:2]
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        print(request.session.get('show_registration_message',"6666666666666666666666666666666"))
        if request.session.get('show_registration_message', False):
            request.session.pop('show_registration_message')
        return response


    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['new_ps'] = Product_version.objects.order_by("date_added").all()[:7]
        context['bestseller_ps'] = Product_version.objects.order_by('-units_sold').all()[:7]
        context['featured_ps'] = Product_version.objects.order_by( "review_count").all()[:7]
        context['laptop'] = Product_version.objects.filter(product__category__name = 'Noutbuklar' )
        context['tvaudio'] = Product_version.objects.filter(Q(product__category__name = 'TV, audio, video') | Q(product__category__p_category__name = 'TV, audio, video'))
        context['trendings'] = Product_version.objects.order_by('-units_sold').all()[:7]
        return context


from django.http import JsonResponse
from django.views import View
from .forms import SubscriberForm, ContactForm
from .models import Subscriber
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def SubscribeView(request):
    email = request.POST.get('emailInput')
   
    if email:
        try:
            validate_email(email)
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': 'You are already subscribed.'})
            else:
                Subscriber.objects.create(email=email)
                # Send confirmation message
                return JsonResponse({'success': True})
        except ValidationError:
            return JsonResponse({'success': False, 'message': 'Enter true email addres.'})
    else:
        return JsonResponse({'success': False, 'message': 'Email field is required.'})


from django.http import JsonResponse
from django.views import View
from .models import Contact
from django.contrib import messages

class ContactView(View):
    def get(self, request):
        return render(request, 'core/contact.html')

    def post(self, request):
        customer_name = request.POST.get('customerName')
        customer_email = request.POST.get('customerEmail')
        contact_subject = request.POST.get('contactSubject')
        contact_message = request.POST.get('contactMessage')

        if customer_name and customer_email and contact_subject and contact_message:
            contact = Contact(
                name=customer_name,
                email=customer_email,
                subject=contact_subject,
                message=contact_message
            )
            contact.save()

            # messages.success(request, 'Message sent successfully.')
            return redirect('contact')
        else:
            # messages.error(request, 'Please fill in all required fields.')
            return redirect('contact')





def Error404(request, exception):
    return render(request , 'core/404.html', status=404)

def AboutUS(request):
    return render(request , 'core/about-us.html')

# def Contact(request):
#     return render(request , 'core/contact.html')

def Faq(request):
    return render(request , 'core/faq.html')

