from django.urls import path

from .views import ProgramTestAPIView

urlpatterns = {
    path('program/', ProgramTestAPIView.as_view(), name='program'),
    path('adaptationprogram/', AdaptationProgramTestAPIView.as_view(), name='adaptation program'),
    path('adaptationlevel/', AdaptationLevelTestAPIView.as_view(), name='adaptation level'),
    path('adaptationstage/', AdaptationStageTestAPIView.as_view(), name='adaptation stage'),
    path('adaptationblock/', AdaptationBlockTestAPIView.as_view(), name='adaptation block'),
    path('adaptationbgoal/', AdaptationGoalTestAPIView.as_view(), name='adaptation goal'),
    path('adaptationdocument/', AdaptationDocumentTestAPIView.as_view(), name='adaptation document'),
    path('adaptationcontact/', AdaptationContactTestAPIView.as_view(), name='adaptation contact'),
    path('lnklevelprogram/', LnkLevelProgramTestAPIView.as_view(), name='lnk level program'),
    path('lnkstagelevel/', LnkStageLevelTestAPIView.as_view(), name='lnk stage level'),
    path('lnkgoalprogram/', LnkGoalProgramTestAPIView.as_view(), name='lnk goal program'),
    path('lnkdocumentprogram/', LnkDocumentProgramTestAPIView.as_view(), name='lnk document program'),
    path('lnkpcontactrogram/', LnkContactProgramTestAPIView.as_view(), name='lnk contact program'),
    path('customer/', CustomerTestAPIView.as_view(), name='customer'),
    path('licensepack/', LicensePackTestAPIView.as_view(), name='license Pack'),
    path('userservice/user/', UserServiceUserTestAPIView.as_view(), name='user service(user)'),
    path('userservice/sms/', UserServiceSMSTestAPIView.as_view(), name='user service(sms)'),
    path('userservice/token/', UserServiceTokenTestAPIView.as_view(), name='user service(token)'),
    path('userservice/candidate/', UserServiceCandidateTestAPIView.as_view(), name='candidate'),
    path('employee/', EmployeTestAPIView.as_view(), name='candidate'),
}