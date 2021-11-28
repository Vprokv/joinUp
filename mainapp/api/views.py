from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "John"}]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3, "name": "axaxa"}, status=status.HTTP_201_CREATED)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_program": 1,
                "program_name": "Адаптация HR специалиста",
                "description": "Программа адаптации предназначена для новых специалистов",
                "duration_day": 16,
                "tier": 12,
                "id_customer": 2,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2
            },
            {
                "id_program": 2,
                "program_name": "Адаптация менеджера по продажам",
                "description": "Программа адаптации предназначена для новых специалистов",
                "duration_day": 21,
                "tier": 12,
                "id_customer": 2,
                "status": 4,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2
            },

        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationLevelTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_level": 1,
                "level_name": "Общие сведения",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_program": [1, 2]
            },
            {
                "id_level": 2,
                "level_name": "Должностные инструкции",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 4,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 12,
                "id_program": [3, 7]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationStageTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationBlockTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationGoalTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationDocumentTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationContactTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class LnkLevelProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class LnkStageLevelTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class LnkGoalProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class LnkDocumentProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class LnkContactProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class LicensePackTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserServiceUserTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserServiceSMSTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserServiceTokenTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserServiceCandidateTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class IEmployeeServiceAuthenticationTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class RequestUserToken(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class IAdaptationProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class ILevelStagesTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class IGoalsTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class IDocumentsTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class IContactsTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class IBlocksTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
