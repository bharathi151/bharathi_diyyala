{"filter":false,"title":"test_react_to_post.py","tooltip":"/fb_post_learning/fb_post_v2/tests/storages/test_react_to_post.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":26,"column":28},"end":{"row":26,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"1019c906288c7a44c66196457512ecbfc01d1354","undoManager":{"mark":31,"position":31,"stack":[[{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"remove","lines":["t"],"id":2},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"remove","lines":["s"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["o"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["r"],"id":3},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["e"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["a"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":51},"action":"remove","lines":["rea_storage_implementation"],"id":4},{"start":{"row":3,"column":25},"end":{"row":3,"column":56},"action":"insert","lines":["reaction_storage_implementation"]}],[{"start":{"row":12,"column":26},"end":{"row":12,"column":37},"action":"remove","lines":["create_post"],"id":5}],[{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["r"],"id":6},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["e"]},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":["a"]}],[{"start":{"row":12,"column":26},"end":{"row":12,"column":29},"action":"remove","lines":["rea"],"id":7},{"start":{"row":12,"column":26},"end":{"row":12,"column":39},"action":"insert","lines":["react_to_post"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":20},"action":"remove","lines":["post_content"],"id":8}],[{"start":{"row":6,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["@pytest.mark.django_db","def test_create_post_given_valid_details_creates_comment(create_users):","    user_id = 1","    post_content = \"Nice Post\"","    sql_storage = StorageImplementation()","","    post_id = sql_storage.react_to_post(","        user_id=user_id,","        =post_content)","","    post = Post.objects.get(id=post_id)","    assert post.id == post_id","    assert post.posted_by_id == user_id","    assert post.content == post_content",""],"id":9},{"start":{"row":6,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["@pytest.mark.django_db","def test_create_post_reaction_given_valid_details_creates_post_reaction(","create_users,","create_post","):","    user_id = 1","    post_id = 1","    reaction_type = ReactionType.HAHA.value","    sql_storage = StorageImplementation()","","    sql_storage.create_post_reaction(user_id=user_id,","                                     post_id=post_id,","                                     reaction_type=reaction_type)","","    reaction = Reactions.objects.get(user_id=user_id,","                                     post_id=post_id)","","    assert reaction.user.id == user_id","    assert reaction.post.id == post_id","    assert reaction.reaction_type == reaction_type",""]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":59},"action":"insert","lines":["from fb_post_clean_arch.constants.enums import ReactionType"],"id":11}],[{"start":{"row":17,"column":16},"end":{"row":17,"column":36},"action":"remove","lines":["create_post_reaction"],"id":12}],[{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["r"],"id":13},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["e"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["a"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["c"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["_"],"id":14},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["t"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["o"]}],[{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["_"],"id":15},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["p"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["o"]},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":["s"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"remove","lines":["s"],"id":16}],[{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"remove","lines":["t"],"id":17},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["s"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"remove","lines":["o"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"remove","lines":["P"]}],[{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["R"],"id":18},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":30},"end":{"row":3,"column":32},"action":"remove","lines":["Re"],"id":19},{"start":{"row":3,"column":30},"end":{"row":3,"column":38},"action":"insert","lines":["Reaction"]}],[{"start":{"row":24,"column":20},"end":{"row":24,"column":24},"action":"remove","lines":["user"],"id":20}],[{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["r"],"id":21},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["e"]},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":["a"]},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["c"]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["t"]},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["e"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":["_"],"id":22},{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"insert","lines":["b"]},{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["u"]}],[{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"remove","lines":["u"],"id":23}],[{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["y"],"id":24}],[{"start":{"row":21,"column":36},"end":{"row":21,"column":43},"action":"remove","lines":["user_id"],"id":25}],[{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":["r"],"id":26},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["e"]},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"insert","lines":["a"]},{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"insert","lines":["c"]},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"insert","lines":["t"]},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":["e"]},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["d"]}],[{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"insert","lines":["_"],"id":31},{"start":{"row":21,"column":44},"end":{"row":21,"column":45},"action":"insert","lines":["b"]},{"start":{"row":21,"column":45},"end":{"row":21,"column":46},"action":"insert","lines":["y"]}],[{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"remove","lines":[" "],"id":32},{"start":{"row":18,"column":32},"end":{"row":18,"column":36},"action":"remove","lines":["    "]},{"start":{"row":18,"column":28},"end":{"row":18,"column":32},"action":"remove","lines":["    "]}],[{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":[" "],"id":33},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":[" "]}],[{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"remove","lines":[" "],"id":34},{"start":{"row":19,"column":32},"end":{"row":19,"column":36},"action":"remove","lines":["    "]},{"start":{"row":19,"column":28},"end":{"row":19,"column":32},"action":"remove","lines":["    "]}],[{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":[" "],"id":35},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"insert","lines":[" "]}],[{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"remove","lines":[" "],"id":36}],[{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"remove","lines":["e"],"id":37},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["p"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["y"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["t"]},{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["_"]}]]},"timestamp":1590383797121}