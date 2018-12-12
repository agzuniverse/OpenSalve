from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from help.models import Requests, Comments
from help.permissions import IsVolunteer, IsPhoneAuthenticated
from help.serializers import RequestsStatusSerializer, RequestsSerializer
from help.serializers import RequestCommentsRead, RequestCommentsWrite
from rest_framework import views
from rest_framework.response import Response


class Request(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all requests
    post:
    Add a request
    """

    serializer_class = RequestsSerializer
    queryset = Requests.objects.all()


class RequestView(generics.RetrieveUpdateAPIView):
    """Get info about a help request
    """
    serializer_class = RequestsSerializer

    lookup_url_kwarg = 'id'

    # permission_classes = (
    #     IsPhoneAuthenticated,
    # )

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        request = Requests.objects.filter(id=id)
        return request


class RequestStatus(generics.RetrieveUpdateAPIView):
    """Get/Set status of request
    get:
    Get status of request
    patch:
    Set status of request
    """
    serializer_class = RequestsStatusSerializer

    lookup_url_kwarg = 'id'

    # permission_classes = (
    #     IsAuthenticatedOrReadOnly,
    #     IsVolunteer,
    # )

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        request = Requests.objects.filter(id=id)
        return request


class RequestStatusChange(views.APIView):
    def get(self, request, id):
        curr_status = Requests.objects.filter(
            id=id).values('status').first()['status']
        Requests.objects.filter(id=id).update(
            status="Teams have responded to the request")

        return Response("success")


class RequestComments(generics.ListCreateAPIView):
    """Get/Add comments of/to request
    get:
    Get all comments of request
    post:
    Add a comment to request
    """

    # permission_classes = (
    #     IsAuthenticatedOrReadOnly,
    # )

    queryset = Comments.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RequestCommentsWrite

        return RequestCommentsRead
