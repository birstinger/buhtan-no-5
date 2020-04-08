from flask import jsonify
from flask_restful import Resource, reqparse
from endpoints import Auxiliary
from endpoints.rating import ratingsys


class RateStudy(Resource):

    @Auxiliary.auth_dec
    def post(self,**kwargs):
        """Rates a study.

        If the user is submitting a duplicate review (all fields the same), this endpoint will fail.

        Args:
            study_id (Integer): The identifier of the study being rated.
            user_id (String): The identifier of the user rating the study.
            name (String): The name of the user, as it will be displayed for this review.
            rating (Integer): The rating the user is apllying to the study, from the range [0-5]
            occupation (String): The occupation of the user, as it will be displayed for this review.
            comment (String): The comment the user is making about the study for this review.

        Returns:
            JSON: {Success: True} if the rating was made successfully.
        """
        # obtain parameters
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("study_id", type=int, required=True, help="The integer identifier of the study to rate.")
        parser.add_argument("name", type=str, required=True, help="The name to be displayed for this review.")
        parser.add_argument("rating", type=int, required=True, choices=(0, 1, 2, 3, 4, 5),
                            help="The integer [0-5] rating being given to the study.")
        parser.add_argument("occupation", type=str, required=True,
                            help="The occupation to be displayed for this review.")
        parser.add_argument("comment", type=str, required=True, help="The comment to be displayed for this review")

        returned_args = parser.parse_args()

        study_id = returned_args.get("study_id", None)
        name = returned_args.get("name", None)
        rating = returned_args.get("rating", None)
        occupation = returned_args.get("occupation", None)
        comment = returned_args.get("comment", None)
        user_id = kwargs["user_id"]

        ratingsys(study_id, user_id, name, occupation, rating, comment)

        return jsonify({"Success": True})
