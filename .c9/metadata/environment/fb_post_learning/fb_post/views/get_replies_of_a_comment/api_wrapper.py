{"changed":true,"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post/views/get_replies_of_a_comment/api_wrapper.py","value":"from django.http import HttpResponse\nfrom django_swagger_utils.drf_server.utils.decorator.interface_decorator \\\n    import validate_decorator\nfrom raven.utils import json\nfrom .validator_class import ValidatorClass\nfrom fb_post.utils import get_replies_for_comment\nfrom fb_post.utils.exceptions import (InvalidCommentException)\nfrom fb_post.constants.exception_messages import (INVALID_COMMENT)\nfrom django_swagger_utils.drf_server.exceptions import NotFound\n\n\n@validate_decorator(validator_class=ValidatorClass)\ndef api_wrapper(*args, **kwargs):\n    comment_id = kwargs[\"comment_id\"]\n\n    try:\n        replies_list = get_replies_for_comment(comment_id=comment_id)\n    except InvalidCommentException:\n        raise NotFound(*INVALID_COMMENT)\n\n    data = json.dumps(replies_list)\n    response = HttpResponse(data, status=200)\n    return response\n    # ---------MOCK IMPLEMENTATION---------\n","undoManager":{"mark":-2,"position":2,"stack":[[{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"remove","lines":[" "],"id":4},{"start":{"row":20,"column":37},"end":{"row":20,"column":38},"action":"remove","lines":[":"]},{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"remove","lines":["'"]},{"start":{"row":20,"column":35},"end":{"row":20,"column":36},"action":"remove","lines":["t"]},{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"remove","lines":["s"]},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"remove","lines":["i"]},{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"remove","lines":["l"]},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"remove","lines":["_"]},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"remove","lines":["s"]},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"remove","lines":["e"]},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["i"]},{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"remove","lines":["l"]},{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"remove","lines":["p"]},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"remove","lines":["e"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["r"]}],[{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"remove","lines":["'"],"id":5},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"remove","lines":["{"]}],[{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"remove","lines":["}"],"id":6}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":34},"end":{"row":20,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588917132720}