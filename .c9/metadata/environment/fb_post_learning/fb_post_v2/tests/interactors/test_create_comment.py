{"filter":false,"title":"test_create_comment.py","tooltip":"/fb_post_learning/fb_post_v2/tests/interactors/test_create_comment.py","undoManager":{"mark":34,"position":34,"stack":[[{"start":{"row":8,"column":0},"end":{"row":33,"column":46},"action":"remove","lines":["def test_create_post():","    #arrange","    user_id = 1","    post_content = \"Hii\"","    new_post_id = 1","    mock_presenter_response = {\"post_id\": new_post_id}","    storage = create_autospec(StorageInterface)","    presenter = create_autospec(PresenterInterface)","    storage.create_post.return_value = new_post_id","    presenter.get_create_post_response.return_value = mock_presenter_response","    interactor = CreatePostInteractor(","        storage = storage,","        presenter = presenter","    )","    #act","    response = interactor.create_post(","        user_id=user_id, post_content=post_content","    )","    #assert","    storage.create_post.assert_called_once_with(","        user_id=user_id, post_content=post_content","    )","    presenter.get_create_post_response.assert_called_once_with(","        post_id=new_post_id","    )","    assert response == mock_presenter_response"],"id":2}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["#"],"id":3}],[{"start":{"row":53,"column":4},"end":{"row":53,"column":5},"action":"remove","lines":["#"],"id":4}],[{"start":{"row":54,"column":4},"end":{"row":54,"column":8},"action":"insert","lines":["    "],"id":6}],[{"start":{"row":55,"column":8},"end":{"row":55,"column":12},"action":"insert","lines":["    "],"id":7}],[{"start":{"row":56,"column":4},"end":{"row":56,"column":8},"action":"insert","lines":["    "],"id":8}],[{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"remove","lines":["c"],"id":9},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"remove","lines":["#"]}],[{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"remove","lines":["s"],"id":10},{"start":{"row":62,"column":4},"end":{"row":62,"column":6},"action":"insert","lines":["ac"]}],[{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"remove","lines":["c"],"id":11}],[{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["s"],"id":12}],[{"start":{"row":62,"column":4},"end":{"row":62,"column":46},"action":"remove","lines":["assert response == mock_presenter_response"],"id":16},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"remove","lines":["    "]},{"start":{"row":61,"column":66},"end":{"row":62,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"remove","lines":["#"],"id":17}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["#"],"id":18}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":79},"action":"remove","lines":["#from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor"],"id":19},{"start":{"row":1,"column":13},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":60,"column":22},"end":{"row":60,"column":23},"action":"remove","lines":["a"],"id":20}],[{"start":{"row":60,"column":23},"end":{"row":60,"column":24},"action":"insert","lines":["a"],"id":21}],[{"start":{"row":46,"column":22},"end":{"row":46,"column":23},"action":"remove","lines":["a"],"id":22}],[{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"insert","lines":["a"],"id":23}],[{"start":{"row":33,"column":5},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":61},"action":"insert","lines":["storage.is_valid_post_id.assert_called_once_with(post_id)"],"id":25}],[{"start":{"row":17,"column":56},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["s"],"id":27}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"remove","lines":["s"],"id":28},{"start":{"row":18,"column":4},"end":{"row":18,"column":11},"action":"insert","lines":["storage"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["."],"id":29}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["i"],"id":30},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":14},"action":"remove","lines":["is"],"id":31},{"start":{"row":18,"column":12},"end":{"row":18,"column":28},"action":"insert","lines":["is_valid_post_id"]}],[{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["."],"id":32},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":["r"]}],[{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"remove","lines":["r"],"id":33},{"start":{"row":18,"column":29},"end":{"row":18,"column":41},"action":"insert","lines":["return_value"]}],[{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":[" "],"id":34},{"start":{"row":18,"column":42},"end":{"row":18,"column":43},"action":"insert","lines":["="]}],[{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"insert","lines":[" "],"id":35},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":["T"]}],[{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["R"],"id":36},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"insert","lines":["U"]}],[{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"remove","lines":["U"],"id":37},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"remove","lines":["R"]}],[{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["r"],"id":38},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"insert","lines":["u"]},{"start":{"row":18,"column":47},"end":{"row":18,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["c"],"id":39}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":55},"action":"remove","lines":["cstorage_interface"],"id":40},{"start":{"row":4,"column":37},"end":{"row":4,"column":62},"action":"insert","lines":["comment_storage_interface"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":41},"end":{"row":20,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590380020981,"hash":"a7acaf4874cb66fdc58062f7dbf97148cc019f4a"}