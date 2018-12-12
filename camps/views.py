from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from camps.models import Camps, CampInhabitants
from camps.serializers import CampsSerializer, CampInhabitantsSerializer
from help.permissions import IsVolunteer
from rest_framework import views
from rest_framework.response import Response


class Camp(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all camps
    post:
    Add a camp
    """

    # permission_classes = (
    #     IsAuthenticatedOrReadOnly,
    #     IsVolunteer,
    # )

    serializer_class = CampsSerializer
    queryset = Camps.objects.all()


class CampView(generics.RetrieveAPIView):
    """Get info about a camp
    """
    serializer_class = CampsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        camp = Camps.objects.filter(id=id)
        return camp


class CampInhabitantsView(generics.ListCreateAPIView):
    """Get/Add inhabitant
    get:
    Get all inhabitants in camp
    post:
    Add a inhabitant to camp
    """

    serializer_class = CampInhabitantsSerializer
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        id = self.kwargs.get(self.lookup_url_kwarg)
        serializer.save(camp=Camps.objects.get(id=id))

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        camp = CampInhabitants.objects.filter(camp=id)
        return camp


class CampInhabitantsDelete(views.APIView):
    def get(self, request, id, inhab_id):
        all_inhabs = CampInhabitants.objects.filter(camp=id)
        for inhab in all_inhabs:
            if(inhab.id == inhab_id):
                inhab.delete()
        return Response("success")


class CampStockView(views.APIView):
    """
    post:
    Add information about stock item needed
    """
    # permission_classes = (
    #     IsAuthenticated,
    # )

    def post(self, request, id):
        supply = request.data['supply']
        existing_supplies = Camps.objects.filter(
            id=id).values('supplies').first()['supplies']
        Camps.objects.filter(id=id).update(
            supplies=existing_supplies+','+supply.strip())

        return Response("success")

class CampStockDelete(views.APIView):
     def post(self, request, id):
        supply = request.data['supply']
        existing_supplies = Camps.objects.filter(
            id=id).values('supplies').first()['supplies'].split(",")
        if supply in existing_supplies:
            existing_supplies.remove(supply)
        print(existing_supplies)
        Camps.objects.filter(id=id).update(
            supplies=",".join(existing_supplies))

        return Response("success")