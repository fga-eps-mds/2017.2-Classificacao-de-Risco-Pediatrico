from apps.risk_rating.apps import RiskRatingConfig


class TestRiskRating:

    def test_app(self):
        assert RiskRatingConfig.name == 'apps.risk_rating'
