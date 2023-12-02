from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from marksheet.models import StudentData
from .forms import StudentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination 
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or another URL
    else:
        form = StudentForm()

    return render(request, 'home.html', {'form': form})

'''If you want a DRF view uncomment the below code'''

# class GetStudentsView(generics.ListAPIView):
#     serializer_class = StudentSerializer

#     def get_queryset(self):
#         class_param = self.request.query_params.get('class', None)

#         queryset = StudentData.objects.all()

#         if class_param:
#             queryset = queryset.filter(student_class=class_param)

#         queryset = sorted(queryset, key=lambda student: student.total_score(), reverse=True)

#         return queryset

# And comment this code below.
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class GetStudentsView(generics.ListAPIView):
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        class_param = self.request.query_params.get('class', None)

        queryset = StudentData.objects.all()

        if class_param:
            queryset = queryset.filter(student_class=class_param)

        queryset = sorted(queryset, key=lambda student: student.total_score(), reverse=True)

        return queryset

class GetStudentsView(generics.ListAPIView):
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    template_name = 'students_list.html'

    def get_queryset(self):
        class_param = self.request.query_params.get('class', None)

        queryset = StudentData.objects.all()

        if class_param:
            queryset = queryset.filter(student_class=class_param)

        queryset = sorted(queryset, key=lambda student: student.total_score(), reverse=True)

        return queryset

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'students': self.paginate_queryset(self.get_queryset())})



# In this below ajax call the server is sucessfully
# processsing the request but the data is not getting saved in the database.

# I'll try to figure it out and push the changes later.


@csrf_protect
@login_required(login_url='login')
def HomePage2(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
            else:
                return redirect('home2')  # Redirect to a success page or another URL
    else:
        form = StudentForm()

    return render(request, 'home2.html', {'form': form})