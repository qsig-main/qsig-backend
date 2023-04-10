# for function based views
from django.shortcuts import render
import requests

# for class based views
from django.shortcuts import get_object_or_404, redirect
from team.models import Member
from team.serializers import MemberSerializer
from pitches.models import Pitch, PitchImage
from pitches.serializers import PitchSerializer, PitchImageSerializer
from reports.models import Report, ReportImage
from reports.serializers import ReportSerializer, ReportImageSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.decorators import login_required
# login
from django.contrib.auth import authenticate, login
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

# logout
from django.contrib.auth import logout
from django.shortcuts import redirect

# deleting files/images
import os

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# @login_required ***uncomment if want nobody to see client/******
def home(request):
    # url of pitch endpoint
    pitch_endpoint = "https://web-production-e20e7.up.railway.app/api/pitch/" 
    # # get the information at the endpoint
    # pitch_get_response = requests.get(pitch_endpoint)
    # turn the information into json
    # pitch_data = pitch_get_response.json()
    # pitch_data['results'] <-- extracting information from the pitch_data object (look at api for json format)
    # 'pitch': pitch_data['results'] <-- key: pitch, value: pitch_data['results] (value is list of objects)

    # pitch_img_endpoint = "https://web-production-e20e7.up.railway.app/api/pitch/img/"
    # pitch_img_get_response = requests.get(pitch_img_endpoint)
    # pitch_img_data = pitch_img_get_response.json()

    # report_endpoint = "https://web-production-e20e7.up.railway.app/api/report/"
    # report_get_response = requests.get(report_endpoint)
    # report_data = report_get_response.json()

    # report_img_endpoint = "https://web-production-e20e7.up.railway.app/api/report/img/"
    # report_img_get_response = requests.get(report_img_endpoint)
    # report_img_data = report_img_get_response.json()

    return render(request, 'client/base.html', {
        # 'pitch': pitch_data['results'],
        # 'pitch_img': pitch_img_data['results'],
        # 'report': report_data['results'],
        # 'report_img': report_img_data['results'],
    })

acceptable_image_types = ['jpg', 'jpeg', 'png', 'tiff', 'tif', 'gif']

class PitchList(APIView):
    """lists pitches, prob could replace function views"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_list.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request):
        queryset = Pitch.objects.all()
        return Response({'pitches': queryset})

class PitchDetail(APIView):
    """pitch detail view(client/pitch/2, can update in this method"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_detail.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        pitch = get_object_or_404(Pitch, pk=pk)
        serializer = PitchSerializer(pitch, context={'request': request})
        PitchSerializer(pitch, data=request.data)
        return Response({'serializer': serializer, 'pitch': pitch})

    def post(self, request, pk):
        if request.data['pdf']:
            filetype = str(request.data['pdf']).split(".")[-1]
            if filetype == 'pdf':
                pitch = get_object_or_404(Pitch, pk=pk)
                pitch_url = pitch.pdf.path
                if pitch_url[-20:] != 'None/pdf_default.pdf':
                    os.remove(pitch_url)
            else:
                return redirect('wrong-file-type')
        pitch = get_object_or_404(Pitch, pk=pk)
        serializer = PitchSerializer(pitch, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'pitch': pitch})
        serializer.save()
        return redirect('home')

class PitchCreate(APIView):
    """place to create pitches"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_create.html'
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = PitchSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        if request.data['pdf']:
            filetype = str(request.data['pdf']).split(".")[-1]
            if filetype != 'pdf':
                return redirect('wrong-file-type')
        serializer = PitchSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('home')

class PitchDelete(APIView):
    """place to delete pitches"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_delete.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        pitch = get_object_or_404(Pitch, pk=pk)
        return Response({'pitch': pitch})
    
    def post(self, request, pk):
        pitch = get_object_or_404(Pitch, pk=pk)
        pitch.delete()
        pitch_url = pitch.pdf.path
        if pitch_url[-20:] != 'None/pdf_default.pdf':
            os.remove(pitch_url)
        return redirect('home')


class PitchImageList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_image_list.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = PitchImage.objects.all()
        return Response({'pitch_images': queryset})

class PitchImageDetail(APIView):
    """pitch image detail view(client/pitch/img/2, can update in this method"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_image_detail.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        pitch_img = get_object_or_404(PitchImage, pk=pk)
        serializer = PitchImageSerializer(pitch_img, context={'request': request})
        PitchImageSerializer(pitch_img, data=request.data)
        return Response({'serializer': serializer, 'pitch_img': pitch_img})

    def post(self, request, pk):
        if request.data['image']:
            filetype = str(request.data['image']).split(".")[-1]
            if filetype in acceptable_image_types:
                pitch_img = get_object_or_404(PitchImage, pk=pk)
                pitch_img_url = pitch_img.image.path
                if pitch_img_url[-22:] != 'None/image_default.png':
                    os.remove(pitch_img_url)
        pitch_img = get_object_or_404(PitchImage, pk=pk)
        serializer = PitchImageSerializer(pitch_img, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'pitch_img': pitch_img})
        serializer.save()
        return redirect('home')

class PitchImageCreate(APIView):
    """place to create pitches"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_image_create.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request):
        serializer = PitchImageSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = PitchImageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('home')

class PitchImageDelete(APIView):
    """place to delete pitches"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_image_delete.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        pitch_img = get_object_or_404(PitchImage, pk=pk)
        return Response({'pitch_img': pitch_img})
    
    def post(self, request, pk):
        pitch_img = get_object_or_404(PitchImage, pk=pk)
        pitch_img.delete()
        pitch_img_url = pitch_img.image.path
        if pitch_img_url[-22:] != 'None/image_default.png':
            os.remove(pitch_img_url)
        return redirect('home')


class ReportList(APIView):
    """lists reports, prob could replace function views"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_list.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request):
        queryset = Report.objects.all()
        return Response({'reports': queryset})

