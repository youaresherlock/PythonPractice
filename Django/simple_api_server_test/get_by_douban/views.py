#coding:utf-8
import requests

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class Music(View):
    DOUBAN_MUSIC_API = 'https://api.douban.com/v2/music/search?q={0}'
    def get(self, request):
        music_name = request.GET.get('musicname', '')
        if not music_name:
            return JsonResponse({'errcode': -1, 'errmsg': '音乐名称不能为空'})
        url = self.DOUBAN_MUSIC_API.format(music_name)
        response = requests.get(url)
        data = response.json()
        return JsonResponse({'errcode': 0, 'errmsg': '成功', 'data': data})


class Movie(View):
    DOUBAN_MOVIE_API = 'https://api.douban.com/v2/movie/search?q={0}'
    def get(self, request):
        movie_name = request.GET.get('moviename', '')
        if not movie_name:
            return JsonResponse({'errcode': -1, 'errmsg': '电影名称不为空'})

        url = self.DOUBAN_MOVIE_API.format(movie_name)

        try:
            response = request.get(url)
        except Exception as e :
            return JsonResponse({'errcode': -1, 'errmsg': str(e)})

        if response.status_code != 200:
            return JsonResponse({'errcode': -1, 'errmsg': '请求豆瓣异常'})

        data = response.json()
        return JsonResponse({'errcode': 0, 'errmsg': '成功', 'data': data})

class Book(View):
    DOUBAN_BOOK_API = 'https://api.douban.com/v2/book/search?q={0}'
    def get(self, request):
        book_name = request.GET.get('bookname', '')
        if not book_name:
            return JsonResponse({'errcode': -1, 'errmsg': '图书名称不为空'})

        url = self.DOUBAN_BOOK_API.format(book_name)
        response = request.get(url)
        data = response.json()
        return JsonResponse({'errcode': 0, 'errmsg': '成功', 'data': data})







































