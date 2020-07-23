{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/views/get_state_daily_report_day_wise/api_wrapper.py","undoManager":{"mark":11,"position":11,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from covid_dashboard.views.get_state_daily_report_day_wise.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from covid_dashboard.views.get_state_daily_report_day_wise.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from covid_dashboard.views.get_state_daily_report_day_wise.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"covid_dashboard\", test_case=test_case,","        operation_name=\"get_state_daily_report_day_wise\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":30,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from covid_dashboard.interactors.get_district_daily_report_day_wise_interactor import DistrictDailyDetailsInteractor","from covid_dashboard.presenters.presenter_implementation import PresenterImplementation","from covid_dashboard.storages.district_storage_implementation import StorageImplementation","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    query_params = kwargs['request_query_params'].__dict__","    district_id = kwargs[\"district_id\"]","    date = query_params[\"date\"]","","","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = DistrictDailyDetailsInteractor(","        storage = storage,","        presenter = presenter","    )","","    response = interactor.get_day_wise_district_daily_details(till_date=date, district_id=district_id)","","    response_data = json.dumps(response)","    return HttpResponse(response_data, status=200)","    # ---------MOCK IMPLEMENTATION---------","",""]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":45},"action":"remove","lines":["district"],"id":3}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["s"],"id":4},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["t"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["a"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["t"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":83},"end":{"row":6,"column":91},"action":"remove","lines":["District"],"id":5}],[{"start":{"row":6,"column":83},"end":{"row":6,"column":84},"action":"insert","lines":["S"],"id":6},{"start":{"row":6,"column":84},"end":{"row":6,"column":85},"action":"insert","lines":["t"]},{"start":{"row":6,"column":85},"end":{"row":6,"column":86},"action":"insert","lines":["a"]},{"start":{"row":6,"column":86},"end":{"row":6,"column":87},"action":"insert","lines":["t"]},{"start":{"row":6,"column":87},"end":{"row":6,"column":88},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":39},"action":"remove","lines":["    district_id = kwargs[\"district_id\"]"],"id":7},{"start":{"row":12,"column":58},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":17},"end":{"row":18,"column":47},"action":"remove","lines":["DistrictDailyDetailsInteractor"],"id":8},{"start":{"row":18,"column":17},"end":{"row":18,"column":44},"action":"insert","lines":["StateDailyDetailsInteractor"]}],[{"start":{"row":23,"column":39},"end":{"row":23,"column":47},"action":"remove","lines":["district"],"id":9}],[{"start":{"row":23,"column":39},"end":{"row":23,"column":40},"action":"insert","lines":["s"],"id":10},{"start":{"row":23,"column":40},"end":{"row":23,"column":41},"action":"insert","lines":["t"]},{"start":{"row":23,"column":41},"end":{"row":23,"column":42},"action":"insert","lines":["a"]},{"start":{"row":23,"column":42},"end":{"row":23,"column":43},"action":"insert","lines":["t"]},{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"insert","lines":["e"]}],[{"start":{"row":23,"column":74},"end":{"row":23,"column":98},"action":"remove","lines":[" district_id=district_id"],"id":11},{"start":{"row":23,"column":73},"end":{"row":23,"column":74},"action":"remove","lines":[","]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":38},"action":"remove","lines":["district"],"id":12}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["s"],"id":13},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["t"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["a"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["t"]},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":9,"scrollleft":0,"selection":{"start":{"row":15,"column":0},"end":{"row":15,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591340535202,"hash":"37f3f71795c1617bf32cd4a2d6b1529da55763b4"}