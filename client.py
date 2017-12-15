# Library imports
import grpc
import logging

# Local imports
from matches_pb2 import CareerHistoryRating
from matches_pb2 import CareerMatchesRequest
from matches_pb2 import ScaleScore
import matches_pb2_grpc


# Logging config
logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

channel = grpc.insecure_channel('localhost:50051')
stub = matches_pb2_grpc.CareerMatchesServiceStub(channel)

# Make a request...

logging.debug('Making a request...')
request = CareerMatchesRequest(
    scale_scores=[
        ScaleScore(scale_id=1, score=1.0),
        ScaleScore(scale_id=2, score=1.0),
        ScaleScore(scale_id=3, score=1.0),
    ],
    career_history_ratings=[
        CareerHistoryRating(career_id=1, rating=5.0),
        CareerHistoryRating(career_id=2, rating=5.0),
        CareerHistoryRating(career_id=3, rating=5.0),
    ]
)
matches = stub.GetMatches(request)
logging.debug('Request completed with %s' % str(matches))
