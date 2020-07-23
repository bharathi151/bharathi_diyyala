{"changed":true,"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post_v2/views/get_posts_details/api_wrapper.py","value":"from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\\n    import validate_decorator\nfrom .validator_class import ValidatorClass\n\n\n@validate_decorator(validator_class=ValidatorClass)\ndef api_wrapper(*args, **kwargs):\n    # ---------MOCK IMPLEMENTATION---------\n    try:\n        from fb_post_v2.views.get_posts_details.tests.test_case_01 \\\n            import TEST_CASE as test_case\n    except ImportError:\n        from fb_post_v2.views.get_posts_details.tests.test_case_01 \\\n            import test_case\n\n    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\\n        import mock_response\n    try:\n        from fb_post_v2.views.get_posts_details.request_response_mocks \\\n            import RESPONSE_200_JSON\n    except ImportError:\n        RESPONSE_200_JSON = ''\n    response_tuple = mock_response(\n        app_name=\"fb_post_v2\", test_case=test_case,\n        operation_name=\"get_posts_details\",\n        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,\n        group_name=\"\")\n    return response_tuple[1]","undoManager":{"mark":3,"position":5,"stack":[[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":2}],[{"start":{"row":8,"column":4},"end":{"row":13,"column":19},"action":"insert","lines":["print(\"******\")","    print(kwargs)","    print(\"******\")","    print(\"******\")","    print(args)","    print(\"******\")"],"id":3}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"remove","lines":["*"],"id":4},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["*"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"remove","lines":["*"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"remove","lines":["*"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"remove","lines":["*"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"remove","lines":["*"]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["/"],"id":5},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["/"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["/"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["/"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["/"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["/"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["/"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["/"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["/"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["/"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["/"]},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["/"]},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["/"]},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["/"]},{"start":{"row":10,"column":25},"end":{"row":10,"column":26},"action":"insert","lines":["/"]},{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"insert","lines":["/"]},{"start":{"row":10,"column":27},"end":{"row":10,"column":28},"action":"insert","lines":["/"]},{"start":{"row":10,"column":28},"end":{"row":10,"column":29},"action":"insert","lines":["/"]},{"start":{"row":10,"column":29},"end":{"row":10,"column":30},"action":"insert","lines":["/"]},{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"insert","lines":["/"]},{"start":{"row":10,"column":31},"end":{"row":10,"column":32},"action":"insert","lines":["/"]}],[{"start":{"row":8,"column":3},"end":{"row":13,"column":19},"action":"remove","lines":[" print(\"******\")","    print(kwargs)","    print(\"/////////////////////\")","    print(\"******\")","    print(args)","    print(\"******\")"],"id":6},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"remove","lines":[" "]},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"remove","lines":[" "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":7,"column":43},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":7}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":43},"end":{"row":7,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590812792513}