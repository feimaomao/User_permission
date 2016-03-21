#coding:utf-8
from django.shortcuts import render,HttpResponse,render_to_response
from query import query_code,query_name,updata,add,delete,query
import json
# 返回权限修改页面
def index(request):
	return render(request,'index.html',locals())
#查询codename
def q_code(request):
	codename = request.GET.get('codename')
	codename = query_code(codename)
	return HttpResponse(json.dumps(codename))
#查询name
def q_name(request):
	name = request.GET.get('name')
	name = query_name(name)
	return HttpResponse(json.dumps(name))
# 添加权限
def u_add(request):
	name = request.GET.get('name')
	codename = request.GET.get('codename')
	content_type_id = 15
	user_add = add(codename,name,content_type_id)
	return HttpResponse(json.dumps(user_add))
# 修改权限
def u_updata(request):
	name = request.GET.get('name')
	codename = request.GET.get('codename')
	user_updata = updata(codename,name)
	return HttpResponse(json.dumps(user_updata))
# 删除权限
def u_delete(request):
	codename = request.GET.get('codename')
	c =delete(codename)
	return HttpResponse(json.dumps(c))
# 查询权限
def u_query(request):
	user_permission = query()
	c = json.dumps(user_permission)
	return render_to_response('query.html', {'user_permission': c})