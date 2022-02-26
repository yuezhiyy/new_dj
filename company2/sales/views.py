from django.shortcuts import render
from django.http import HttpResponse
from common.models import Customer


# Create your views here.
def listorders(resquest):
    return HttpResponse('下面是所有订单信息：')  # 返回一个字符串


# # 1、读取数据库表记录
# # 导入Customer对象定义（上面）
#
# def listcustomers(request):
#     # 返回一个QuerySet对象，包含所有的表记录，每条表记录都是一个dict对象，{‘字段名’：‘字段值’}
#     qs = Customer.objects.values()  # objects 操作数据库 manage接口
#
#     # 定义返回字符串
#     retStr = ''
#     for custumer in qs:
#         for name, value in custumer.items():
#             retStr += f'{name}:{value}|'
#
#         retStr += '<br>'  # <br>表示换行
#     return HttpResponse(retStr)

# # 2、添加过滤条件
# def listcustomers(request):
#     # 返回一个 QuerySet 对象 ，包含所有的表记录
#     qs = Customer.objects.values()
#
#     # 检查url中是否有参数phone_number
#     ph = request.GET.get('phone_number', None)
#
#     # 如果有，添加过滤条件  filter
#     if ph:
#         qs = qs.filter(phone_number=ph)
#
#     # 定义返回字符串
#     retStr = ''
#     for customer in qs:
#         for name, value in customer.items():
#             retStr += f'{name} : {value} | '
#         # <br> 表示换行
#         retStr += '<br>'
#
#     return HttpResponse(retStr)

# # 3、用html显示，先定义好HTML模板
# html_template = '''
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="UTF-8">
# <style>
# table {
#     border-collapse: collapse;
# }
# th, td {
#     padding: 8px;
#     text-align: left;
#     border-bottom: 1px solid #ddd;
# }
# </style>
# </head>
#     <body>
#         <table>
#         <tr>
#         <th>id</th>
#         <th>姓名</th>
#         <th>电话号码</th>
#         <th>地址</th>
#         </tr>
#
#         %s
#
#
#         </table>
#     </body>
# </html>
# '''
#
#
# def listcustomers(request):
#     # 返回一个 QuerySet 对象 ，包含所有的表记录
#     qs = Customer.objects.values()
#
#     # 检查url中是否有参数phone_number
#     ph = request.GET.get('phone_number', None)
#
#     # 如果有，添加过滤条件
#     if ph:
#         qs = qs.filter(phone_number=ph)
#
#     # 生成html模板中要插入的html片段内容
#     tableContent = ''
#     for customer in qs:
#         tableContent += '<tr>'
#
#         for name, value in customer.items():
#             tableContent += f'<td>{value}</td>'
#
#         tableContent += '</tr>'
#
#     return HttpResponse(html_template % tableContent)


# 使用Django的模板引擎,先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        {% for customer in customers %}
            <tr>

            {% for name, value in customer.items %}            
                <td>{{ value }}</td>            
            {% endfor %}

            </tr>
        {% endfor %}

        </table>
    </body>
</html>
'''

from django.template import engines  # 使用django模板可以处理多个内容需要拼接的情况

django_engine = engines['django']
template = django_engine.from_string(html_template)


def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phone_number
    ph = request.GET.get('phone_number', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phone_number=ph)

    # 传入渲染模板需要的参数
    rendered = template.render({'customers': qs})

    return HttpResponse(rendered)
