from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),#admin管理者専用ページの設定
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # add 何もパスを指定しない場合のページを指定する
    path('accounts/', include('accounts.urls')),#アカウント系のページのパスを設定する（ただし該当するパス名等が存在しない場合はテンプレート（Djangoのデォルト）が呼び出される）
    path('accounts/', include('django.contrib.auth.urls')),
    path('layworth/', TemplateView.as_view(template_name='main.html'), name='layworth'),  # add メイン画面のパスを設定する
]
