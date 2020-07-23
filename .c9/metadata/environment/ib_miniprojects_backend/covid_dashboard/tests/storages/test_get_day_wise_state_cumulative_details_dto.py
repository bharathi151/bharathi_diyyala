{"filter":false,"title":"test_get_day_wise_state_cumulative_details_dto.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/tests/storages/test_get_day_wise_state_cumulative_details_dto.py","undoManager":{"mark":62,"position":62,"stack":[[{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"remove","lines":["5"],"id":100}],[{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["1"],"id":101}],[{"start":{"row":9,"column":81},"end":{"row":9,"column":91},"action":"remove","lines":["post_cases"],"id":102}],[{"start":{"row":9,"column":81},"end":{"row":9,"column":82},"action":"insert","lines":["c"],"id":103},{"start":{"row":9,"column":82},"end":{"row":9,"column":83},"action":"insert","lines":["o"]},{"start":{"row":9,"column":83},"end":{"row":9,"column":84},"action":"insert","lines":["n"]},{"start":{"row":9,"column":84},"end":{"row":9,"column":85},"action":"insert","lines":["t"]},{"start":{"row":9,"column":85},"end":{"row":9,"column":86},"action":"insert","lines":["i"]}],[{"start":{"row":9,"column":86},"end":{"row":9,"column":87},"action":"insert","lines":["n"],"id":104},{"start":{"row":9,"column":87},"end":{"row":9,"column":88},"action":"insert","lines":["u"]},{"start":{"row":9,"column":88},"end":{"row":9,"column":89},"action":"insert","lines":["e"]},{"start":{"row":9,"column":89},"end":{"row":9,"column":90},"action":"insert","lines":["d"]}],[{"start":{"row":9,"column":90},"end":{"row":9,"column":91},"action":"insert","lines":["_"],"id":105},{"start":{"row":9,"column":91},"end":{"row":9,"column":92},"action":"insert","lines":["d"]},{"start":{"row":9,"column":92},"end":{"row":9,"column":93},"action":"insert","lines":["a"]},{"start":{"row":9,"column":93},"end":{"row":9,"column":94},"action":"insert","lines":["i"]},{"start":{"row":9,"column":94},"end":{"row":9,"column":95},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":95},"end":{"row":9,"column":96},"action":"insert","lines":["y"],"id":106}],[{"start":{"row":9,"column":95},"end":{"row":9,"column":96},"action":"remove","lines":["y"],"id":107},{"start":{"row":9,"column":94},"end":{"row":9,"column":95},"action":"remove","lines":["l"]},{"start":{"row":9,"column":93},"end":{"row":9,"column":94},"action":"remove","lines":["i"]},{"start":{"row":9,"column":92},"end":{"row":9,"column":93},"action":"remove","lines":["a"]},{"start":{"row":9,"column":91},"end":{"row":9,"column":92},"action":"remove","lines":["d"]},{"start":{"row":9,"column":90},"end":{"row":9,"column":91},"action":"remove","lines":["_"]},{"start":{"row":9,"column":89},"end":{"row":9,"column":90},"action":"remove","lines":["d"]},{"start":{"row":9,"column":88},"end":{"row":9,"column":89},"action":"remove","lines":["e"]},{"start":{"row":9,"column":87},"end":{"row":9,"column":88},"action":"remove","lines":["u"]},{"start":{"row":9,"column":86},"end":{"row":9,"column":87},"action":"remove","lines":["n"]},{"start":{"row":9,"column":85},"end":{"row":9,"column":86},"action":"remove","lines":["i"]},{"start":{"row":9,"column":84},"end":{"row":9,"column":85},"action":"remove","lines":["t"]},{"start":{"row":9,"column":83},"end":{"row":9,"column":84},"action":"remove","lines":["n"]},{"start":{"row":9,"column":82},"end":{"row":9,"column":83},"action":"remove","lines":["o"]},{"start":{"row":9,"column":81},"end":{"row":9,"column":82},"action":"remove","lines":["c"]}],[{"start":{"row":9,"column":81},"end":{"row":9,"column":82},"action":"insert","lines":["d"],"id":108},{"start":{"row":9,"column":82},"end":{"row":9,"column":83},"action":"insert","lines":["a"]},{"start":{"row":9,"column":83},"end":{"row":9,"column":84},"action":"insert","lines":["i"]},{"start":{"row":9,"column":84},"end":{"row":9,"column":85},"action":"insert","lines":["l"]},{"start":{"row":9,"column":85},"end":{"row":9,"column":86},"action":"insert","lines":["y"]}],[{"start":{"row":9,"column":86},"end":{"row":9,"column":87},"action":"insert","lines":["_"],"id":109},{"start":{"row":9,"column":87},"end":{"row":9,"column":88},"action":"insert","lines":["c"]},{"start":{"row":9,"column":88},"end":{"row":9,"column":89},"action":"insert","lines":["a"]},{"start":{"row":9,"column":89},"end":{"row":9,"column":90},"action":"insert","lines":["s"]},{"start":{"row":9,"column":90},"end":{"row":9,"column":91},"action":"insert","lines":["e"]},{"start":{"row":9,"column":91},"end":{"row":9,"column":92},"action":"insert","lines":["s"]}],[{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":110}],[{"start":{"row":36,"column":0},"end":{"row":63,"column":0},"action":"insert","lines":["@pytest.mark.django_db","def test_get_day_wise_state_cumulative_details_dto_returns_state_total_cases_dto(daily_cases):","","    day_wise_statistics = [","           DayWiseStateTotalCasesDto(","               date=\"20/05/2020\",","               total_confirmed_cases=10,","               total_recovered_cases=2,","               total_deaths=1,","            ),","            DayWiseStateTotalCasesDto(","               date=\"21/05/2020\",","               total_confirmed_cases=20,","               total_recovered_cases=4,","               total_deaths=2,","            )","        ]","","    expected_output = DayWiseStateTotalCasesDtos(","               state_name=\"AndhraPradesh\",","               day_wise_statistics=day_wise_statistics","        )","    sql_storage = StorageImplementation()","","    state_total_cases_dto = sql_storage.get_day_wise_state_cumulative_dto()","","    assert expected_output == state_total_cases_dto",""],"id":111}],[{"start":{"row":37,"column":51},"end":{"row":37,"column":52},"action":"insert","lines":["w"],"id":112},{"start":{"row":37,"column":52},"end":{"row":37,"column":53},"action":"insert","lines":["h"]},{"start":{"row":37,"column":53},"end":{"row":37,"column":54},"action":"insert","lines":["e"]},{"start":{"row":37,"column":54},"end":{"row":37,"column":55},"action":"insert","lines":["n"]},{"start":{"row":37,"column":55},"end":{"row":37,"column":56},"action":"insert","lines":["_"]}],[{"start":{"row":37,"column":56},"end":{"row":37,"column":57},"action":"insert","lines":["t"],"id":113},{"start":{"row":37,"column":57},"end":{"row":37,"column":58},"action":"insert","lines":["h"]},{"start":{"row":37,"column":58},"end":{"row":37,"column":59},"action":"insert","lines":["e"]},{"start":{"row":37,"column":59},"end":{"row":37,"column":60},"action":"insert","lines":["r"]},{"start":{"row":37,"column":60},"end":{"row":37,"column":61},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":61},"end":{"row":37,"column":62},"action":"insert","lines":["_"],"id":114},{"start":{"row":37,"column":62},"end":{"row":37,"column":63},"action":"insert","lines":["i"]},{"start":{"row":37,"column":63},"end":{"row":37,"column":64},"action":"insert","lines":["s"]},{"start":{"row":37,"column":64},"end":{"row":37,"column":65},"action":"insert","lines":["_"]}],[{"start":{"row":37,"column":65},"end":{"row":37,"column":66},"action":"insert","lines":["n"],"id":115},{"start":{"row":37,"column":66},"end":{"row":37,"column":67},"action":"insert","lines":["o"]},{"start":{"row":37,"column":67},"end":{"row":37,"column":68},"action":"insert","lines":["_"]},{"start":{"row":37,"column":68},"end":{"row":37,"column":69},"action":"insert","lines":["C"]}],[{"start":{"row":37,"column":69},"end":{"row":37,"column":70},"action":"insert","lines":["A"],"id":116},{"start":{"row":37,"column":70},"end":{"row":37,"column":71},"action":"insert","lines":["s"]},{"start":{"row":37,"column":71},"end":{"row":37,"column":72},"action":"insert","lines":["e"]},{"start":{"row":37,"column":72},"end":{"row":37,"column":73},"action":"insert","lines":["s"]}],[{"start":{"row":37,"column":72},"end":{"row":37,"column":73},"action":"remove","lines":["s"],"id":117},{"start":{"row":37,"column":71},"end":{"row":37,"column":72},"action":"remove","lines":["e"]},{"start":{"row":37,"column":70},"end":{"row":37,"column":71},"action":"remove","lines":["s"]},{"start":{"row":37,"column":69},"end":{"row":37,"column":70},"action":"remove","lines":["A"]},{"start":{"row":37,"column":68},"end":{"row":37,"column":69},"action":"remove","lines":["C"]}],[{"start":{"row":37,"column":68},"end":{"row":37,"column":69},"action":"insert","lines":["c"],"id":118},{"start":{"row":37,"column":69},"end":{"row":37,"column":70},"action":"insert","lines":["a"]},{"start":{"row":37,"column":70},"end":{"row":37,"column":71},"action":"insert","lines":["s"]},{"start":{"row":37,"column":71},"end":{"row":37,"column":72},"action":"insert","lines":["e"]},{"start":{"row":37,"column":72},"end":{"row":37,"column":73},"action":"insert","lines":["_"]},{"start":{"row":37,"column":73},"end":{"row":37,"column":74},"action":"insert","lines":["b"]}],[{"start":{"row":37,"column":74},"end":{"row":37,"column":75},"action":"insert","lines":["w"],"id":119},{"start":{"row":37,"column":75},"end":{"row":37,"column":76},"action":"insert","lines":["t"]},{"start":{"row":37,"column":76},"end":{"row":37,"column":77},"action":"insert","lines":["w"]},{"start":{"row":37,"column":77},"end":{"row":37,"column":78},"action":"insert","lines":["e"]},{"start":{"row":37,"column":78},"end":{"row":37,"column":79},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":79},"end":{"row":37,"column":80},"action":"insert","lines":["n"],"id":120},{"start":{"row":37,"column":80},"end":{"row":37,"column":81},"action":"insert","lines":["_"]}],[{"start":{"row":37,"column":81},"end":{"row":37,"column":82},"action":"insert","lines":["t"],"id":121},{"start":{"row":37,"column":82},"end":{"row":37,"column":83},"action":"insert","lines":["w"]},{"start":{"row":37,"column":83},"end":{"row":37,"column":84},"action":"insert","lines":["o"]},{"start":{"row":37,"column":84},"end":{"row":37,"column":85},"action":"insert","lines":["_"]},{"start":{"row":37,"column":85},"end":{"row":37,"column":86},"action":"insert","lines":["d"]}],[{"start":{"row":37,"column":86},"end":{"row":37,"column":87},"action":"insert","lines":["a"],"id":122},{"start":{"row":37,"column":87},"end":{"row":37,"column":88},"action":"insert","lines":["t"]},{"start":{"row":37,"column":88},"end":{"row":37,"column":89},"action":"insert","lines":["e"]},{"start":{"row":37,"column":89},"end":{"row":37,"column":90},"action":"insert","lines":["s"]}],[{"start":{"row":37,"column":90},"end":{"row":37,"column":91},"action":"insert","lines":["_"],"id":123}],[{"start":{"row":37,"column":83},"end":{"row":37,"column":84},"action":"remove","lines":["o"],"id":124},{"start":{"row":37,"column":82},"end":{"row":37,"column":83},"action":"remove","lines":["w"]},{"start":{"row":37,"column":81},"end":{"row":37,"column":82},"action":"remove","lines":["t"]},{"start":{"row":37,"column":80},"end":{"row":37,"column":81},"action":"remove","lines":["_"]},{"start":{"row":37,"column":79},"end":{"row":37,"column":80},"action":"remove","lines":["n"]},{"start":{"row":37,"column":78},"end":{"row":37,"column":79},"action":"remove","lines":["e"]},{"start":{"row":37,"column":77},"end":{"row":37,"column":78},"action":"remove","lines":["e"]},{"start":{"row":37,"column":76},"end":{"row":37,"column":77},"action":"remove","lines":["w"]},{"start":{"row":37,"column":75},"end":{"row":37,"column":76},"action":"remove","lines":["t"]},{"start":{"row":37,"column":74},"end":{"row":37,"column":75},"action":"remove","lines":["w"]},{"start":{"row":37,"column":73},"end":{"row":37,"column":74},"action":"remove","lines":["b"]}],[{"start":{"row":37,"column":73},"end":{"row":37,"column":74},"action":"insert","lines":["f"],"id":125},{"start":{"row":37,"column":74},"end":{"row":37,"column":75},"action":"insert","lines":["o"]},{"start":{"row":37,"column":75},"end":{"row":37,"column":76},"action":"insert","lines":["r"]}],[{"start":{"row":37,"column":112},"end":{"row":37,"column":113},"action":"insert","lines":["_"],"id":126},{"start":{"row":37,"column":113},"end":{"row":37,"column":114},"action":"insert","lines":["w"]},{"start":{"row":37,"column":114},"end":{"row":37,"column":115},"action":"insert","lines":["i"]},{"start":{"row":37,"column":115},"end":{"row":37,"column":116},"action":"insert","lines":["t"]},{"start":{"row":37,"column":116},"end":{"row":37,"column":117},"action":"insert","lines":["h"]},{"start":{"row":37,"column":117},"end":{"row":37,"column":118},"action":"insert","lines":["_"]}],[{"start":{"row":37,"column":118},"end":{"row":37,"column":119},"action":"insert","lines":["r"],"id":127},{"start":{"row":37,"column":119},"end":{"row":37,"column":120},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":120},"end":{"row":37,"column":121},"action":"insert","lines":["t"],"id":128}],[{"start":{"row":37,"column":120},"end":{"row":37,"column":121},"action":"remove","lines":["t"],"id":129},{"start":{"row":37,"column":119},"end":{"row":37,"column":120},"action":"remove","lines":["e"]},{"start":{"row":37,"column":118},"end":{"row":37,"column":119},"action":"remove","lines":["r"]}],[{"start":{"row":37,"column":118},"end":{"row":37,"column":119},"action":"insert","lines":["p"],"id":130},{"start":{"row":37,"column":119},"end":{"row":37,"column":120},"action":"insert","lines":["r"]},{"start":{"row":37,"column":120},"end":{"row":37,"column":121},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":121},"end":{"row":37,"column":122},"action":"insert","lines":["v"],"id":131},{"start":{"row":37,"column":122},"end":{"row":37,"column":123},"action":"insert","lines":["i"]},{"start":{"row":37,"column":123},"end":{"row":37,"column":124},"action":"insert","lines":["o"]},{"start":{"row":37,"column":124},"end":{"row":37,"column":125},"action":"insert","lines":["u"]},{"start":{"row":37,"column":125},"end":{"row":37,"column":126},"action":"insert","lines":["s"]},{"start":{"row":37,"column":126},"end":{"row":37,"column":127},"action":"insert","lines":["_"]}],[{"start":{"row":37,"column":127},"end":{"row":37,"column":128},"action":"insert","lines":["d"],"id":132},{"start":{"row":37,"column":128},"end":{"row":37,"column":129},"action":"insert","lines":["a"]},{"start":{"row":37,"column":129},"end":{"row":37,"column":130},"action":"insert","lines":["t"]},{"start":{"row":37,"column":130},"end":{"row":37,"column":131},"action":"insert","lines":["a"]}],[{"start":{"row":37,"column":131},"end":{"row":37,"column":132},"action":"insert","lines":["_"],"id":133},{"start":{"row":37,"column":132},"end":{"row":37,"column":133},"action":"insert","lines":["f"]},{"start":{"row":37,"column":133},"end":{"row":37,"column":134},"action":"insert","lines":["o"]},{"start":{"row":37,"column":134},"end":{"row":37,"column":135},"action":"insert","lines":["r"]},{"start":{"row":37,"column":135},"end":{"row":37,"column":136},"action":"insert","lines":["_"]},{"start":{"row":37,"column":136},"end":{"row":37,"column":137},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":137},"end":{"row":37,"column":138},"action":"insert","lines":["h"],"id":134},{"start":{"row":37,"column":138},"end":{"row":37,"column":139},"action":"insert","lines":["o"]},{"start":{"row":37,"column":139},"end":{"row":37,"column":140},"action":"insert","lines":["s"]},{"start":{"row":37,"column":140},"end":{"row":37,"column":141},"action":"insert","lines":["e"]},{"start":{"row":37,"column":141},"end":{"row":37,"column":142},"action":"insert","lines":["_"]}],[{"start":{"row":37,"column":142},"end":{"row":37,"column":143},"action":"insert","lines":["d"],"id":135},{"start":{"row":37,"column":143},"end":{"row":37,"column":144},"action":"insert","lines":["a"]},{"start":{"row":37,"column":144},"end":{"row":37,"column":145},"action":"insert","lines":["t"]},{"start":{"row":37,"column":145},"end":{"row":37,"column":146},"action":"insert","lines":["e"]},{"start":{"row":37,"column":146},"end":{"row":37,"column":147},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"remove","lines":["1"],"id":136}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"insert","lines":["2"],"id":137}],[{"start":{"row":45,"column":14},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":138},{"start":{"row":46,"column":0},"end":{"row":46,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":46,"column":12},"end":{"row":51,"column":14},"action":"insert","lines":["DayWiseStateTotalCasesDto(","               date=\"20/05/2020\",","               total_confirmed_cases=10,","               total_recovered_cases=2,","               total_deaths=1,","            ),"],"id":139}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"remove","lines":["0"],"id":140}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"insert","lines":["1"],"id":141}],[{"start":{"row":37,"column":148},"end":{"row":37,"column":159},"action":"remove","lines":["daily_cases"],"id":142}],[{"start":{"row":37,"column":148},"end":{"row":37,"column":149},"action":"insert","lines":["r"],"id":143},{"start":{"row":37,"column":149},"end":{"row":37,"column":150},"action":"insert","lines":["a"]},{"start":{"row":37,"column":150},"end":{"row":37,"column":151},"action":"insert","lines":["n"]},{"start":{"row":37,"column":151},"end":{"row":37,"column":152},"action":"insert","lines":["d"]},{"start":{"row":37,"column":152},"end":{"row":37,"column":153},"action":"insert","lines":["o"]},{"start":{"row":37,"column":153},"end":{"row":37,"column":154},"action":"insert","lines":["m"]}],[{"start":{"row":37,"column":154},"end":{"row":37,"column":155},"action":"insert","lines":["_"],"id":144},{"start":{"row":37,"column":155},"end":{"row":37,"column":156},"action":"insert","lines":["c"]},{"start":{"row":37,"column":156},"end":{"row":37,"column":157},"action":"insert","lines":["a"]},{"start":{"row":37,"column":157},"end":{"row":37,"column":158},"action":"insert","lines":["s"]},{"start":{"row":37,"column":158},"end":{"row":37,"column":159},"action":"insert","lines":["e"]},{"start":{"row":37,"column":159},"end":{"row":37,"column":160},"action":"insert","lines":["s"]}],[{"start":{"row":37,"column":148},"end":{"row":37,"column":160},"action":"remove","lines":["random_cases"],"id":145}],[{"start":{"row":37,"column":148},"end":{"row":37,"column":149},"action":"insert","lines":["p"],"id":146},{"start":{"row":37,"column":149},"end":{"row":37,"column":150},"action":"insert","lines":["o"]}],[{"start":{"row":37,"column":148},"end":{"row":37,"column":150},"action":"remove","lines":["po"],"id":147},{"start":{"row":37,"column":148},"end":{"row":37,"column":160},"action":"insert","lines":["post_cases()"]}],[{"start":{"row":37,"column":158},"end":{"row":37,"column":160},"action":"remove","lines":["()"],"id":148}],[{"start":{"row":69,"column":0},"end":{"row":70,"column":0},"action":"insert","lines":["",""],"id":149}],[{"start":{"row":70,"column":0},"end":{"row":103,"column":0},"action":"insert","lines":["@pytest.mark.django_db","def test_get_day_wise_state_cumulative_details_dto_when_there_is_no_case_for_dates_returns_state_total_cases_dto_with_previous_data_for_those_dates(post_cases):","","    day_wise_statistics = [","           DayWiseStateTotalCasesDto(","               date=\"20/05/2020\",","               total_confirmed_cases=10,","               total_recovered_cases=2,","               total_deaths=1,","            ),","            DayWiseStateTotalCasesDto(","               date=\"21/05/2020\",","               total_confirmed_cases=10,","               total_recovered_cases=2,","               total_deaths=1,","            ),","            DayWiseStateTotalCasesDto(","               date=\"22/05/2020\",","               total_confirmed_cases=20,","               total_recovered_cases=4,","               total_deaths=2,","            )","        ]","","    expected_output = DayWiseStateTotalCasesDtos(","               state_name=\"AndhraPradesh\",","               day_wise_statistics=day_wise_statistics","        )","    sql_storage = StorageImplementation()","","    state_total_cases_dto = sql_storage.get_day_wise_state_cumulative_dto()","","    assert expected_output == state_total_cases_dto",""],"id":150}],[{"start":{"row":71,"column":148},"end":{"row":71,"column":158},"action":"remove","lines":["post_cases"],"id":151}],[{"start":{"row":71,"column":148},"end":{"row":71,"column":149},"action":"insert","lines":["k"],"id":152},{"start":{"row":71,"column":149},"end":{"row":71,"column":150},"action":"insert","lines":["a"]}],[{"start":{"row":71,"column":148},"end":{"row":71,"column":150},"action":"remove","lines":["ka"],"id":153},{"start":{"row":71,"column":148},"end":{"row":71,"column":162},"action":"insert","lines":["kadapa_cases()"]}],[{"start":{"row":71,"column":160},"end":{"row":71,"column":162},"action":"remove","lines":["()"],"id":154}],[{"start":{"row":71,"column":4},"end":{"row":71,"column":147},"action":"remove","lines":["test_get_day_wise_state_cumulative_details_dto_when_there_is_no_case_for_dates_returns_state_total_cases_dto_with_previous_data_for_those_dates"],"id":155},{"start":{"row":71,"column":4},"end":{"row":71,"column":157},"action":"insert","lines":["test_get_day_wise_district_cumulative_details_dto_when_cases_registered_for_two_mandals_on_same_dates_returns_district_total_cases_dto_with_for_that_date"]}],[{"start":{"row":71,"column":29},"end":{"row":71,"column":30},"action":"remove","lines":["t"],"id":156},{"start":{"row":71,"column":28},"end":{"row":71,"column":29},"action":"remove","lines":["c"]},{"start":{"row":71,"column":27},"end":{"row":71,"column":28},"action":"remove","lines":["i"]},{"start":{"row":71,"column":26},"end":{"row":71,"column":27},"action":"remove","lines":["r"]},{"start":{"row":71,"column":25},"end":{"row":71,"column":26},"action":"remove","lines":["t"]},{"start":{"row":71,"column":24},"end":{"row":71,"column":25},"action":"remove","lines":["s"]},{"start":{"row":71,"column":23},"end":{"row":71,"column":24},"action":"remove","lines":["i"]},{"start":{"row":71,"column":22},"end":{"row":71,"column":23},"action":"remove","lines":["d"]}],[{"start":{"row":71,"column":22},"end":{"row":71,"column":23},"action":"insert","lines":["s"],"id":157},{"start":{"row":71,"column":23},"end":{"row":71,"column":24},"action":"insert","lines":["t"]},{"start":{"row":71,"column":24},"end":{"row":71,"column":25},"action":"insert","lines":["a"]},{"start":{"row":71,"column":25},"end":{"row":71,"column":26},"action":"insert","lines":["t"]},{"start":{"row":71,"column":26},"end":{"row":71,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":74,"column":11},"end":{"row":85,"column":14},"action":"remove","lines":["DayWiseStateTotalCasesDto(","               date=\"20/05/2020\",","               total_confirmed_cases=10,","               total_recovered_cases=2,","               total_deaths=1,","            ),","            DayWiseStateTotalCasesDto(","               date=\"21/05/2020\",","               total_confirmed_cases=10,","               total_recovered_cases=2,","               total_deaths=1,","            ),"],"id":162},{"start":{"row":74,"column":10},"end":{"row":74,"column":11},"action":"remove","lines":[" "]},{"start":{"row":74,"column":9},"end":{"row":74,"column":10},"action":"remove","lines":[" "]},{"start":{"row":74,"column":8},"end":{"row":74,"column":9},"action":"remove","lines":[" "]},{"start":{"row":74,"column":4},"end":{"row":74,"column":8},"action":"remove","lines":["    "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":73,"column":27},"end":{"row":74,"column":0},"action":"remove","lines":["",""],"id":163}],[{"start":{"row":75,"column":22},"end":{"row":75,"column":23},"action":"remove","lines":["2"],"id":164}],[{"start":{"row":75,"column":22},"end":{"row":75,"column":23},"action":"insert","lines":["0"],"id":165}],[{"start":{"row":78,"column":29},"end":{"row":78,"column":30},"action":"remove","lines":[","],"id":166}]]},"ace":{"folds":[],"scrolltop":177,"scrollleft":0,"selection":{"start":{"row":24,"column":9},"end":{"row":24,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1591178614697,"hash":"702e0e304642b514249336316f0745b9d82e00a2"}