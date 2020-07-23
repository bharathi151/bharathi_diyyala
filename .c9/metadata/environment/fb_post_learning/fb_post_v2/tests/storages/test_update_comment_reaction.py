{"changed":true,"filter":false,"title":"test_update_comment_reaction.py","tooltip":"/fb_post_learning/fb_post_v2/tests/storages/test_update_comment_reaction.py","value":"import pytest\n\nfrom fb_post_v2.constants.enums import ReactionType\nfrom fb_post_v2.models import Reaction\nfrom fb_post_v2.storages.reaction_storage_implementation import StorageImplementation\n\n\n@pytest.mark.django_db\ndef test_update_comment_reaction_given_valid_details_updates_comment_reaction(\n    create_users,\n    create_post,\n    create_comments,\n    create_comment_reactions\n):\n    user_id = 1\n    comment_id = 1\n    reaction_type = ReactionType.HAHA.value\n    sql_storage = StorageImplementation()\n\n    sql_storage.update_comment_reaction(user_id=user_id,\n                                     comment_id=comment_id,\n                                     reaction_type=reaction_type)\n\n    reaction = Reaction.objects.get(reacted_by=user_id,\n                                    comment_id=comment_id,\n                                    reaction=reaction_type)\n\n    assert reaction.reacted_by_id == user_id\n    assert reaction.comment_id == comment_id\n    assert reaction.reaction == reaction_type\n","undoManager":{"mark":36,"position":38,"stack":[[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["t"],"id":2},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["s"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["o"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["c"],"id":3},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["o"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["m"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["m"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["n"],"id":4},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":37},"action":"remove","lines":["post_id"],"id":5},{"start":{"row":19,"column":30},"end":{"row":19,"column":40},"action":"insert","lines":["comment_id"]}],[{"start":{"row":19,"column":41},"end":{"row":19,"column":48},"action":"remove","lines":["post_id"],"id":6},{"start":{"row":19,"column":41},"end":{"row":19,"column":51},"action":"insert","lines":["comment_id"]}],[{"start":{"row":23,"column":36},"end":{"row":23,"column":43},"action":"remove","lines":["post_id"],"id":7},{"start":{"row":23,"column":36},"end":{"row":23,"column":46},"action":"insert","lines":["comment_id"]}],[{"start":{"row":23,"column":47},"end":{"row":23,"column":54},"action":"remove","lines":["post_id"],"id":8},{"start":{"row":23,"column":47},"end":{"row":23,"column":57},"action":"insert","lines":["comment_id"]}],[{"start":{"row":27,"column":31},"end":{"row":27,"column":38},"action":"remove","lines":["post_id"],"id":9},{"start":{"row":27,"column":31},"end":{"row":27,"column":41},"action":"insert","lines":["comment_id"]}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":27},"action":"remove","lines":["id"],"id":10},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"remove","lines":["."]},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"remove","lines":["t"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"remove","lines":["s"]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"remove","lines":["o"]},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":27,"column":20},"end":{"row":27,"column":30},"action":"insert","lines":["comment_id"],"id":11}],[{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["."],"id":12}],[{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["_"],"id":13}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":14},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["t"],"id":15},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["s"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["o"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["c"],"id":16},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["o"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["m"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["m"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["e"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["t"],"id":17}],[{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"remove","lines":["t"],"id":18},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"remove","lines":["s"]},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"remove","lines":["o"]},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["c"],"id":19},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["o"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["m"]},{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["m"]},{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["e"]},{"start":{"row":8,"column":66},"end":{"row":8,"column":67},"action":"insert","lines":["n"]},{"start":{"row":8,"column":67},"end":{"row":8,"column":68},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "],"id":20},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "],"id":21},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"remove","lines":[" "],"id":23}],[{"start":{"row":20,"column":37},"end":{"row":20,"column":38},"action":"remove","lines":[" "],"id":24}],[{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"remove","lines":["t"],"id":25},{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"remove","lines":["s"]},{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"remove","lines":["o"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"remove","lines":["p"]}],[{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["c"],"id":26},{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["o"]},{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["m"]},{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"insert","lines":["m"]},{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["n"],"id":27},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"remove","lines":["t"],"id":28},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["s"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["o"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["p"]}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["c"],"id":29},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["o"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["m"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":15},"action":"remove","lines":["create_comm"],"id":30},{"start":{"row":11,"column":4},"end":{"row":11,"column":30},"action":"insert","lines":["create_comment_reactions()"]}],[{"start":{"row":11,"column":28},"end":{"row":11,"column":40},"action":"remove","lines":["()_reactions"],"id":31}],[{"start":{"row":10,"column":16},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["c"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["r"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["a"],"id":33},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["t"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["e"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["v"],"id":34}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["v"],"id":35}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["c"],"id":36},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["o"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":14},"action":"remove","lines":["create_com"],"id":37},{"start":{"row":11,"column":4},"end":{"row":11,"column":21},"action":"insert","lines":["create_comments()"]}],[{"start":{"row":11,"column":19},"end":{"row":11,"column":21},"action":"remove","lines":["()"],"id":38}],[{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":[","],"id":39}],[{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"remove","lines":["h"],"id":40},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"remove","lines":["c"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"remove","lines":["r"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"remove","lines":["a"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"remove","lines":["_"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"remove","lines":["n"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["a"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["e"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["l"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["c"]}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["v"],"id":41},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["2"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":18},"end":{"row":15,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590423403186}