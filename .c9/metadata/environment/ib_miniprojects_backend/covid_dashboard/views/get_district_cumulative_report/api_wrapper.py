{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/views/get_district_cumulative_report/api_wrapper.py","undoManager":{"mark":29,"position":29,"stack":[[{"start":{"row":7,"column":4},"end":{"row":28,"column":28},"action":"remove","lines":["# ---------MOCK IMPLEMENTATION---------","","    try:","        from covid_dashboard.views.get_district_cumulative_report.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from covid_dashboard.views.get_district_cumulative_report.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from covid_dashboard.views.get_district_cumulative_report.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"covid_dashboard\", test_case=test_case,","        operation_name=\"get_district_cumulative_report\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    "],"id":3},{"start":{"row":0,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["import json","","from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from covid_dashboard.interactors.get_state_cumulative_report_interactor import StateCumulativeDetailsInteractor","from covid_dashboard.presenters.presenter_implementation import PresenterImplementation","from covid_dashboard.storages.state_storage_implementation import StorageImplementation","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    query_params = kwargs['request_query_params'].__dict__","    date = query_params[\"date\"]","","","    storage = StorageImplementation()","    presenter = PresenterImplementation()","    interactor = StateCumulativeDetailsInteractor(","        storage = storage,","        presenter = presenter","    )","","    response = interactor.get_state_cumulative_details(till_date=date)","","    response_data = json.dumps(response)","    return HttpResponse(response_data, status=200)","    # ---------MOCK IMPLEMENTATION---------","",""]}],[{"start":{"row":12,"column":58},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["d"],"id":5},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["i"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":7},"action":"remove","lines":["dis"],"id":6},{"start":{"row":13,"column":4},"end":{"row":13,"column":12},"action":"insert","lines":["district"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["_"],"id":7},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["i"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":[" "],"id":8},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":[" "],"id":9},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["k"]}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["k"],"id":10},{"start":{"row":13,"column":18},"end":{"row":13,"column":24},"action":"insert","lines":["kwargs"]}],[{"start":{"row":13,"column":24},"end":{"row":13,"column":26},"action":"insert","lines":["[]"],"id":11}],[{"start":{"row":13,"column":25},"end":{"row":13,"column":27},"action":"insert","lines":["\"\""],"id":12}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["d"],"id":13}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["d"],"id":14},{"start":{"row":13,"column":26},"end":{"row":13,"column":37},"action":"insert","lines":["district_id"]}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"remove","lines":["e"],"id":15},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["t"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["a"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["t"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["s"]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["d"],"id":16},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["i"]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":55},"action":"remove","lines":["di_storage_implementation"],"id":17},{"start":{"row":8,"column":30},"end":{"row":8,"column":61},"action":"insert","lines":["district_storage_implementation"]}],[{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["e"],"id":18},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["t"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["a"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["t"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["s"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["d"],"id":19},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["i"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["t"],"id":20},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["r"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":["i"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["c"]},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":86},"end":{"row":6,"column":87},"action":"remove","lines":["e"],"id":21},{"start":{"row":6,"column":85},"end":{"row":6,"column":86},"action":"remove","lines":["t"]},{"start":{"row":6,"column":84},"end":{"row":6,"column":85},"action":"remove","lines":["a"]},{"start":{"row":6,"column":83},"end":{"row":6,"column":84},"action":"remove","lines":["t"]},{"start":{"row":6,"column":82},"end":{"row":6,"column":83},"action":"remove","lines":["S"]}],[{"start":{"row":6,"column":82},"end":{"row":6,"column":83},"action":"insert","lines":["D"],"id":22}],[{"start":{"row":6,"column":82},"end":{"row":6,"column":110},"action":"remove","lines":["DCumulativeDetailsInteractor"],"id":23},{"start":{"row":6,"column":82},"end":{"row":6,"column":117},"action":"insert","lines":["DistrictCumulativeDetailsInteractor"]}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":49},"action":"remove","lines":["StateCumulativeDetailsInteractor"],"id":24},{"start":{"row":19,"column":17},"end":{"row":19,"column":52},"action":"insert","lines":["DistrictCumulativeDetailsInteractor"]}],[{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"remove","lines":["e"],"id":25},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"remove","lines":["t"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"remove","lines":["a"]},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"remove","lines":["t"]},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"remove","lines":["s"]}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["d"],"id":26},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["i"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["s"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["t"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["r"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["i"]},{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"insert","lines":["c"]},{"start":{"row":24,"column":37},"end":{"row":24,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":24,"column":72},"end":{"row":24,"column":73},"action":"insert","lines":[","],"id":27}],[{"start":{"row":24,"column":73},"end":{"row":24,"column":74},"action":"insert","lines":[" "],"id":28},{"start":{"row":24,"column":74},"end":{"row":24,"column":75},"action":"insert","lines":["d"]},{"start":{"row":24,"column":75},"end":{"row":24,"column":76},"action":"insert","lines":["i"]}],[{"start":{"row":24,"column":74},"end":{"row":24,"column":76},"action":"remove","lines":["di"],"id":29},{"start":{"row":24,"column":74},"end":{"row":24,"column":85},"action":"insert","lines":["district_id"]}],[{"start":{"row":24,"column":85},"end":{"row":24,"column":86},"action":"insert","lines":["="],"id":30},{"start":{"row":24,"column":86},"end":{"row":24,"column":87},"action":"insert","lines":["d"]},{"start":{"row":24,"column":87},"end":{"row":24,"column":88},"action":"insert","lines":["i"]},{"start":{"row":24,"column":88},"end":{"row":24,"column":89},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":86},"end":{"row":24,"column":89},"action":"remove","lines":["dis"],"id":31},{"start":{"row":24,"column":86},"end":{"row":24,"column":97},"action":"insert","lines":["district_id"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":26},"end":{"row":20,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591095595804,"hash":"17a73905501837831cb19aa05758b24cc35aa9a7"}