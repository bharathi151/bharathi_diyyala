{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/views/get_mandal_stats/api_wrapper.py","undoManager":{"mark":11,"position":11,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from covid_dashboard.views.get_mandal_stats.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from covid_dashboard.views.get_mandal_stats.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from covid_dashboard.views.get_mandal_stats.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"covid_dashboard\", test_case=test_case,","        operation_name=\"get_mandal_stats\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from covid_dashboard.interactors.get_state_cumulative_report_day_wise_interactor import StateCumulativeDetailsInteractor","from covid_dashboard.presenters.presenter_implementation import PresenterImplementation","from covid_dashboard.storages.state_storage_implementation import StorageImplementation","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = StateCumulativeDetailsInteractor(","        storage = storage,","        presenter = presenter","    )","","    response = interactor.get_day_wise_state_cumulative_details()","","    response_data = json.dumps(response)","    return HttpResponse(response_data, status=200)","    # ---------MOCK IMPLEMENTATION---------","",""],"id":3}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":80},"action":"remove","lines":["get_state_cumulative_report_day_wise_interactor"],"id":4}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["g"],"id":5},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["e"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["t"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["_"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["s"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["a"],"id":6},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["t"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":42},"action":"remove","lines":["get_stats"],"id":7},{"start":{"row":6,"column":33},"end":{"row":6,"column":53},"action":"insert","lines":["get_stats_interactor"]}],[{"start":{"row":6,"column":61},"end":{"row":6,"column":93},"action":"remove","lines":["StateCumulativeDetailsInteractor"],"id":8}],[{"start":{"row":6,"column":61},"end":{"row":6,"column":82},"action":"insert","lines":["MandalStatsInteractor"],"id":9}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"remove","lines":["e"],"id":10},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["t"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["a"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["t"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["s"]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["u"],"id":11},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["s"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["e"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":49},"action":"remove","lines":["StateCumulativeDetailsInteractor"],"id":12},{"start":{"row":15,"column":17},"end":{"row":15,"column":38},"action":"insert","lines":["MandalStatsInteractor"]}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":63},"action":"remove","lines":["get_day_wise_state_cumulative_details"],"id":13},{"start":{"row":20,"column":26},"end":{"row":20,"column":42},"action":"insert","lines":["get_mandal_stats"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":33},"end":{"row":11,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591416300260,"hash":"2daa904fc22648c5fdca6cf16cd28a98857258b2"}