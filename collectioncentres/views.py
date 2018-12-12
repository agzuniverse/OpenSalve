from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import views
from rest_framework.response import Response

from collectioncentres.models import CollectionCentre
from collectioncentres.serializers import *
from help.permissions import IsVolunteer


class CollectionCentreList(generics.ListCreateAPIView):
    """Get/Add collection centre
    get:
    Get all collection centres
    post:
    Add a collection centre
    """

    # permission_classes = (
    #     IsAuthenticatedOrReadOnly,
    #     IsVolunteer,
    # )

    serializer_class = CollectionCentreSerializer
    queryset = CollectionCentre.objects.all()


class CollectionCentreView(generics.RetrieveAPIView):
    """Get info about a collection centre
    """
    serializer_class = CollectionCentreSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        collection_centre = CollectionCentre.objects.filter(id=id)
        return collection_centre

    def get_serializer_context(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        return {
            'collection_centre_id': id,
            'request': self.request
        }


class CollectionCentreStockView(views.APIView):
    """
    post:
    Add information about stock item needed
    """
    # permission_classes = (
    #     IsAuthenticated,
    # )

    def post(self, request, id):
        supply = request.data['supply']
        existing_supplies = CollectionCentre.objects.filter(
            id=id).values('supplies').first()['supplies']
        CollectionCentre.objects.filter(id=id).update(
            supplies=existing_supplies+','+supply)

        return Response("success")

class CollectionCentreStockDelete(views.APIView):
     def post(self, request, id):
        supply = request.data['supply']
        existing_supplies = CollectionCentre.objects.filter(
            id=id).values('supplies').first()['supplies'].split(",")
        if supply in existing_supplies:
            existing_supplies.remove(supply)
        CollectionCentre.objects.filter(id=id).update(
            supplies=",".join(existing_supplies))

        return Response("success")
