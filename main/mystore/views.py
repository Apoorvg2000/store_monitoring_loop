"""
This module defines the views used in the store monitoring application. It contains function-based views that handle various webpage requests to render the appropriate templates with context data or perform certain actions based on user requests.
"""
from django.shortcuts import render
from .models import StoreReport, ReportStatus
from mystore.helper import trigger_report_combined
from django.conf import settings
from threading import Thread
import logging
import csv

# Create your views here.

# The `index` view renders the homepage template.
# It takes a request object and returns an HttpResponse.
def index(request):
    return render(request, 'index.html')

# The `trigger_report` view initiates the generation of a store report.
# It creates a new StoreReport object, starts a thread to generate the report, and renders the 'trigger_report.html' with the report ID.
# It takes a request object and returns an HttpResponse.
def trigger_report(request):
    report = StoreReport.objects.create(status=ReportStatus.PENDING)

    # Created a thread to generate report so that the report id is shown to user even if the report
    # genertion is in progress.
    thread = Thread(target=trigger_report_combined, args=(report,))
    thread.start()
    data = {
        'report_id': report.id,
        'status': 200
    }
    return render(request, 'trigger_report.html', data)

# The `get_report` view fetches the status and details of a specific report based on a provided report ID.
# It handles the case where the report ID is invalid and returns the appropriate HttpResponse.
# It takes a request object and returns an HttpResponse with the report status or an error message.
def get_report(request):
    report_id = request.GET['report_id']

    # if report_id exists in database, then show report status, otherwise, inform user that report_id is wrong.
    try:
        report = StoreReport.objects.get(id=report_id)
    except Exception:
        data = {
            'message': "The report ID entered is not valid. Please enter a valid report ID.",
            'status': 404
        }
        logging.error("The report ID entered is not valid. Please enter a valid report ID.")
        return render(request, "get_report.html", data)
        
    if report.status == ReportStatus.COMPLETED:
        rows = []
        report_url = settings.MEDIA_ROOT + "/" + report.report_url.name

        with open(report_url, "r") as csv_file:
            csv_data = csv.reader(csv_file)
            for lines in csv_data:
                rows.append(lines)

        data = {
            'message': "Completed",
            'status': 200,
            'report_url': report_url,
            'rows': rows
        }
        return render(request, "get_report.html", data)
    else:
        data = {
            'message': "Running",
            'status': 200,
            'report_url': ""
        }
        return render(request, "get_report.html", data)
