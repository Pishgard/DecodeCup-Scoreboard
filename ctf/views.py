from ctf.models import *
from django.db.models import Sum
from django.db.models import F
from django.shortcuts import render, redirect
from .forms import SubmitForm
from django.contrib.auth.decorators import login_required


def board(request, id):
    teams = Team.objects.filter(league=id).annotate(total_score=Sum(F('score_level1') + F('score_level2'))).order_by('-total_score', 'time')
    team_scores = []
    for team in teams:
        row_data = {
            'name': team.name,
            'rank': teams.filter(total_score__gt=team.total_score).count() + 1,
            'level1_points': team.score_level1,
            'level2_points': team.score_level2,
            'total_points': team.total_score,
            'time': team.time,
        }
        team_scores.append(row_data)
    context = {'team_scores': team_scores, 'title': League.objects.get(id=id)}
    return render(request, 'board.html', context)


def index(request):
    content = League.objects.all()
    return render(request, "index.html", context={
        "content": League,
        "custom_title": "تست"
    })


@login_required
def submit_form(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            submit_instance = form.save(commit=False)

            if submit_instance.status:
                if submit_instance.level == "1":
                    submit_instance.team.score_level1 += 1
                    if submit_instance.team_broken and submit_instance.team_broken.code_level1:
                        submit_instance.team_broken.code_level1 = False
                        submit_instance.team_broken.score_level1 -= 3
                        submit_instance.team_broken.save()

                if submit_instance.level == "2":
                    submit_instance.team.score_level2 += 1
                    if submit_instance.team_broken and submit_instance.team_broken.code_level2:
                        submit_instance.team_broken.code_level2 = False
                        submit_instance.team_broken.score_level2 -= 3
                        submit_instance.team_broken.save()

                submit_instance.team.time += submit_instance.time
                submit_instance.team.save()
            else:
                submit_instance.team.time += 10
                submit_instance.team.save()
            submit_instance.save()

            return redirect('submit-list')
    else:
        form = SubmitForm()

    return render(request, 'submit.html', {'form': form})


def submit_list(request):
    submit_list = Submit.objects.all()
    return render(request, 'submit_list.html', {'submit_list': submit_list})