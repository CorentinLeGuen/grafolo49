from .model import Draw


def list_draws_resolver(obj, info, limit: int = 10, ordered: bool = True):  # NOSONAR
    try:
        draws = [draw.to_dict() for draw in Draw.query.all()]
        if ordered:
            draws.sort(key=lambda d: d['draw_date'], reverse=True)
        payload = {
            "success": True,
            "draw": draws[:limit]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
