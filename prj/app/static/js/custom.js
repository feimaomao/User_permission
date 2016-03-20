var codename,name,name_is
var code_in=0

//查询code
function show(){
	var co = $('#codename').val();
	if (co!=''){
		$.ajax({
			url:'/user_permission/query_code/',
			dataType:'json',//自动把json数据格式转换为js对象
			data:{'codename':co},
			type:'GET',
			success:function(data){
				if(data['codename']){
					$('#name').val(data['name']);
					$('.tishi').removeClass('show')
					$('.tishi').addClass('hide')
					code_in = 1;	
				}
				else{
					$('#name').val('');
					$('.tishi').removeClass('show')
					$('.tishi').addClass('hide')
					code_in = 0;
				}
				codename = data['codename'];
				name = data['name'];
			},
		});
	}
}
//查询name
function examine(){
	var na = $('#name').val();
	if (na!=''){
		$.ajax({
			url:'/user_permission/query_name/',
			dataType:'json',//自动把json数据格式转换为js对象
			data:{'name':na},
			type:'GET',
			success:function(data){
				if(data['name']){
					if(data['name'] != name){
					$('.tishi').removeClass('hide')
					$('.tishi').addClass('show')
					name_is=1;	
					}
					else{
					$('.tishi').removeClass('show')
					$('.tishi').addClass('hide')
					name_is=0;
					}
				}
				else{
					$('.tishi').removeClass('show')
					$('.tishi').addClass('hide')
					name_is=0;
				}
			},
		});
	}
}
//修改和添加，如果code_in判断正确就修改，错误就添加
function modifaction(){
	var na = $('#name').val();
	var co = $('#codename').val();
	if (co!='' && na!=''){
		if (name_is){
			alert('name已经存在请重写输入')
		}
		else{			
			if (code_in){
				$.ajax({
    				url:'/user_permission/updata/',
    				dataType:'json',//自动把json数据格式转换为js对象
    				data:{'codename':co,'name':na,},
    				type:'GET',
    				success:function(data){
    					alert('修改成功');
    					$('#codename').val('');
    					$('#name').val('');
    				},
				});
			}
			else{   					
				//添加操作
				$.ajax({
				url:'/user_permission/add/',
				dataType:'json',//自动把json数据格式转换为js对象
				data:{'codename':co,'name':na,},
				type:'GET',
				success:function(data){
					alert('添加成功');
					$('#codename').val('');
					$('#name').val('');
					},
				});
			}
		}
	}
	else{
		alert('请全部输入')
	}
}
//删除功能
function delete11(){
	if(code_in){
	    $.ajax({
			url:'/user_permission/delete/',
			dataType:'json',//自动把json数据格式转换为js对象
			data:{'codename':codename,},
			type:'GET',
			success:function(data){
				alert('删除成功');
				$('#codename').val('');
				$('#name').val('');
			},
		});
	} 
	else{
		alert('用户不存在');
	}
}