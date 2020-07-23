{"filter":false,"title":"test_fill_in_the_blank.py","tooltip":"/ib_miniprojects_backend/formaster/tests/interactors/test_fill_in_the_blank.py","undoManager":{"mark":42,"position":42,"stack":[[{"start":{"row":0,"column":0},"end":{"row":46,"column":0},"action":"insert","lines":["def test_mcq_question_when_valid_details_given_return_response_id():","    #arrange","    question_id = 1","    form_id = 1","    user_id = 1","    user_submitted_option_id = 1","    response_id = 1","    expected_output = {\"response_id\": 1}","    user_response_dto = UserMCQResponseDTO(","        user_id=1,","        question_id=1,","        user_submitted_option_id=1","    )","    storage = create_autospec(StorageInterface)","    presenter = create_autospec(PresenterInterface)","    storage.is_valid_form_id.return_value = True","    storage.get_form_status.return_value = True","    storage.validate_question_id_with_form.return_value = True","    storage.get_option_ids_for_question.return_value = [1, 2, 3]","    storage.create_user_mcq_response.return_value = response_id","    presenter.submit_form_response_return.return_value = expected_output","    interactor = MCQQuestionSubmitFormResponseInteractor(","        storage = storage,","        question_id=question_id,","        form_id=form_id,","        user_id=user_id,","        user_submitted_option_id=user_submitted_option_id","    )","    #act","    response = interactor.submit_form_response_wrapper(","            presenter=presenter","        )","    #assert","    assert response == expected_output","    storage.is_valid_form_id.assert_called_once_with(","        form_id=form_id","    )","    storage.get_form_status.assert_called_once_with(","        form_id=form_id","    )","    storage.validate_question_id_with_form.assert_called_once_with(","        question_id=question_id, form_id=form_id","    )","    storage.get_option_ids_for_question.assert_called_once_with(question_id=question_id)","    storage.create_user_mcq_response.assert_called_once_with(user_response_dto=user_response_dto)","    presenter.submit_form_response_return.assert_called_once()",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":6,"column":77},"action":"insert","lines":["from unittest.mock import create_autospec","import pytest","from formaster.interactors.storages.dtos import *","from formaster.exceptions.exceptions import *","from formaster.interactors.submit_form_response.mcq_question import MCQQuestionSubmitFormResponseInteractor","from formaster.interactors.presenters.presenter_interface import PresenterInterface","from formaster.interactors.storages.storage_interface import StorageInterface"],"id":3}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":4,"column":68},"end":{"row":4,"column":107},"action":"remove","lines":["MCQQuestionSubmitFormResponseInteractor"],"id":5},{"start":{"row":4,"column":68},"end":{"row":4,"column":118},"action":"insert","lines":["FillInTheBlankQuestionSubmitFormResponseInteractor"]}],[{"start":{"row":4,"column":48},"end":{"row":4,"column":60},"action":"remove","lines":["mcq_question"],"id":6}],[{"start":{"row":4,"column":48},"end":{"row":4,"column":49},"action":"insert","lines":["f"],"id":7},{"start":{"row":4,"column":49},"end":{"row":4,"column":50},"action":"insert","lines":["i"]},{"start":{"row":4,"column":50},"end":{"row":4,"column":51},"action":"insert","lines":["l"]},{"start":{"row":4,"column":51},"end":{"row":4,"column":52},"action":"insert","lines":["l"]}],[{"start":{"row":4,"column":52},"end":{"row":4,"column":53},"action":"insert","lines":["_"],"id":8},{"start":{"row":4,"column":53},"end":{"row":4,"column":54},"action":"insert","lines":["i"]},{"start":{"row":4,"column":54},"end":{"row":4,"column":55},"action":"insert","lines":["n"]},{"start":{"row":4,"column":55},"end":{"row":4,"column":56},"action":"insert","lines":["_"]},{"start":{"row":4,"column":56},"end":{"row":4,"column":57},"action":"insert","lines":["t"]},{"start":{"row":4,"column":57},"end":{"row":4,"column":58},"action":"insert","lines":["h"]},{"start":{"row":4,"column":58},"end":{"row":4,"column":59},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":59},"end":{"row":4,"column":60},"action":"insert","lines":["_"],"id":9},{"start":{"row":4,"column":60},"end":{"row":4,"column":61},"action":"insert","lines":["b"]},{"start":{"row":4,"column":61},"end":{"row":4,"column":62},"action":"insert","lines":["l"]},{"start":{"row":4,"column":62},"end":{"row":4,"column":63},"action":"insert","lines":["a"]}],[{"start":{"row":4,"column":63},"end":{"row":4,"column":64},"action":"insert","lines":["n"],"id":10},{"start":{"row":4,"column":64},"end":{"row":4,"column":65},"action":"insert","lines":["k"]}],[{"start":{"row":30,"column":17},"end":{"row":30,"column":56},"action":"remove","lines":["MCQQuestionSubmitFormResponseInteractor"],"id":11},{"start":{"row":30,"column":17},"end":{"row":30,"column":67},"action":"insert","lines":["FillInTheBlankQuestionSubmitFormResponseInteractor"]}],[{"start":{"row":35,"column":31},"end":{"row":35,"column":32},"action":"remove","lines":["d"],"id":12},{"start":{"row":35,"column":30},"end":{"row":35,"column":31},"action":"remove","lines":["i"]}],[{"start":{"row":35,"column":30},"end":{"row":35,"column":31},"action":"insert","lines":["t"],"id":13},{"start":{"row":35,"column":31},"end":{"row":35,"column":32},"action":"insert","lines":["e"]},{"start":{"row":35,"column":32},"end":{"row":35,"column":33},"action":"insert","lines":["x"]},{"start":{"row":35,"column":33},"end":{"row":35,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":35,"column":28},"end":{"row":35,"column":29},"action":"remove","lines":["n"],"id":14},{"start":{"row":35,"column":27},"end":{"row":35,"column":28},"action":"remove","lines":["o"]},{"start":{"row":35,"column":26},"end":{"row":35,"column":27},"action":"remove","lines":["i"]},{"start":{"row":35,"column":25},"end":{"row":35,"column":26},"action":"remove","lines":["t"]},{"start":{"row":35,"column":24},"end":{"row":35,"column":25},"action":"remove","lines":["p"]},{"start":{"row":35,"column":23},"end":{"row":35,"column":24},"action":"remove","lines":["o"]},{"start":{"row":35,"column":22},"end":{"row":35,"column":23},"action":"remove","lines":["_"]}],[{"start":{"row":35,"column":51},"end":{"row":35,"column":52},"action":"remove","lines":["d"],"id":15},{"start":{"row":35,"column":50},"end":{"row":35,"column":51},"action":"remove","lines":["i"]},{"start":{"row":35,"column":49},"end":{"row":35,"column":50},"action":"remove","lines":["_"]},{"start":{"row":35,"column":48},"end":{"row":35,"column":49},"action":"remove","lines":["n"]},{"start":{"row":35,"column":47},"end":{"row":35,"column":48},"action":"remove","lines":["o"]},{"start":{"row":35,"column":46},"end":{"row":35,"column":47},"action":"remove","lines":["i"]},{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"remove","lines":["t"]},{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"remove","lines":["p"]},{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"remove","lines":["o"]}],[{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"insert","lines":["t"],"id":16},{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":["e"]},{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":["x"]},{"start":{"row":35,"column":46},"end":{"row":35,"column":47},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["1"],"id":17}],[{"start":{"row":14,"column":31},"end":{"row":14,"column":33},"action":"insert","lines":["\"\""],"id":18}],[{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["w"],"id":19},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["o"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["r"]}],[{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["l"],"id":20},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"insert","lines":["d"]}],[{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"remove","lines":["d"],"id":21},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"remove","lines":["i"]},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"remove","lines":["_"]},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["n"]},{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"remove","lines":["o"]},{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"remove","lines":["i"]},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"remove","lines":["t"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["p"]}],[{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"remove","lines":["o"],"id":22}],[{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["t"],"id":23},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":8},"end":{"row":20,"column":25},"action":"remove","lines":["user_submitted_te"],"id":24},{"start":{"row":20,"column":8},"end":{"row":20,"column":27},"action":"insert","lines":["user_submitted_text"]}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["1"],"id":25}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":30},"action":"insert","lines":["\"\""],"id":26}],[{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["w"],"id":27},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"insert","lines":["o"]},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"insert","lines":["r"]},{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["l"]},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["d"],"id":28},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["i"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["_"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["n"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["o"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["i"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["t"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["p"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["o"]}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["t"],"id":29},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["e"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["x"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":24},"end":{"row":17,"column":42},"action":"remove","lines":["UserMCQResponseDTO"],"id":30}],[{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["U"],"id":31}],[{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"remove","lines":["U"],"id":32},{"start":{"row":17,"column":24},"end":{"row":17,"column":53},"action":"insert","lines":["UserFillInTheBlankResponseDTO"]}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["q"],"id":33},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["c"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["m"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["F"],"id":34},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["I"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["L"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["L"]}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["L"],"id":35},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["L"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["I"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["F"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["f"],"id":36},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["i"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["l"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["l"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["_"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["i"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["_"],"id":37},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["y"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["y"],"id":38}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["t"],"id":39},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["h"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["e"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["_"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["b"]}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["l"],"id":40},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["a"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["n"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["k"]}],[{"start":{"row":27,"column":3},"end":{"row":27,"column":64},"action":"remove","lines":[" storage.get_option_ids_for_question.return_value = [1, 2, 3]"],"id":41},{"start":{"row":27,"column":2},"end":{"row":27,"column":3},"action":"remove","lines":[" "]},{"start":{"row":27,"column":1},"end":{"row":27,"column":2},"action":"remove","lines":[" "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":26,"column":62},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":42}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":88},"action":"remove","lines":["    storage.get_option_ids_for_question.assert_called_once_with(question_id=question_id)"],"id":43},{"start":{"row":50,"column":5},"end":{"row":51,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":554,"scrollleft":0,"selection":{"start":{"row":50,"column":5},"end":{"row":50,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":26,"state":"start","mode":"ace/mode/python"}},"timestamp":1592559266054,"hash":"846f94f0c645fea67db11f957e0443be7a37054b"}