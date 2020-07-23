{"changed":true,"filter":false,"title":"test_delete_post.py","tooltip":"/fb_post_learning/fb_post_v2/tests/interactors/test_delete_post.py","value":"from unittest.mock import create_autospec\nimport pytest\nfrom fb_post_v2.interactors.delete_post_interactor import DeletePostInteractor\nfrom fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface\nfrom fb_post_v2.interactors.storages.post_storage_interface import StorageInterface\nfrom django_swagger_utils.drf_server.exceptions import NotFound, BadRequest\n\n\ndef test_delete_post_when_there_is_post_deletes_post():\n    #arrange\n    user_id = 1\n    post_id = 1\n    storage = create_autospec(StorageInterface)\n    presenter = create_autospec(PresenterInterface)\n    storage.is_valid_post_id.return_value = True\n    interactor = DeletePostInteractor(\n        storage = storage,\n        presenter = presenter\n    )\n    #act\n    interactor.delete_post(\n        user_id=user_id, post_id=post_id\n    )\n    #assert\n    storage.delete_post.assert_called_once_with(\n        user_id=user_id, post_id=post_id\n    )\n    storage.is_valid_post_id.assert_called_once_with(post_id)\n    storage.delete_post.assert_called_once_with(user_id, post_id)\n\ndef test_delete_post_with_invalid_post_id_raise_invalid_post_id_exception():\n    #arrange\n    user_id = 1\n    post_id = -1\n    storage = create_autospec(StorageInterface)\n    presenter = create_autospec(PresenterInterface)\n    storage.is_valid_post_id.return_value = False\n    presenter.raise_invalid_post_id_exception.side_effect = NotFound\n    interactor = DeletePostInteractor(\n        storage = storage,\n        presenter = presenter\n    )\n    #act\n    with pytest.raises(NotFound):\n        interactor.delete_post(\n            user_id=user_id, post_id=post_id\n        )\n    #assert\n    storage.is_valid_post_id.assert_called_once_with(post_id)\n    presenter.raise_invalid_post_id_exception.assert_called_once()\n\ndef test_delete_post_where_user_cannot_delete_post_raise_user_cannot_dele_post_exception():\n    #arrange\n    user_id = 1\n    post_id = 1\n    storage = create_autospec(StorageInterface)\n    presenter = create_autospec(PresenterInterface)\n    storage.is_valid_post_id.return_value = True\n    storage.can_user_delete_post.return_value = False\n    presenter.raise_user_cannot_delete_post_exception.side_effect = BadRequest\n    interactor = DeletePostInteractor(\n        storage = storage,\n        presenter = presenter\n    )\n    #act\n    with pytest.raises(BadRequest):\n        interactor.delete_post(\n            user_id=user_id, post_id=post_id\n        )\n    #assert\n    storage.is_valid_post_id.assert_called_once_with(post_id)\n    presenter.raise_user_cannot_delete_post_exception.assert_called_once()\n","undoManager":{"mark":-2,"position":11,"stack":[[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["t"],"id":147},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["n"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["e"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["m"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["m"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["o"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["c"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["_"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["o"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["t"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["_"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["t"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["c"],"id":148},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["a"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["e"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["r"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":20},"action":"insert","lines":["delete_post"],"id":149}],[{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"remove","lines":["n"],"id":150},{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"remove","lines":["o"]},{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"remove","lines":["i"]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"remove","lines":["t"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"remove","lines":["c"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"remove","lines":["a"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"remove","lines":["e"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"remove","lines":["r"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["_"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"remove","lines":["s"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["e"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"remove","lines":["t"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"remove","lines":["a"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"remove","lines":["e"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"remove","lines":["r"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"remove","lines":["c"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":["_"]}],[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"remove","lines":["n"],"id":151},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"remove","lines":["o"]},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"remove","lines":["i"]},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"remove","lines":["t"]},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"remove","lines":["c"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"remove","lines":["a"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":["e"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"remove","lines":["r"]}],[{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["p"],"id":152},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["o"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["s"]},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["t"]},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["_"]},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["d"]},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["l"],"id":153},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["e"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["t"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["e"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["d"]}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"remove","lines":["d"],"id":154}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["s"],"id":155},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["_"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["p"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["o"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["s"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"remove","lines":["n"],"id":156},{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"remove","lines":["o"]},{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"remove","lines":["i"]},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"remove","lines":["t"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"remove","lines":["c"]},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"remove","lines":["a"]},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"remove","lines":["e"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"remove","lines":["r"]}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["p"],"id":157},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"insert","lines":["o"]},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"insert","lines":["s"]}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":58},"action":"remove","lines":["pos_storage_interface"],"id":158},{"start":{"row":4,"column":37},"end":{"row":4,"column":59},"action":"insert","lines":["post_storage_interface"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":59},"end":{"row":4,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589866058691}