{"filter":false,"title":"api_wrapper.py","tooltip":"/fb_post_learning/fb_post_v2/views/react_to_post/api_wrapper.py","ace":{"folds":[],"scrolltop":173.94061979237077,"scrollleft":0,"selection":{"start":{"row":32,"column":0},"end":{"row":32,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"hash":"4369e2b8ca1fb89374426bb8807a8792dbf60910","undoManager":{"mark":42,"position":42,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from fb_post_v2.views.react_to_post.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from fb_post_v2.views.react_to_post.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from fb_post_v2.views.react_to_post.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"fb_post_v2\", test_case=test_case,","        operation_name=\"react_to_post\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":34,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","","from fb_post_v2.interactors.create_comment_interactor import \\","    CreateCommentInteractor","from fb_post_v2.presenters.presenter_implementation import PresenterImplementation","from fb_post_v2.storages.comment_storage_implementation import StorageImplementation","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    request_data = kwargs['request_data']","    post_id = kwargs[\"post_id\"]","    comment_content = request_data['content']","    user = kwargs['user']","    user_id = user.id","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = CreateCommentInteractor(","        storage=storage,","        presenter=presenter","    )","","    comment_id_dict = interactor.create_comment(","        post_id=post_id,","        comment_content=comment_content,","        user_id=user_id)","","    response_data = json.dumps(comment_id_dict)","    return HttpResponse(response_data, status=201)",""]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["t"],"id":3},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["n"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"remove","lines":["e"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"remove","lines":["m"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"remove","lines":["m"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"remove","lines":["o"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"remove","lines":["C"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"remove","lines":["e"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["t"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":["a"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":["e"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":["r"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":["C"],"id":4}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["R"],"id":5},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["e"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["a"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":["a"],"id":6},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":["e"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["e"],"id":7},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["a"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["c"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["t"],"id":8},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["n"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["e"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["m"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["m"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["o"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["c"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["_"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["e"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["t"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["a"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["e"],"id":9},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"remove","lines":["r"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"remove","lines":["c"]}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["r"],"id":10},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["e"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":42},"action":"remove","lines":["rea_interactor"],"id":11},{"start":{"row":6,"column":28},"end":{"row":6,"column":49},"action":"insert","lines":["react_post_interactor"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["P"],"id":12},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["o"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["s"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["T"],"id":13}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":24},"action":"remove","lines":["ReactTPostInteractor"],"id":14},{"start":{"row":7,"column":4},"end":{"row":7,"column":25},"action":"insert","lines":["ReactToPostInteractor"]}],[{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"remove","lines":["t"],"id":15},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["n"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":["e"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"remove","lines":["m"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"remove","lines":["m"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["o"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["c"],"id":16}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["r"],"id":17},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":50},"action":"remove","lines":["re_storage_implementation"],"id":18},{"start":{"row":9,"column":25},"end":{"row":9,"column":56},"action":"insert","lines":["reaction_storage_implementation"]}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":40},"action":"remove","lines":["CreateCommentInteractor"],"id":19},{"start":{"row":22,"column":17},"end":{"row":22,"column":38},"action":"insert","lines":["ReactToPostInteractor"]}],[{"start":{"row":17,"column":36},"end":{"row":17,"column":43},"action":"remove","lines":["content"],"id":20}],[{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["r"],"id":21},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["e"]},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["a"]}],[{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["c"],"id":22},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"insert","lines":["t"]},{"start":{"row":17,"column":41},"end":{"row":17,"column":42},"action":"insert","lines":["i"]},{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"remove","lines":["n"],"id":23}],[{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"insert","lines":["o"],"id":24},{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"insert","lines":["n"]},{"start":{"row":17,"column":44},"end":{"row":17,"column":45},"action":"insert","lines":["_"]},{"start":{"row":17,"column":45},"end":{"row":17,"column":46},"action":"insert","lines":["t"]},{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"insert","lines":["y"]}],[{"start":{"row":17,"column":36},"end":{"row":17,"column":47},"action":"remove","lines":["reaction_ty"],"id":25},{"start":{"row":17,"column":36},"end":{"row":17,"column":49},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":47},"action":"remove","lines":["create_comment"],"id":26}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["r"],"id":27},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":35},"action":"remove","lines":["re"],"id":28},{"start":{"row":27,"column":33},"end":{"row":27,"column":46},"action":"insert","lines":["react_to_post"]}],[{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"remove","lines":[" "],"id":29},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"remove","lines":["="]},{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"remove","lines":[" "]},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"remove","lines":["t"]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"remove","lines":["c"]},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"remove","lines":["i"]},{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"remove","lines":["d"]},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"remove","lines":["_"]},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"remove","lines":["d"]},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"remove","lines":["i"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"remove","lines":["_"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"remove","lines":["t"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"remove","lines":["n"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"remove","lines":["e"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"remove","lines":["m"]}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"remove","lines":["m"],"id":30},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"remove","lines":["o"]},{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":30,"column":23},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":31,"column":0},"end":{"row":31,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":8},"action":"remove","lines":["    "],"id":32}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":23},"action":"remove","lines":["comment_content"],"id":33}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["r"],"id":34},{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":10},"action":"remove","lines":["re"],"id":35},{"start":{"row":29,"column":8},"end":{"row":29,"column":21},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":29,"column":22},"end":{"row":29,"column":37},"action":"remove","lines":["comment_content"],"id":36}],[{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["r"],"id":37},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":29,"column":22},"end":{"row":29,"column":24},"action":"remove","lines":["re"],"id":38},{"start":{"row":29,"column":22},"end":{"row":29,"column":35},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":19},"action":"remove","lines":["comment_content"],"id":39}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["r"],"id":40},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["e"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["a"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":7},"action":"remove","lines":["rea"],"id":41},{"start":{"row":17,"column":4},"end":{"row":17,"column":17},"action":"insert","lines":["reaction_type"]}],[{"start":{"row":34,"column":38},"end":{"row":34,"column":39},"action":"remove","lines":[" "],"id":42},{"start":{"row":34,"column":37},"end":{"row":34,"column":38},"action":"remove","lines":[","]},{"start":{"row":34,"column":36},"end":{"row":34,"column":37},"action":"remove","lines":["a"]},{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"remove","lines":["t"]},{"start":{"row":34,"column":34},"end":{"row":34,"column":35},"action":"remove","lines":["a"]},{"start":{"row":34,"column":33},"end":{"row":34,"column":34},"action":"remove","lines":["d"]},{"start":{"row":34,"column":32},"end":{"row":34,"column":33},"action":"remove","lines":["_"]},{"start":{"row":34,"column":31},"end":{"row":34,"column":32},"action":"remove","lines":["e"]},{"start":{"row":34,"column":30},"end":{"row":34,"column":31},"action":"remove","lines":["s"]},{"start":{"row":34,"column":29},"end":{"row":34,"column":30},"action":"remove","lines":["n"]},{"start":{"row":34,"column":28},"end":{"row":34,"column":29},"action":"remove","lines":["o"]},{"start":{"row":34,"column":27},"end":{"row":34,"column":28},"action":"remove","lines":["p"]},{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"remove","lines":["s"]},{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"remove","lines":["e"]}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["r"],"id":43}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":47},"action":"remove","lines":["    response_data = json.dumps(comment_id_dict)"],"id":44},{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"remove","lines":["",""]}]]},"timestamp":1590425055580}