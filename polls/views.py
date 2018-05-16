from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

#added en tutorial 4
from django.http import HttpResponseRedirect
from django.urls import reverse

#added casi a final del tuto 4
from django.views import generic

#added en tuto part 5
from django.utils import timezone

from .models import Choice, Question

from polls.models import Document
from polls.forms import DocumentForm

'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''

'''
#lo mismo que arriba pero usando un shortcut : render()  part 3
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



# Leave the rest of the views (detail, results, vote) unchanged
    #return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



# Primera implementacion de vote, cambiada en tuto part 4
#def vote(request, question_id):
#    return HttpResponse("you're voting on quest %s." % question_id)


#tuto part 4
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

'''

#agregado a final del tuto part 4

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
  
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



#tuto part 4
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#nuevo form upload
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           # return redirect('polls/model_form_upload.html')
    else:
        form = DocumentForm()
    return render(request, 'polls/model_form_upload.html', {
        'form': form
    })


class IndexView2(generic.ListView):
    template_name = 'polls/music.html'
    context_object_name = 'latest_music_list'
    def get_queryset(self):
  
        return Document.objects.filter(uploaded_at__lte=timezone.now()).order_by('-uploaded_at')[:10]
