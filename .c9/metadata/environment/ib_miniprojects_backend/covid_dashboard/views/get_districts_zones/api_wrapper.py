{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/views/get_districts_zones/api_wrapper.py","undoManager":{"mark":11,"position":11,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from covid_dashboard.views.get_districts_zones.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from covid_dashboard.views.get_districts_zones.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from covid_dashboard.views.get_districts_zones.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"covid_dashboard\", test_case=test_case,","        operation_name=\"get_districts_zones\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from covid_dashboard.interactors.get_stats_interactor import MandalStatsInteractor","from covid_dashboard.presenters.presenter_implementation import PresenterImplementation","from covid_dashboard.storages.user_storage_implementation import StorageImplementation","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = MandalStatsInteractor(","        storage = storage,","        presenter = presenter","    )","","    response = interactor.get_mandal_stats()","","    response_data = json.dumps(response)","    return HttpResponse(response_data, status=200)","    # ---------MOCK IMPLEMENTATION---------","",""],"id":3}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":42},"action":"remove","lines":["get_mandal_stats"],"id":4},{"start":{"row":20,"column":26},"end":{"row":20,"column":45},"action":"insert","lines":["get_districts_zones"]}],[{"start":{"row":6,"column":61},"end":{"row":6,"column":82},"action":"remove","lines":["MandalStatsInteractor"],"id":5},{"start":{"row":6,"column":61},"end":{"row":6,"column":84},"action":"insert","lines":["DistrictZonesInteractor"]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":38},"action":"remove","lines":["MandalStatsInteractor"],"id":6},{"start":{"row":15,"column":17},"end":{"row":15,"column":40},"action":"insert","lines":["DistrictZonesInteractor"]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["r"],"id":8},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["e"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["s"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["u"]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["s"],"id":9},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["t"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["a"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["t"]},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":53},"action":"remove","lines":["get_stats_interactor"],"id":10}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["d"],"id":11}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["d"],"id":12}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["g"],"id":13},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["e"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":36},"action":"remove","lines":["get"],"id":14},{"start":{"row":6,"column":33},"end":{"row":6,"column":51},"action":"insert","lines":["get_district_zones"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":51},"end":{"row":6,"column":51},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":201,"mode":"ace/mode/python"}},"timestamp":1591426131476,"hash":"771a70ce38ed85202087c065e10938fca72ca1b0"}