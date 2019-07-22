from django.shortcuts import render

# 함수형 뷰
# def my_view(request):
#     myname ='홍길동'
#     context = {'myname': myname }
#     return render(request, 'my_view.html', context)


# 클래스형 뷰
# from django.views.generic import View
#
# class MyView(View):
#     def get(self, request ):
#         myname = '홍길자'
#         context = {'myname' : myname}
#         return render(request, 'my_view.html', context)

# 제네릭뷰
from django.views.generic import TemplateView
class AboutView(TemplateView):
    template_name = 'my_view.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['myname'] = "홍길숙"
        return context
