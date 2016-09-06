from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


@login_required
def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            send_mail(
                'Feedback from your site, topic: %s' % topic,
                message, sender,
                ['772052869@qq.com']
            )
            return HttpResponseRedirect('/contacts/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact/contact.html', {
                            'form':form
                            }, RequestContext(request)
                            )


@login_required
def thanks(request):
    return render_to_response('contact/thanks.html', {
            }, context_instance=RequestContext(request))


