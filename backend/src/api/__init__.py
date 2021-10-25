from flask_restx.api import Api
from flask_restx import Api

from .users import ns as user_ns
from .scans import ns as scans_ns
from .stats import ns as stats_ns
from .leaderboard import ns as leaderboard_ns
from .products import ns as products_ns

api = Api(
    title='Asso card API',
    version='1.0',
    description='Work in progress',
)

api.add_namespace(user_ns, path="/api")
api.add_namespace(scans_ns, path="/api")
api.add_namespace(stats_ns, path="/api")
api.add_namespace(leaderboard_ns, path="/api")
api.add_namespace(products_ns, path="/api")
