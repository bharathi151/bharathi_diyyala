{"changed":true,"filter":false,"title":"test_get_posts_reacted_by_user.py","tooltip":"/fb_post_learning/fb_post_v2/tests/storages/test_get_posts_reacted_by_user.py","value":"import pytest\n\nfrom fb_post_v2.storages.reaction_storage_implementation import StorageImplementation\n\n\n@pytest.mark.django_db\ndef test_get_posts_reacted_by_user_given_valid_details_returns_post_ids_list(\n    create_users,\n    create_post_reactions,\n    create_post):\n    expected_post_ids_list=[1]\n    sql_storage = StorageImplementation()\n\n    post_ids_list = sql_storage.get_posts_with_more_positive_reactions()\n\n    assert expected_post_ids_list == post_ids_list","undoManager":{"mark":5,"position":8,"stack":[[{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"remove","lines":["s"],"id":2},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"remove","lines":["n"]},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"remove","lines":["o"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"remove","lines":["i"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":["t"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["c"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["a"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["e"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["r"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["_"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["e"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["v"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["i"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["t"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["i"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["s"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["o"]}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"remove","lines":["p"],"id":3},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"remove","lines":["_"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"remove","lines":["e"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"remove","lines":["r"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"remove","lines":["o"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["m"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["_"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["h"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["t"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["i"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["w"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["_"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["s"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["t"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["s"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["o"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["p"],"id":4},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["_"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["t"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["e"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["g"]}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":34},"action":"insert","lines":["get_posts_reacted_by_user"],"id":5}],[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["e"],"id":6},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["v"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["i"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["t"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["i"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["s"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["o"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["p"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["_"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["e"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["r"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["o"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["m"],"id":7},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["_"]}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"remove","lines":["t"],"id":9},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"remove","lines":["s"]},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"remove","lines":["o"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["r"],"id":10},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["e"]},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["a"]}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["c"],"id":11},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["t"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["i"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["o"]},{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":["n"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":50},"end":{"row":15,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590075199457}