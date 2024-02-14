from rest_framework import generics
from rest_framework.response import Response


from .models import Todo
from .serialazers import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    """
    Bu class Todo yaratish va barcha Todolar
    ro'yhatini qaytarishga xizmat qiladi.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class TodoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Bu class Todoni o'zgarish va o'chirishga
    xizmat qiladi.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        title = instance.title
        self.perform_destroy(instance)
        return Response({"xabar": f"'{title}' muvaffaqiyatli o'chirildi."})
