from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings
from io import BytesIO
import xlwt
import datetime
import pytz


class ExcelResponse(HttpResponse):

    def __init__(self, data, headers, output_name='excel_data', force_csv=False, encoding='utf8'):
        if isinstance(data, QuerySet):
            data = list(data.values())

        output = BytesIO()
        if len(data) <= 65536 and force_csv is not True:
            book = xlwt.Workbook(encoding=encoding)
            sheet = book.add_sheet('Sheet 1')
            styles = {
                'datetime': xlwt.easyxf(num_format_str='yyyy-mm-dd hh:mm:ss'),
                'date': xlwt.easyxf(num_format_str='yyyy-mm-dd'),
                'time': xlwt.easyxf(num_format_str='hh:mm:ss'),
                'default': xlwt.Style.default_style
            }
            for row, header in enumerate(headers):
                sheet.write(0, row, header)

            for rowx, entry in enumerate(data):
                rowx = rowx + 1
                for colx, headerName in enumerate(headers):
                    if isinstance(entry[headerName], datetime.datetime):
                        if timezone.is_aware(entry[headerName]):
                            entry[headerName] = timezone.make_naive(entry[headerName], pytz.timezone(settings.TIME_ZONE))
                        cell_style = styles['datetime']
                    if isinstance(entry[headerName], datetime.datetime):
                        cell_style = styles['datetime']
                    elif isinstance(entry[headerName], datetime.date):
                        cell_style = styles['date']
                    elif isinstance(entry[headerName], datetime.time):
                        cell_style = styles['time']
                    else:
                        cell_style = styles['default']
                    sheet.write(rowx, colx, entry[headerName], style=cell_style)
            book.save(output)
            content_type = 'application/vnd.ms-excel'
            file_ext = 'xls'
        else:
            # for row in data:
            #     out_row = []
            #     for value in row:
            #         if not isinstance(value, basestring):
            #             value = unicode(value)
            #         value = value.encode(encoding)
            #         out_row.append(value.replace('"', '""'))
            #     output.write('"%s"\n' % '","'.join(out_row))
            content_type = 'text/csv'
            file_ext = 'csv'
        super(ExcelResponse, self).__init__(content=output.getvalue(), content_type=content_type)
        self['Content-Disposition'] = 'attachment;filename="%s.%s"' % (output_name.replace('"', '\"'), file_ext)
