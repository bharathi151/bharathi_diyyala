{"filter":false,"title":"test_make_comment_reaction.py","tooltip":"/fb_post_learning/fb_post_v2/tests/storages/test_make_comment_reaction.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":12,"column":4},"end":{"row":27,"column":0},"action":"remove","lines":["user_id = 1","    post_id = 1","    reaction_type = ReactionType.HAHA.value","    sql_storage = StorageImplementation()","","    sql_storage.react_to_post(user_id=user_id,","                              post_id=post_id,","                              reaction_type=reaction_type)","","    reaction = Reaction.objects.get(reacted_by=user_id,","                                    post_id=post_id)","","    assert reaction.reacted_by.id == user_id","    assert reaction.post.id == post_id","    assert reaction.reaction == reaction_type",""],"id":2},{"start":{"row":12,"column":4},"end":{"row":22,"column":45},"action":"insert","lines":["user_id = 1","    comment_id = 1","    comment_not_exist = False","    sql_storage = StorageImplementation()","","    sql_storage.undo_comment_reaction(user_id=user_id,","                                      comment_id=comment_id)","    actual_result = Reactions.objects.filter(user_id=user_id,","                                             comment_id=comment_id).exists()","","    assert actual_result == comment_not_exist"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":22,"column":45},"end":{"row":22,"column":45},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590421871521,"hash":"561bd79e148b881a1400bc0f61e4f23f5b145bb7"}