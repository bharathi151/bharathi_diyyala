{"filter":false,"title":"test_update_case_details.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/tests/storages/test_update_case_details.py","undoManager":{"mark":37,"position":37,"stack":[[{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"remove","lines":["t"],"id":2},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"remove","lines":["s"]},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"remove","lines":["o"]},{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"remove","lines":["p"]}],[{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["i"],"id":3},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"insert","lines":["p"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["d"]},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"insert","lines":["a"]},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["t"]},{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"remove","lines":["e"],"id":4},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"remove","lines":["t"]},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"remove","lines":["a"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"remove","lines":["d"]},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"remove","lines":["p"]},{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"remove","lines":["i"]}],[{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["u"],"id":5},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"insert","lines":["p"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["d"]},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"insert","lines":["a"]},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["t"]},{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"remove","lines":["a"],"id":6}],[{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":["a"],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":8},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"insert","lines":["# "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["# "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":2},"action":"insert","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":0,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["# import pytest","","# from covid_dashboard.models import CasesDetails","# from covid_dashboard.storages.user_storage_implementation import StorageImplementation","","","# @pytest.mark.django_db","# def test_post_cases_interactor_given_valid_details_creates_comment(","#         create_users,","#         create_post):","#     mandal_id=1,","#     confirmed_cases=2,","#     deaths=0,","#     recovered_cases=1","#     sql_storage = StorageImplementation()","","#     cases_details_id = sql_storage.update_cases_details(","#         mandal_id=mandal_id,","#         confirmed_cases=confirmed_cases,","#         deaths=deaths,","#         recovered_cases=recovered_cases)","","#     cases_details = CasesDetails.objects.get(id=cases_details_id)","#     assert cases_details.id == cases_details_id","#     assert cases_details.recovered_cases == recovered_cases","#     assert cases_details.confirmed_cases == confirmed_cases","#     assert cases_details.deaths == deaths","#     assert cases_details.mandal_id == mandal_id",""],"id":9}],[{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["import pytest","import datetime","","from covid_dashboard.models import CasesDetails","from covid_dashboard.storages.user_storage_implementation import StorageImplementation","","","@pytest.mark.django_db","def test_post_cases_given_valid_details_posts_cases(create_mandals):","    mandal_id=1","    confirmed_cases=2","    deaths=0","    recovered_cases=1","    date = datetime.date(2020,5,30)","    sql_storage = StorageImplementation()","","    cases_details_id = sql_storage.post_cases_details(","        mandal_id=mandal_id,","        date=date,","        confirmed_cases=confirmed_cases,","        ","        deaths=deaths,","        recovered_cases=recovered_cases)","","    cases_details = CasesDetails.objects.get(id=cases_details_id)","    assert cases_details.id == cases_details_id","    assert cases_details.date == date","    assert cases_details.recovered_cases == recovered_cases","    assert cases_details.confirmed_cases == confirmed_cases","    assert cases_details.deaths == deaths","    assert cases_details.mandal_id == mandal_id",""],"id":10}],[{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"remove","lines":["t"],"id":11},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"remove","lines":["s"]},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"remove","lines":["o"]},{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"remove","lines":["p"]}],[{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["u"],"id":12},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"insert","lines":["p"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["d"]},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"insert","lines":["a"]},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["t"]},{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":66},"end":{"row":8,"column":67},"action":"insert","lines":[","],"id":13}],[{"start":{"row":8,"column":67},"end":{"row":8,"column":83},"action":"insert","lines":["cases_for_update"],"id":14}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":67},"action":"remove","lines":["create_mandals,"],"id":15}],[{"start":{"row":16,"column":5},"end":{"row":16,"column":23},"action":"remove","lines":["ases_details_id = "],"id":16}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["    assert cases_details.id == cases_details_id",""],"id":17}],[{"start":{"row":24,"column":48},"end":{"row":24,"column":64},"action":"remove","lines":["cases_details_id"],"id":18},{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"remove","lines":["="]},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"remove","lines":["d"]},{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"remove","lines":["i"]}],[{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":["d"],"id":19},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":["a"]},{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"insert","lines":["t"]},{"start":{"row":24,"column":48},"end":{"row":24,"column":49},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":45},"end":{"row":24,"column":49},"action":"remove","lines":["date"],"id":20},{"start":{"row":24,"column":45},"end":{"row":24,"column":49},"action":"insert","lines":["date"]}],[{"start":{"row":24,"column":49},"end":{"row":24,"column":50},"action":"insert","lines":["="],"id":21},{"start":{"row":24,"column":50},"end":{"row":24,"column":51},"action":"insert","lines":["d"]},{"start":{"row":24,"column":51},"end":{"row":24,"column":52},"action":"insert","lines":["a"]},{"start":{"row":24,"column":52},"end":{"row":24,"column":53},"action":"insert","lines":["t"]}],[{"start":{"row":24,"column":53},"end":{"row":24,"column":54},"action":"insert","lines":["e"],"id":22},{"start":{"row":24,"column":54},"end":{"row":24,"column":55},"action":"insert","lines":[","]}],[{"start":{"row":24,"column":55},"end":{"row":24,"column":56},"action":"insert","lines":[" "],"id":23},{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"insert","lines":["m"]},{"start":{"row":24,"column":57},"end":{"row":24,"column":58},"action":"insert","lines":["a"]},{"start":{"row":24,"column":58},"end":{"row":24,"column":59},"action":"insert","lines":["n"]},{"start":{"row":24,"column":59},"end":{"row":24,"column":60},"action":"insert","lines":["d"]},{"start":{"row":24,"column":60},"end":{"row":24,"column":61},"action":"insert","lines":["a"]},{"start":{"row":24,"column":61},"end":{"row":24,"column":62},"action":"insert","lines":["l"]}],[{"start":{"row":24,"column":56},"end":{"row":24,"column":62},"action":"remove","lines":["mandal"],"id":24},{"start":{"row":24,"column":56},"end":{"row":24,"column":65},"action":"insert","lines":["mandal_id"]}],[{"start":{"row":24,"column":65},"end":{"row":24,"column":66},"action":"insert","lines":["="],"id":25},{"start":{"row":24,"column":66},"end":{"row":24,"column":67},"action":"insert","lines":["m"]},{"start":{"row":24,"column":67},"end":{"row":24,"column":68},"action":"insert","lines":["a"]}],[{"start":{"row":24,"column":66},"end":{"row":24,"column":68},"action":"remove","lines":["ma"],"id":26},{"start":{"row":24,"column":66},"end":{"row":24,"column":75},"action":"insert","lines":["mandal_id"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"remove","lines":["c"],"id":27}],[{"start":{"row":24,"column":4},"end":{"row":29,"column":47},"action":"remove","lines":["cases_details = CasesDetails.objects.get(date=date, mandal_id=mandal_id)","    assert cases_details.date == date","    assert cases_details.recovered_cases == recovered_cases","    assert cases_details.confirmed_cases == confirmed_cases","    assert cases_details.deaths == deaths","    assert cases_details.mandal_id == mandal_id"],"id":28}],[{"start":{"row":16,"column":4},"end":{"row":24,"column":4},"action":"remove","lines":["sql_storage.update_cases_details(","        mandal_id=mandal_id,","        date=date,","        confirmed_cases=confirmed_cases,","        ","        deaths=deaths,","        recovered_cases=recovered_cases)","","    "],"id":29}],[{"start":{"row":16,"column":4},"end":{"row":29,"column":43},"action":"insert","lines":["stats_dto = sql_storage.post_cases_details(","        mandal_id=mandal_id,","        date=date,","        confirmed_cases=confirmed_cases,","        ","        deaths=deaths,","        recovered_cases=recovered_cases)","","","    assert stats_dto.date == date","    assert stats_dto.total_recovered_cases == recovered_cases","    assert stats_dto.total_confirmed_cases == confirmed_cases","    assert stats_dto.total_deaths == deaths","    assert stats_dto.mandal_id == mandal_id"],"id":30}],[{"start":{"row":16,"column":31},"end":{"row":16,"column":32},"action":"remove","lines":["t"],"id":31},{"start":{"row":16,"column":30},"end":{"row":16,"column":31},"action":"remove","lines":["s"]},{"start":{"row":16,"column":29},"end":{"row":16,"column":30},"action":"remove","lines":["o"]},{"start":{"row":16,"column":28},"end":{"row":16,"column":29},"action":"remove","lines":["p"]}],[{"start":{"row":16,"column":28},"end":{"row":16,"column":29},"action":"insert","lines":["u"],"id":32},{"start":{"row":16,"column":29},"end":{"row":16,"column":30},"action":"insert","lines":["p"]},{"start":{"row":16,"column":30},"end":{"row":16,"column":31},"action":"insert","lines":["d"]},{"start":{"row":16,"column":31},"end":{"row":16,"column":32},"action":"insert","lines":["a"]},{"start":{"row":16,"column":32},"end":{"row":16,"column":33},"action":"insert","lines":["t"]},{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"insert","lines":["e"]},{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"insert","lines":["w"]}],[{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"remove","lines":["w"],"id":33}],[{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"remove","lines":["s"],"id":34},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":["t"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"remove","lines":["s"]},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"remove","lines":["o"]},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["u"],"id":35},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["p"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["d"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["a"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["t"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["e"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["t"],"id":36},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["s"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["o"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["u"],"id":37},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["p"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["d"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["a"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["t"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":["."],"id":38}],[{"start":{"row":25,"column":34},"end":{"row":25,"column":54},"action":"insert","lines":["strftime(\"%d/%m/%Y\")"],"id":39}]]},"ace":{"folds":[],"scrolltop":54.5,"scrollleft":0,"selection":{"start":{"row":25,"column":54},"end":{"row":25,"column":54},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":1,"state":"start","mode":"ace/mode/python"}},"timestamp":1592579284624,"hash":"0f83db66eb0a913c3b7319f4faedff8f81458e82"}