{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/views/get_state_daily_report/api_wrapper.py","undoManager":{"mark":11,"position":11,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from covid_dashboard.views.get_state_daily_report.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from covid_dashboard.views.get_state_daily_report.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from covid_dashboard.views.get_state_daily_report.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"covid_dashboard\", test_case=test_case,","        operation_name=\"get_state_daily_report\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from covid_dashboard.interactors.get_state_cumulative_report_interactor import StateCumulativeDetailsInteractor","from covid_dashboard.presenters.presenter_implementation import PresenterImplementation","from covid_dashboard.storages.state_storage_implementation import StorageImplementation","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    query_params = kwargs['request_query_params'].__dict__","    date = query_params[\"date\"]","","","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = StateCumulativeDetailsInteractor(","        storage = storage,","        presenter = presenter","    )","","    response = interactor.get_state_cumulative_details(till_date=date)","","    response_data = json.dumps(response)","    return HttpResponse(response_data, status=200)","    # ---------MOCK IMPLEMENTATION---------","",""],"id":3}],[{"start":{"row":6,"column":43},"end":{"row":6,"column":53},"action":"remove","lines":["cumulative"],"id":4}],[{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["d"],"id":5},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":["a"]},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"insert","lines":["i"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"insert","lines":["l"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"insert","lines":["y"]}],[{"start":{"row":6,"column":79},"end":{"row":6,"column":89},"action":"remove","lines":["Cumulative"],"id":6}],[{"start":{"row":6,"column":79},"end":{"row":6,"column":80},"action":"insert","lines":["D"],"id":7},{"start":{"row":6,"column":80},"end":{"row":6,"column":81},"action":"insert","lines":["a"]},{"start":{"row":6,"column":81},"end":{"row":6,"column":82},"action":"insert","lines":["i"]},{"start":{"row":6,"column":82},"end":{"row":6,"column":83},"action":"insert","lines":["l"]},{"start":{"row":6,"column":83},"end":{"row":6,"column":84},"action":"insert","lines":["y"]}],[{"start":{"row":18,"column":17},"end":{"row":18,"column":49},"action":"remove","lines":["StateCumulativeDetailsInteractor"],"id":8},{"start":{"row":18,"column":17},"end":{"row":18,"column":44},"action":"insert","lines":["StateDailyDetailsInteractor"]}],[{"start":{"row":23,"column":36},"end":{"row":23,"column":46},"action":"remove","lines":["cumulative"],"id":14}],[{"start":{"row":23,"column":36},"end":{"row":23,"column":37},"action":"insert","lines":["d"],"id":15},{"start":{"row":23,"column":37},"end":{"row":23,"column":38},"action":"insert","lines":["a"]},{"start":{"row":23,"column":38},"end":{"row":23,"column":39},"action":"insert","lines":["i"]},{"start":{"row":23,"column":39},"end":{"row":23,"column":40},"action":"insert","lines":["l"]},{"start":{"row":23,"column":40},"end":{"row":23,"column":41},"action":"insert","lines":["y"]}],[{"start":{"row":13,"column":31},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":17},{"start":{"row":13,"column":31},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":31},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":18}]]},"ace":{"folds":[],"scrolltop":48,"scrollleft":0,"selection":{"start":{"row":13,"column":31},"end":{"row":13,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":1,"state":"start","mode":"ace/mode/python"}},"timestamp":1591249019356,"hash":"bad96d01359fd82c5e7d58c49fbe92c26aefa99d"}