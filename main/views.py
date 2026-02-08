from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import InquiryForm, ContactForm, ScheduleContactForm
from .models import Inquiry, ServiceInquiry

def index(request):
    # Handle Contact Form (CTA Section)
    contact_form = InquiryForm(request.POST or None)
    
    if request.method == "POST":
        # Check which form was submitted
        if 'contact_submit' in request.POST:
            if contact_form.is_valid():
                inquiry = contact_form.save()
                # Email content for contact form
                admin_message = f"""
New Inquiry Received:

Name: {inquiry.name}
Email: {inquiry.email}
Phone: {inquiry.phone}
Message:
{inquiry.message}
"""
                user_message = f"""
Hi {inquiry.name},

Thank you for reaching out! We have received your message and will get back to you soon.

Your Message:
{inquiry.message}
------------------------------------

Best regards,
R2 Electrical & Air Conditioning
"""
                try:
                    # Send email to admin
                    send_mail(
                        subject=f"New Inquiry from {inquiry.name}",
                        message=admin_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=settings.ADMIN_EMAIL,
                        fail_silently=False,
                    )

                    # Send confirmation email to user
                    send_mail(
                        subject="Thank you for contacting Electra!",
                        message=user_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[inquiry.email],
                        fail_silently=False,
                    )

                    messages.success(request, "Your message has been sent successfully!")
                    return redirect('index')
                except Exception as e:
                    print("Email error:", e)
                    messages.error(request, "Message saved, but failed to send email.")
            else:
                messages.error(request, "Please correct the errors in the contact form.")
        
        # Handle Carousel Form (Service Inquiry)
        elif 'carousel_submit' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            service = request.POST.get('service')
            message_text = request.POST.get('message')

            if name and email and phone and service and message_text:
                service_inquiry = ServiceInquiry.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    service=service,
                    message=message_text
                )

                # Email content for carousel form
                admin_message = f"""
New Service Inquiry:

Name: {service_inquiry.name}
Email: {service_inquiry.email}
Phone: {service_inquiry.phone}
Service: {service_inquiry.service}
Message:
{service_inquiry.message}
"""
                user_message = f"""
Hi {service_inquiry.name},

Thank you for requesting a service! We have received your request for '{service_inquiry.service}' and will contact you soon.

Your Message:
{service_inquiry.message}
------------------------------------

Best regards,
R2 Electrical & Air Conditioning
"""
                try:
                    # Email to admin
                    send_mail(
                        subject=f"New Service Inquiry from {service_inquiry.name}",
                        message=admin_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=settings.ADMIN_EMAIL,
                        fail_silently=False,
                    )
                    # Confirmation email to user
                    send_mail(
                        subject="Thank you for contacting Electra!",
                        message=user_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[service_inquiry.email],
                        fail_silently=False,
                    )
                    messages.success(request, "Your service request has been submitted successfully!")
                    return redirect('index')
                except Exception as e:
                    print("Email error:", e)
                    messages.error(request, "Request saved, but failed to send email.")
            else:
                messages.error(request, "Please fill in all fields in the service form.")

    return render(request, "main/index.html", {'form': contact_form})

# About Page
def about(request):
    return render(request, 'main/about.html')

# Services Page
def service(request):
    return render(request, 'main/service.html')

# Contact Page
def contact(request):
    if request.method == 'POST':
        form = ScheduleContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            # Email to admin
            admin_message = f"""
New Schedule Request

Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone}
Service: {contact.subject}

Message:
{contact.message}
"""

            # Email to customer
            customer_message = f"""
Hi {contact.name},

Thanks for booking a service with Mayday Appliance Repairs 👋

We’ve received your request with the following details:

Service: {contact.subject}
Phone: {contact.phone}
Message:
{contact.message}

Our technician will contact you shortly.

Regards,
Mayday Appliance Repairs
📞 +61 404 000 049
"""

            try:
                send_mail(
                    subject=f"New Service Booking – {contact.subject}",
                    message=admin_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=settings.ADMIN_EMAIL,
                    fail_silently=False,
                )

                send_mail(
                    subject="We’ve received your service request",
                    message=customer_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[contact.email],
                    fail_silently=False,
                )

                messages.success(request, "Your service request has been submitted successfully!")
                return redirect('contact')

            except Exception as e:
                print("Email Error:", e)
                messages.error(request, "Something went wrong. Please try again.")

        else:
            messages.error(request, "Please correct the errors in the form.")

    else:
        form = ScheduleContactForm()

    return render(request, 'main/contact.html', {'form': form})