class ReportDetail(APIView):
    """report detail view(client/report/2, can update in this method"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_detail.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(report, context={'request': request})
        ReportSerializer(report, data=request.data)
        return Response({'serializer': serializer, 'report': report})

    def post(self, request, pk):
        if request.data['pdf']:
            filetype = str(request.data['pdf']).split(".")[-1]
            if filetype == 'pdf':
                report = get_object_or_404(Report, pk=pk)
                report_url = report.pdf.path
                if report_url[-20:] != 'None/pdf_default.pdf':
                    os.remove(report_url)
            else:
                return redirect('wrong-file-type')
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(report, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'report': report})
        serializer.save()
        return redirect('home')

class ReportCreate(APIView):
    """place to create reports"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_create.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request):
        serializer = ReportSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        if request.data['pdf']:
            filetype = str(request.data['pdf']).split(".")[-1]
            if filetype != 'pdf':
                return redirect('wrong-file-type')
        serializer = ReportSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('home')

class ReportDelete(APIView):
    """place to delete reports"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_delete.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        return Response({'report': report})
    
    def post(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        report.delete()
        report_url = report.pdf.path
        if report_url[-20:] != 'None/pdf_default.pdf':
            os.remove(report_url)
        return redirect('home')


class ReportImageList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_image_list.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = ReportImage.objects.all()
        return Response({'report_images': queryset})

class ReportImageDetail(APIView):
    """report image detail view(client/report/img/2, can update in this method"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_image_detail.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        report_img = get_object_or_404(ReportImage, pk=pk)
        serializer = ReportImageSerializer(report_img, context={'request': request})
        ReportImageSerializer(report_img, data=request.data)
        return Response({'serializer': serializer, 'report_img': report_img})

    def post(self, request, pk):
        if request.data['image']:
            filetype = str(request.data['image']).split(".")[-1]
            if filetype in acceptable_image_types:
                report_img = get_object_or_404(ReportImage, pk=pk)
                report_img_url = report_img.image.path
                if report_img_url[-22:] != 'None/image_default.png':
                    os.remove(report_img_url)
        report_img = get_object_or_404(ReportImage, pk=pk)
        serializer = ReportImageSerializer(report_img, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'report_img': report_img})
        serializer.save()
        return redirect('home')

class ReportImageCreate(APIView):
    """place to create reports"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_image_create.html'
    # permission_classes = [IsAuthenticated]


    def get(self, request):
        serializer = ReportImageSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = ReportImageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('home')

class ReportImageDelete(APIView):
    """place to delete reports"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'report_image_delete.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        report_img = get_object_or_404(ReportImage, pk=pk)
        return Response({'report_img': report_img})
    
    def post(self, request, pk):
        report_img = get_object_or_404(ReportImage, pk=pk)
        report_img.delete()
        report_img_url = report_img.image.path
        if report_img_url[-22:] != 'None/image_default.png':
            os.remove(report_img_url)
        return redirect('home')


def wrong_file_type(request):
    return render(request, 'wrong.html', {})


class MemberList(APIView):
    """lists members, prob could replace function views"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'member_list.html'
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Member.objects.all()
        return render(request, 'member_list.html', {'members': queryset})

class MemberListPosition(APIView):
    """lists members, prob could replace function views"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'member_list_position.html'
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Member.objects.all()
        return render(request, 'member_list_position.html', {'members': queryset})

class MemberDetail(APIView):
    """member detail view(client/member/2, can update in this method"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'member_detail.html'
    # permission_classes = [IsAuthenticated]
    style = {'template_pack': 'rest_framework/vertical/'}

    def get(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        serializer = MemberSerializer(member, context={'request': request})
        MemberSerializer(member, data=request.data)
        refer = request.META.get('HTTP_REFERER')
        return Response({'serializer': serializer, 'member': member, 'refer': refer, 'style': self.style})

    def post(self, request, pk):
        if request.data['headshot']:
            filetype = str(request.data['headshot']).split(".")[-1]
            if filetype in acceptable_image_types:
                headshot_img = get_object_or_404(Member, pk=pk)
                headshot_img_url = headshot_img.headshot.path
                if headshot_img_url[-26:] != 'None/headshot_default.jpeg':
                    os.remove(headshot_img_url)
        member = get_object_or_404(Member, pk=pk)
        serializer = MemberSerializer(member, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'member': member, 'style': self.style})
        serializer.save()
        next_url = request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('client-member-list')

class MemberCreate(APIView):
    """place to create memberes"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'member_create.html'
    # permission_classes = [IsAuthenticated]
    style = {'template_pack': 'rest_framework/vertical/'}

    def get(self, request):
        serializer = MemberSerializer()
        refer = request.META.get('HTTP_REFERER')
        return Response({'serializer': serializer, 'style': self.style, 'refer': refer})

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'style': self.style})
            # return Response({'serializer': serializer})
        serializer.save()
        next_url = request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('client-member-list')

class MemberDelete(APIView):
    """place to delete memberes"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'member_delete.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        refer = request.META.get('HTTP_REFERER')
        return Response({'member': member, 'refer': refer})
    
    def post(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        member.delete()
        headshot_img_url = member.headshot.path
        if headshot_img_url[-26:] != 'None/headshot_default.jpeg':
            os.remove(headshot_img_url)
        next_url = request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('client-member-list')