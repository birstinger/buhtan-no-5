from flask import Blueprint
from flask_restful import Api
from endpoints.Deliver import Deliver
from endpoints.Purchase import Purchase
from database import studies
from gui_endpoints import preview_study
from endpoints.Search import Search
from endpoints.IsOwned import IsOwned
from endpoints.GetOwned import GetOwned
from endpoints.GetViewed import GetViewed
from endpoints.GetWishList import GetWishList
from endpoints.Upload import Upload
from endpoints.GetAdminDetails import GetAdminDetails
from endpoints.GetPending import GetPending
from endpoints.ReviewPending import ReviewPending
from endpoints.GetPreview import GetPreview
from endpoints.GetImage import GetImage
from endpoints.UploadImage import UploadImage
from endpoints.suggestions import TextSuggestion
from endpoints.AddWishlist import AddWishlist
from endpoints.RemoveWishlist import RemoveWishlist
from endpoints.IsWishlisted import IsWishlisted
from endpoints.RateStudy import RateStudy

trans_bp = Blueprint('transaction', __name__)
api = Api(trans_bp)

api.add_resource(Deliver, '/deliver')
api.add_resource(Purchase, '/purchase')
api.add_resource(studies.EndPointOwnedStudies, '/owned')
api.add_resource(studies.EndPointViewedStudies, '/previewed')
api.add_resource(preview_study.EndPoint_PreviewStudies, '/studyPreview')
api.add_resource(Search, '/search')
api.add_resource(IsOwned, '/isOwned')
api.add_resource(GetOwned, '/getOwned')
api.add_resource(GetViewed, '/getViewed')
api.add_resource(GetWishList, '/getWishlist')
api.add_resource(Upload, '/upload')
api.add_resource(GetAdminDetails, '/getAdminDetails')
api.add_resource(GetPending, '/getPending')
api.add_resource(ReviewPending, '/reviewPending')
api.add_resource(GetPreview, '/getPreview')
api.add_resource(GetImage, '/getImage')
api.add_resource(UploadImage, '/uploadImage')
api.add_resource(TextSuggestion,'/suggestion')
api.add_resource(AddWishlist, '/addWishlist')
api.add_resource(RemoveWishlist, '/removeWishlist')
api.add_resource(IsWishlisted, '/isWishlisted')
api.add_resource(RateStudy, '/rateStudy')