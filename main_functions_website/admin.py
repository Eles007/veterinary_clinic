from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Price,GroupPrice,Article
from django.forms import ModelForm


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основная часть',widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

class PriceErrorForm(ModelForm):
    class Meta:
        model = Price
        fields = "__all__"
        error_messages = {
            "subtitle"   : {'required': "Услуга не может быть пустым"},
            "price"      : {'required': "Цена не может быть пустой"},
            "group_price": {'required': "Категория не может быть пустой"}
        }

class GroupPriceErrorForm(ModelForm):
    class Meta:
        model = GroupPrice
        fields = "__all__"
        error_messages = {
            "name": {'required': "Категория не может быть пустой"}
        }

class PriceInline(admin.TabularInline):
    extra = 0
    model = Price

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    ordering = ('group_price',)
    list_display = ('group_price','subtitle','price')
    list_display_links = ('subtitle',)
    list_editable = ('group_price','price',)
    list_filter = (
        ('group_price', admin.RelatedOnlyFieldListFilter),
    )

    form = PriceErrorForm

@admin.register(GroupPrice)
class GroupPriceAdmin(admin.ModelAdmin):
    ordering = ('position', )
    inlines = [PriceInline,]
    list_display = ['position','name']
    list_display_links = ('name',)
    list_editable = ('position',)
    form = GroupPriceErrorForm

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    form = ArticleAdminForm