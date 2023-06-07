from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from . import connection




def home_view(request):
    return render(request, "pages/home.html", {})

@xframe_options_sameorigin
def result(request):
    result_list, column_indexlist = connection.clickhouse_client.execute(query='')
    context = {'result_list': result_list, 'column_indexlist': column_indexlist}
    return render(request, "pages/table.html", context)