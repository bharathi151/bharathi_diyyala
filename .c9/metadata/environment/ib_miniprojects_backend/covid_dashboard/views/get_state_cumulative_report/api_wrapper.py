{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/views/get_state_cumulative_report/api_wrapper.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from covid_dashboard.views.get_state_cumulative_report.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from covid_dashboard.views.get_state_cumulative_report.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from covid_dashboard.views.get_state_cumulative_report.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"covid_dashboard\", test_case=test_case,","        operation_name=\"get_state_cumulative_report\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from covid_dashboard.interactors.get_state_cumulative_report_interactor import StateCumulativeDetailsInteractor","from covid_dashboard.presenters.presenter_implementation import PresenterImplementation","from covid_dashboard.storages.state_storage_implementation import StorageImplementation","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    query_params = kwargs['request_query_params'].__dict__","    date = query_params[\"date\"]","","","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = StateCumulativeDetailsInteractor(","        storage = storage,","        presenter = presenter","    )","","    response = interactor.get_state_cumulative_details(till_date=date)","","    response_data = json.dumps(response)","    return HttpResponse(response_data, status=200)","    # ---------MOCK IMPLEMENTATION---------","",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":37},"end":{"row":16,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591072566685,"hash":"dd8bf156e22e8b9969bbc9b16a314c908dc71ca2"}