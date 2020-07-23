{"filter":false,"title":"state_storage_interface.py","tooltip":"/ib_miniprojects_backend/covid_dashboard/interactors/storages/state_storage_interface.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":16,"column":78},"end":{"row":16,"column":79},"action":"insert","lines":["D"],"id":33}],[{"start":{"row":16,"column":71},"end":{"row":16,"column":93},"action":"remove","lines":["DayWiseDTotalCasesDtos"],"id":34},{"start":{"row":16,"column":71},"end":{"row":16,"column":100},"action":"insert","lines":["DayWiseDistrictTotalCasesDtos"]}],[{"start":{"row":12,"column":46},"end":{"row":12,"column":62},"action":"remove","lines":[", till_date: str"],"id":35}],[{"start":{"row":16,"column":50},"end":{"row":16,"column":66},"action":"remove","lines":[", till_date: str"],"id":36}],[{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"remove","lines":["r"],"id":37},{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"remove","lines":["t"]},{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"remove","lines":["s"]}],[{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"insert","lines":["d"],"id":38},{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":["a"]},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":["t"]},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":3},"end":{"row":28,"column":14},"action":"remove","lines":[" # @abstractmethod","    # def add_day_data_to_state_report(","    #     self,","    #     state_name: str,","    #     district_name: str,","    #     confirmed_cases:int,","    #     recovered_cases_count:int,","    #     deaths_count:int","    # ) -> int:","    #     pass"],"id":39}],[{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":["@"],"id":40},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["a"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["b"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":6},"action":"remove","lines":["ab"],"id":41},{"start":{"row":19,"column":4},"end":{"row":19,"column":20},"action":"insert","lines":["abstractmethod()"]}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":20},"action":"remove","lines":["()"],"id":42}],[{"start":{"row":19,"column":18},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":20,"column":0},"end":{"row":20,"column":3},"action":"insert","lines":["   "]},{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"insert","lines":["d"]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["e"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":[" "],"id":44}],[{"start":{"row":20,"column":7},"end":{"row":20,"column":34},"action":"insert","lines":["get_state_daily_details_dto"],"id":45}],[{"start":{"row":20,"column":34},"end":{"row":20,"column":36},"action":"insert","lines":["()"],"id":46}],[{"start":{"row":20,"column":35},"end":{"row":20,"column":36},"action":"insert","lines":["s"],"id":47},{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"insert","lines":["e"]},{"start":{"row":20,"column":37},"end":{"row":20,"column":38},"action":"insert","lines":["l"]},{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"insert","lines":["d"]}],[{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"remove","lines":["d"],"id":48}],[{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"insert","lines":["f"],"id":49},{"start":{"row":20,"column":39},"end":{"row":20,"column":40},"action":"insert","lines":[","]}],[{"start":{"row":20,"column":40},"end":{"row":20,"column":41},"action":"insert","lines":[" "],"id":50},{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"insert","lines":["t"]},{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"insert","lines":["i"]},{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"insert","lines":["l"]}],[{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"remove","lines":["l"],"id":51},{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"remove","lines":["i"]},{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"remove","lines":["t"]}],[{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"insert","lines":["d"],"id":52},{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"insert","lines":["a"]},{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"insert","lines":["t"]},{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"insert","lines":[":"],"id":53}],[{"start":{"row":20,"column":47},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":21,"column":0},"end":{"row":21,"column":7},"action":"insert","lines":["       "]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["p"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["a"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["s"],"id":55}],[{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":[" "],"id":56}],[{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"insert","lines":[" "],"id":57}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":[" "],"id":58}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"remove","lines":[" "],"id":59}],[{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":[" "],"id":60}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "],"id":61},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":48},"end":{"row":21,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":20,"column":48},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":62},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"insert","lines":["    "],"id":63}],[{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"insert","lines":[":"],"id":64}],[{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"insert","lines":[" "],"id":65},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"insert","lines":["d"]},{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"insert","lines":["a"]},{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"insert","lines":["t"]},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"insert","lines":[" "],"id":66},{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"insert","lines":["-"]}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"insert","lines":[" "],"id":67}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"remove","lines":[" "],"id":68}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"insert","lines":[">"],"id":69}],[{"start":{"row":20,"column":56},"end":{"row":20,"column":57},"action":"insert","lines":[" "],"id":70},{"start":{"row":20,"column":57},"end":{"row":20,"column":58},"action":"insert","lines":["S"]}],[{"start":{"row":20,"column":57},"end":{"row":20,"column":58},"action":"remove","lines":["S"],"id":71},{"start":{"row":20,"column":57},"end":{"row":20,"column":75},"action":"insert","lines":["StateTotalCasesDto"]}],[{"start":{"row":21,"column":12},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":99},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]},{"start":{"row":22,"column":4},"end":{"row":22,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":100}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":101}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "],"id":102}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["@"],"id":103}],[{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["d"],"id":104},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["e"]},{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["f"]}],[{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":[" "],"id":105}],[{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"remove","lines":[" "],"id":106},{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"remove","lines":["f"]},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"remove","lines":["e"]},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"remove","lines":["d"]}],[{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["a"],"id":107},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":23,"column":5},"end":{"row":23,"column":7},"action":"remove","lines":["ab"],"id":108},{"start":{"row":23,"column":5},"end":{"row":23,"column":21},"action":"insert","lines":["abstractmethod()"]}],[{"start":{"row":23,"column":19},"end":{"row":23,"column":21},"action":"remove","lines":["()"],"id":109}],[{"start":{"row":23,"column":19},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":110},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["d"]},{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"insert","lines":["e"]},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":[" "],"id":111}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":36},"action":"insert","lines":["get_day_wise_state_daily_dto"],"id":112}],[{"start":{"row":24,"column":36},"end":{"row":24,"column":38},"action":"insert","lines":["()"],"id":113}],[{"start":{"row":24,"column":37},"end":{"row":24,"column":38},"action":"insert","lines":["s"],"id":114},{"start":{"row":24,"column":38},"end":{"row":24,"column":39},"action":"insert","lines":["e"]},{"start":{"row":24,"column":39},"end":{"row":24,"column":40},"action":"insert","lines":["l"]}],[{"start":{"row":24,"column":40},"end":{"row":24,"column":41},"action":"insert","lines":["f"],"id":115},{"start":{"row":24,"column":41},"end":{"row":24,"column":42},"action":"insert","lines":[","]}],[{"start":{"row":24,"column":42},"end":{"row":24,"column":43},"action":"insert","lines":[" "],"id":116},{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"insert","lines":["d"]},{"start":{"row":24,"column":44},"end":{"row":24,"column":45},"action":"insert","lines":["a"]},{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":["t"]},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"insert","lines":[":"],"id":117}],[{"start":{"row":24,"column":48},"end":{"row":24,"column":49},"action":"insert","lines":[" "],"id":118},{"start":{"row":24,"column":49},"end":{"row":24,"column":50},"action":"insert","lines":["d"]},{"start":{"row":24,"column":50},"end":{"row":24,"column":51},"action":"insert","lines":["a"]},{"start":{"row":24,"column":51},"end":{"row":24,"column":52},"action":"insert","lines":["t"]},{"start":{"row":24,"column":52},"end":{"row":24,"column":53},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":54},"end":{"row":24,"column":55},"action":"insert","lines":[" "],"id":119},{"start":{"row":24,"column":55},"end":{"row":24,"column":56},"action":"insert","lines":["-"]},{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"insert","lines":[">"]}],[{"start":{"row":24,"column":57},"end":{"row":24,"column":58},"action":"insert","lines":[" "],"id":120}],[{"start":{"row":24,"column":58},"end":{"row":24,"column":59},"action":"insert","lines":["D"],"id":121}],[{"start":{"row":24,"column":59},"end":{"row":24,"column":60},"action":"insert","lines":["a"],"id":122},{"start":{"row":24,"column":60},"end":{"row":24,"column":61},"action":"insert","lines":["y"]},{"start":{"row":24,"column":61},"end":{"row":24,"column":62},"action":"insert","lines":["w"]}],[{"start":{"row":24,"column":61},"end":{"row":24,"column":62},"action":"remove","lines":["w"],"id":123}],[{"start":{"row":24,"column":61},"end":{"row":24,"column":62},"action":"insert","lines":["W"],"id":124},{"start":{"row":24,"column":62},"end":{"row":24,"column":63},"action":"insert","lines":["i"]},{"start":{"row":24,"column":63},"end":{"row":24,"column":64},"action":"insert","lines":["s"]},{"start":{"row":24,"column":64},"end":{"row":24,"column":65},"action":"insert","lines":["e"]},{"start":{"row":24,"column":65},"end":{"row":24,"column":66},"action":"insert","lines":["S"]}],[{"start":{"row":24,"column":58},"end":{"row":24,"column":66},"action":"remove","lines":["DayWiseS"],"id":125},{"start":{"row":24,"column":58},"end":{"row":24,"column":83},"action":"insert","lines":["DayWiseStateTotalCasesDto"]}],[{"start":{"row":24,"column":83},"end":{"row":24,"column":84},"action":"insert","lines":[":"],"id":126}],[{"start":{"row":24,"column":84},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":127},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["p"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["a"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["s"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":83},"end":{"row":24,"column":84},"action":"insert","lines":["s"],"id":128}],[{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"insert","lines":["t"],"id":129},{"start":{"row":24,"column":44},"end":{"row":24,"column":45},"action":"insert","lines":["i"]},{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":["l"]},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":["l"]},{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"insert","lines":["_"]}],[{"start":{"row":24,"column":54},"end":{"row":24,"column":58},"action":"remove","lines":["date"],"id":130}],[{"start":{"row":24,"column":54},"end":{"row":24,"column":55},"action":"insert","lines":["s"],"id":131},{"start":{"row":24,"column":55},"end":{"row":24,"column":56},"action":"insert","lines":["t"]},{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"insert","lines":["e"]},{"start":{"row":24,"column":57},"end":{"row":24,"column":58},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":57},"end":{"row":24,"column":58},"action":"remove","lines":["r"],"id":132},{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"remove","lines":["e"]}],[{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"insert","lines":["r"],"id":133}],[{"start":{"row":25,"column":12},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":134},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]},{"start":{"row":26,"column":4},"end":{"row":26,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "],"id":135}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":136}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "],"id":137}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["@"],"id":138},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["a"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":7},"action":"remove","lines":["ab"],"id":139},{"start":{"row":27,"column":5},"end":{"row":27,"column":10},"action":"insert","lines":["abs()"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":10},"action":"remove","lines":["()"],"id":140}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["t"],"id":141}],[{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["r"],"id":142}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":10},"action":"remove","lines":["abstr"],"id":143},{"start":{"row":27,"column":5},"end":{"row":27,"column":21},"action":"insert","lines":["abstractmethod()"]}],[{"start":{"row":27,"column":19},"end":{"row":27,"column":21},"action":"remove","lines":["()"],"id":144}],[{"start":{"row":27,"column":19},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":145},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":["d"]},{"start":{"row":28,"column":5},"end":{"row":28,"column":6},"action":"insert","lines":["e"]},{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":28,"column":7},"end":{"row":28,"column":8},"action":"insert","lines":[" "],"id":146}],[{"start":{"row":28,"column":8},"end":{"row":28,"column":31},"action":"insert","lines":["get_districts_zones_dto"],"id":147}],[{"start":{"row":28,"column":31},"end":{"row":28,"column":33},"action":"insert","lines":["()"],"id":148}],[{"start":{"row":28,"column":32},"end":{"row":28,"column":33},"action":"insert","lines":["s"],"id":149},{"start":{"row":28,"column":33},"end":{"row":28,"column":34},"action":"insert","lines":["e"]},{"start":{"row":28,"column":34},"end":{"row":28,"column":35},"action":"insert","lines":["l"]},{"start":{"row":28,"column":35},"end":{"row":28,"column":36},"action":"insert","lines":["f"]}],[{"start":{"row":28,"column":37},"end":{"row":28,"column":38},"action":"insert","lines":[":"],"id":150}],[{"start":{"row":28,"column":37},"end":{"row":28,"column":38},"action":"remove","lines":[":"],"id":151}],[{"start":{"row":28,"column":37},"end":{"row":28,"column":38},"action":"insert","lines":[" "],"id":152},{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":["-"]}],[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":[" "],"id":153}],[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"remove","lines":[" "],"id":154}],[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":[">"],"id":155}],[{"start":{"row":28,"column":40},"end":{"row":28,"column":41},"action":"insert","lines":[" "],"id":156},{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"insert","lines":["D"]}],[{"start":{"row":28,"column":42},"end":{"row":28,"column":43},"action":"insert","lines":["i"],"id":157}],[{"start":{"row":28,"column":41},"end":{"row":28,"column":43},"action":"remove","lines":["Di"],"id":158},{"start":{"row":28,"column":41},"end":{"row":28,"column":54},"action":"insert","lines":["DistrictZones"]}],[{"start":{"row":28,"column":54},"end":{"row":28,"column":55},"action":"insert","lines":[":"],"id":159}],[{"start":{"row":28,"column":55},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":160},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"insert","lines":["        "]},{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["p"]},{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["a"]},{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":["s"]},{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":234,"scrollleft":0,"selection":{"start":{"row":29,"column":12},"end":{"row":29,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":10,"state":"start","mode":"ace/mode/python"}},"timestamp":1591425038993,"hash":"cc6b39ff6e87bba8ac53a51ef138adfc19793edf"}