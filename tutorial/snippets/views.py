from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    列出所有的snippets，或创建一个新的snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    获取，更新或删除一个code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
