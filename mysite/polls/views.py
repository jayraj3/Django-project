from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import View
from .models import Question
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect



def owner(request):
    oldval = request.COOKIES.get('dj4e_cookie', '4dc3ed26')
    resp = HttpResponse("Hello,"+str(oldval) +"is the polls index.")
    resp.set_cookie('dj4e_cookie', '4dc3ed26', max_age=1000)
    return resp


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

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


