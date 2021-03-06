from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import render
from plainbox.impl.unit import test_file

from Shareback_App.src.adapter.FeedbackGetAdapter import FeedbackGetAdapter
from Shareback_App.src.adapter.FeedbackInsertAdapter import FeedbackInsertAdapter
from Shareback_App.src.adapter.FileCopyAdapter import FileCopyAdapter
from Shareback_App.src.adapter.FileDeleteAdapter import FileDeleteAdapter
from Shareback_App.src.adapter.FileLsAdapter import FileLsAdapter
from Shareback_App.src.adapter.FileMkdirAdapter import FileMkdirAdapter
from Shareback_App.src.adapter.FileMoveAdapter import FileMoveAdapter
from Shareback_App.src.adapter.FileRenameAdapter import FileRenameAdapter
from Shareback_App.src.adapter.FileUploadAdapter import FileUploadAdapter
from Shareback_App.src.adapter.PreviousSessionsAdapter import PreviousSessionsAdapter
from Shareback_App.src.adapter.dto.AddSessionFileResponseDTO import AddSessionFileResponseDTO
from Shareback_App.src.util.MyEncoder import MyEncoder


def test(request):
    dto = AddSessionFileResponseDTO()
    dto.set_result("Hello this is result")
    a = MyEncoder().encode(dto)
    return HttpResponse(a)


def feedback_get(request):
    print("Entering feedbacks_get()...")
    response = FeedbackGetAdapter(request).execute()
    print("Exiting feedbacks_get()...")
    return HttpResponse(response.__str__())


def feedback_insert(request):
    print("Entering feedbacks_insert()...")
    response = FeedbackInsertAdapter(request).execute()
    print("Exiting feedbacks_insert()...")
    return HttpResponse(response.__str__())


def file_copy(request):
    print("Entering file_copy()...")
    response = FileCopyAdapter(request).execute()
    print("Exiting file_copy()...")
    return HttpResponse(response.__str__())


def file_delete(request):
    print("Entering file_delete()...")
    response = FileDeleteAdapter(request).execute()
    print("Exiting file_delete()...")
    return HttpResponse(response.__str__())


def file_ls(request):
    print("Entering file_ls()...")
    response = FileLsAdapter(request).execute()
    print("Exiting file_ls()...")
    return HttpResponse(response.__str__())


def file_mkdir(request):
    print("Entering file_mkdir()...")
    response = FileMkdirAdapter(request).execute()
    print("Exiting file_mkdir()...")
    return HttpResponse(response.__str__())


def file_move(request):
    print("Entering file_move()...")
    response = FileMoveAdapter(request).execute()
    print("Exiting file_move()...")
    return HttpResponse(response.__str__())


def file_rename(request):
    print("Entering file_rename()...")
    response = FileRenameAdapter(request).execute()
    print("Exiting file_rename()...")
    return HttpResponse(response.__str__())


def file_upload(request):
    print("Entering file_upload()...")
    response = FileUploadAdapter(request).execute()
    print("Exiting file_upload()...")
    return HttpResponse(response.__str__())


def prev_sessions(request):
    print("Entering prev_sessions()...")
    response = PreviousSessionsAdapter(request).execute()
    print("Exiting prev_sessions()...")
    return HttpResponse(response.__str__())


def start_sesssion(request):
    print("Entering start_session()...")
    response = FileRenameAdapter(request).execute()
    print("Exiting start_session()...")
    return HttpResponse(response.__str__())


def test_upload(request):
    print("Entering start_session()...")
    #response = FileUploadAdapter(request).execute()
    print("Exiting start_session()...")
    return render(request, 'core/simple_upload.html')
